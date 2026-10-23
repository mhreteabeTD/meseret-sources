"""Apply tools/moves.json with git mv / git rm (run on GitHub, where all files are present)."""
import json, subprocess, pathlib, sys
m = json.load(open('tools/moves.json')); n = 0
for src, dst in m['moves'].items():
    if not pathlib.Path(src).exists(): print('missing', src); continue
    pathlib.Path(dst).parent.mkdir(parents=True, exist_ok=True); subprocess.run(['git', 'mv', src, dst], check=True); n += 1
for p in m['drops']:
    if pathlib.Path(p).exists(): subprocess.run(['git', 'rm', '-q', p], check=True)
print('moved', n, 'dropped', len(m['drops']))
