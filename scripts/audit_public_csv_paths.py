#!/usr/bin/env python3
"""Print possible absolute/raw personal paths in public CSV artifacts.

Heuristic only. Manually review before any GitHub publication.
"""
from pathlib import Path
import re,csv
root=Path(__file__).resolve().parents[1]
pat=re.compile(r'(?:/kaggle/(?:input|working)/|/home/[^/\s]+/|[A-Za-z]:\\Users\\|/Users/[^/\s]+/|ghp_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+)')
count=0
for p in (root/'results').rglob('*.csv'):
 text=p.read_text(encoding='utf8',errors='replace')
 matches=list(pat.finditer(text))
 if matches:
  print('WARNING',p.relative_to(root),len(matches),'potential path/token occurrences')
  count+=len(matches)
print('Potential matches:',count)
print('Manual review required; this scan does not guarantee all secrets are absent.')
