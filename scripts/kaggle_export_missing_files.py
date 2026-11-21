#!/usr/bin/env python3
"""Run in a successful Kaggle Notebook to inventory and export small original research inputs.

This script creates a REVIEW archive. Do not upload it to a public repo without
checking manifest/metadata for platform-specific paths and personal data.
"""
from pathlib import Path
import zipfile,csv,json,io,hashlib

ROOTS=[Path('/kaggle/input'),Path('/kaggle/working')]
OUTPUT=Path('/kaggle/working/CA_PFG_Original_Small_Files_REVIEW.zip')
WANTED={
 'manifest_split.csv',
 'plantdoc_metadata.csv','plantvillage_metadata.csv',
 'plantdoc_resnet50_metadata.csv','plantvillage_resnet50_metadata.csv',
 'oxford102_metadata.csv',
 'confirmatory_task_results.csv','confirmatory_candidate_results.csv','confirmatory_protocol_audit.csv',
 'robustness_task_results.csv','robustness_candidate_results.csv','robustness_protocol_audit.csv',
 'Figure_4_Selected_Examples.csv',
}
MAX_BYTES=40*1024*1024
all_files=[]
for base in ROOTS:
 if not base.exists(): continue
 for p in base.rglob('*'):
  if not p.is_file():continue
  if p.suffix.lower()=='.npy' and ('features' in p.name.lower()):
   all_files.append({'file':p.name,'absolute_runtime_path':str(p),'size_mib':round(p.stat().st_size/1024**2,3),'kind':'FEATURE_CACHE_NOT_EXPORTED'})
  if p.name in WANTED:
   all_files.append({'file':p.name,'absolute_runtime_path':str(p),'size_mib':round(p.stat().st_size/1024**2,3),'kind':'SMALL_INPUT'})

if not all_files: raise FileNotFoundError('No matching inputs under Kaggle /input or /working')
for x in all_files: print(x['kind'], x['file'],x['size_mib'],'MiB',x['absolute_runtime_path'])

buf=io.StringIO();w=csv.DictWriter(buf,fieldnames=['file','absolute_runtime_path','size_mib','kind']);w.writeheader();w.writerows(all_files)
with zipfile.ZipFile(OUTPUT,'w',compression=zipfile.ZIP_DEFLATED) as z:
 z.writestr('INVENTORY_REVIEW_ONLY.csv',buf.getvalue())
 duplicates={}
 for x in all_files:
  if x['kind']!='SMALL_INPUT':continue
  p=Path(x['absolute_runtime_path'])
  if p.stat().st_size>MAX_BYTES:
   print('SKIP LARGE',p);continue
  # Preserve duplicates instead of silently picking the wrong version.
  duplicates[p.name]=duplicates.get(p.name,0)+1
  arc=f'candidates/{p.name}__source_{duplicates[p.name]}/{p.name}'
  z.write(p,arcname=arc)
print('REVIEW ARCHIVE:',OUTPUT)
print('IMPORTANT: inspect the inventory for duplicate filenames and paths before release.')
print('No .npy feature caches are included. Keep these in a separate authorized archive.')
