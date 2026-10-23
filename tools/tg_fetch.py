"""Telegram → repo. Runs in GitHub Actions (see .github/workflows/telegram.yml).

The owner forwards files from any channel to the bot. A plain text message like `textbooks/g8/maths`
sets the folder for the files that follow. Each file is downloaded at full size (MTProto, no 20 MB
limit) into that folder, files over the GitHub limit are split into parts, and the bot replies.

Secrets: TG_API_ID, TG_API_HASH, TG_BOT_TOKEN. State: .tg/state.json (offset, folder, owner).
"""
import asyncio, json, os, re, pathlib, sys, time
import requests
from pyrogram import Client

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE = ROOT / '.tg' / 'state.json'
TOKEN = os.environ['TG_BOT_TOKEN']
API = f'https://api.telegram.org/bot{TOKEN}'
LIMIT = 90 * 1024 * 1024  # GitHub refuses files over 100 MB

def load_state():
    if STATE.exists(): return json.loads(STATE.read_text())
    return {'offset': 0, 'folder': 'inbox', 'owner': None}

def save_state(s): STATE.parent.mkdir(exist_ok=True); STATE.write_text(json.dumps(s, indent=1) + '\n')

def say(chat, text):
    try: requests.post(f'{API}/sendMessage', json={'chat_id': chat, 'text': text}, timeout=30)
    except Exception as e: print('say failed', e)

def safe_name(n):
    n = re.sub(r'[^\w.\-() ሀ-፿]+', '_', n or 'file').strip() or 'file'
    return n[:120]

def split_pdf(path):
    """Split a PDF over the limit into page-range parts, halving any part still over the limit.
    Old parts of the same book (from an earlier run) are replaced, so numbering stays consistent."""
    from pypdf import PdfReader, PdfWriter
    import io
    r = PdfReader(path); n = len(r.pages)
    def chunk(a, b):  # pages [a, b) as bytes, bisected until small enough
        w = PdfWriter(); [w.add_page(r.pages[k]) for k in range(a, b)]; buf = io.BytesIO(); w.write(buf); data = buf.getvalue()
        if len(data) <= LIMIT or b - a == 1: return [data]
        m = (a + b) // 2; return chunk(a, m) + chunk(m, b)
    # first cut by estimate, then bisect anything still too big
    per = max(1, int(n * LIMIT / path.stat().st_size * 0.8)); blobs = []
    for a in range(0, n, per): blobs += chunk(a, min(n, a + per))
    for old in path.parent.glob(f'{path.stem}.part*.pdf'): old.unlink()
    parts = []
    for k, data in enumerate(blobs, 1):
        p = path.with_name(f'{path.stem}.part{k}.pdf'); p.write_bytes(data); parts.append(p)
    path.unlink(); return parts

def split_bytes(path):
    """Non-PDF over the limit: cut into raw byte parts (rejoin with cat)."""
    parts = []; k = 1
    with open(path, 'rb') as f:
        while True:
            data = f.read(LIMIT)
            if not data: break
            p = path.with_name(f'{path.name}.part{k:02d}'); p.write_bytes(data); parts.append(p); k += 1
    path.unlink(); return parts

async def main():
    s = load_state(); res = requests.get(f'{API}/getUpdates', params={'offset': s['offset'], 'timeout': 0, 'limit': 100}, timeout=60).json()
    ups = res.get('result', [])
    if not ups: print('nothing new'); return
    files = []  # (chat, folder, file_id, name, size)
    for u in ups:
        s['offset'] = u['update_id'] + 1
        m = u.get('message') or u.get('channel_post')
        if not m: continue
        chat = m['chat']['id']; frm = (m.get('from') or {}).get('id')
        if s['owner'] is None and frm: s['owner'] = frm; say(chat, 'Hello, I will save what you forward here. Send a folder name like textbooks/g8/maths to choose where.')
        if frm and frm != s['owner']: continue  # only the owner's messages
        doc = m.get('document') or m.get('audio') or m.get('video')
        txt = (m.get('text') or '').strip()
        if doc:
            name = safe_name(doc.get('file_name') or f"{doc['file_unique_id']}.bin")
            files.append((chat, s['folder'], doc['file_id'], name, doc.get('file_size', 0)))
        elif txt and re.fullmatch(r'[\w./\- ]{1,80}', txt) and not txt.startswith('/'):
            s['folder'] = txt.strip('/ ').replace(' ', '-') or 'inbox'; say(chat, f'📁 Folder: {s["folder"]}')
        elif txt == '/status':
            say(chat, f'Folder: {s["folder"]}\nFiles in repo: {sum(1 for _ in ROOT.rglob("*") if _.is_file() and ".git" not in _.parts)}')
    save_state(s)
    if not files: print('no files'); return
    app = Client('bot', api_id=int(os.environ['TG_API_ID']), api_hash=os.environ['TG_API_HASH'], bot_token=TOKEN, in_memory=True, workdir=str(ROOT / '.tg'))
    async with app:
        for chat, folder, fid, name, size in files:
            d = ROOT / folder; d.mkdir(parents=True, exist_ok=True); dest = d / name
            if (dest.exists() and dest.stat().st_size == size) or list(d.glob(f'{dest.stem}.part*.pdf')) or list(d.glob(f'{dest.name}.part*')): say(chat, f'↩︎ Already have {folder}/{name}'); continue
            t0 = time.time(); print('downloading', folder, name, size)
            try: await app.download_media(fid, file_name=str(dest))
            except Exception as e: say(chat, f'❌ {name}: {e}'); print('failed', name, e); continue
            got = [dest]
            if dest.stat().st_size > LIMIT: got = split_pdf(dest) if dest.suffix.lower() == '.pdf' else split_bytes(dest)
            mb = size / 1048576
            say(chat, f'✅ {folder}/{name} ({mb:.0f} MB, {time.time() - t0:.0f}s)' + (f' → split into {len(got)} parts' if len(got) > 1 else ''))
    print('done', len(files))

asyncio.run(main())
