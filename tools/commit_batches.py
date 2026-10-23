"""Commit and push new files in batches of ~300 MB, so no single push is too large. Retries each push."""
import subprocess, pathlib, sys, time
BATCH = 300 * 1024 * 1024
def run(*a, check=True):
    r = subprocess.run(a, capture_output=True, text=True)
    if check and r.returncode:
        print('::error::' + ' '.join(a[:4]) + ' -> ' + (r.stderr or r.stdout)[-600:].replace('\n', ' | ')); sys.exit(1)
    return r
out = run('git', 'status', '--porcelain', '-uall').stdout.splitlines()
paths = [l[3:].strip('"') for l in out if l.strip()]
state = [p for p in paths if p.startswith('.tg/')]; files = [p for p in paths if not p.startswith('.tg/')]
def push():
    for k in range(5):
        r = run('git', 'push', check=False)
        if r.returncode == 0: return
        print('::warning::push failed', k, r.stderr[-500:].replace('\n', ' | ')); run('git', 'pull', '--rebase', check=False); time.sleep(10 * (k + 1))
    print('::error::push kept failing'); sys.exit(1)
batch, size, n = [], 0, 0
def flush():
    global batch, size, n
    if not batch: return
    run('git', 'add', '--', *batch); run('git', '-c', 'user.name=Mhreteabe Tesfaye', '-c', 'user.email=mhreteabetesfaye71624@gmail.com', 'commit', '-qm', f'Telegram: new files ({n + 1})')
    push(); print('pushed batch', n + 1, len(batch), 'files', size // 1048576, 'MB'); n += 1; batch, size = [], 0
for f in sorted(files):
    p = pathlib.Path(f); s = p.stat().st_size if p.exists() else 0
    if batch and size + s > BATCH: flush()
    batch.append(f); size += s
flush()
if state: batch = state; size = 0; flush()
print('done', n, 'batches')
