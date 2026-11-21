#!/usr/bin/env python3
"""Build ONE Kaggle/Drive-ready ZIP from original author feature caches.

Prerequisite: manually unpack features_DINOv2.rar with WinRAR/7-Zip to a folder;
keep features_ResNet50.zip untouched. This avoids requiring unrar in Python.

Example:
  python scripts/build_external_bundle_from_sources.py --dino-dir "C:/CA-PFG/features_DINOv2" --resnet-zip "C:/CA-PFG/features_ResNet50.zip" --oxford-npy "C:/CA-PFG/oxford102_resnet50_features.npy"
"""
from pathlib import Path
import argparse, hashlib, json, zipfile
ROOT=Path(__file__).resolve().parents[1]
INDEX=json.loads((ROOT/'docs/FEATURE_CACHE_INDEX.json').read_text())['features']
TARGET={
 'plantdoc_DINOv2':'features/dinov2_small/plantdoc_features.npy',
 'plantvillage_DINOv2':'features/dinov2_small/plantvillage_features.npy',
 'plantdoc_ResNet50':'features/resnet50/plantdoc_resnet50_features.npy',
 'plantvillage_ResNet50':'features/resnet50/plantvillage_resnet50_features.npy',
 'oxford102_ResNet50':'features/oxford102/oxford102_resnet50_features.npy',
}

def put_stream(archive,source,name,key):
 expected=INDEX[key]['sha256'];h=hashlib.sha256()
 with archive.open(name,'w',force_zip64=True) as out:
  while True:
   chunk=source.read(2*1024*1024)
   if not chunk:break
   out.write(chunk);h.update(chunk)
 if h.hexdigest()!=expected:raise ValueError(f'SHA mismatch for {key}: '+h.hexdigest())
 print('PASS:',name)

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--dino-dir',required=True,type=Path)
 p.add_argument('--resnet-zip',required=True,type=Path)
 p.add_argument('--oxford-npy',required=True,type=Path)
 p.add_argument('--output',type=Path,default=Path('CA-PFG_Frozen_Features_Kaggle_External.zip'))
 args=p.parse_args()
 with zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
  for key in ['plantdoc_DINOv2','plantvillage_DINOv2']:
   n=Path(TARGET[key]).name
   matches=list(args.dino_dir.rglob(n))
   if len(matches)!=1:raise RuntimeError(f'Expected exactly one {n}, got {matches}')
   with matches[0].open('rb') as src:put_stream(z,src,TARGET[key],key)
  with zipfile.ZipFile(args.resnet_zip) as r:
   for key in ['plantdoc_ResNet50','plantvillage_ResNet50']:
    with r.open(INDEX[key]['member']) as src:put_stream(z,src,TARGET[key],key)
  with args.oxford_npy.open('rb') as src:
   put_stream(z,src,TARGET['oxford102_ResNet50'],'oxford102_ResNet50')
  for f in [ROOT/'splits/manifest_split.csv',*sorted((ROOT/'metadata').rglob('*.csv'))]:
   z.write(f,f.relative_to(ROOT).as_posix())
  z.writestr('README_CACHE.txt','CA-PFG frozen-feature caches (no original images). Redistribution requires author review of original dataset terms. See public GitHub repository for provenance and checksum index.\n')
 print('Created:',args.output,'size MiB:',round(args.output.stat().st_size/2**20,1))
 with zipfile.ZipFile(args.output) as z:
  assert z.testzip() is None
 print('Archive CRC: PASS')
if __name__=='__main__':main()
