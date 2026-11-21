#!/usr/bin/env python3
"""Extract the optional external frozen-feature ZIP, with safe paths and SHA-256 checks.

Example: python scripts/extract_feature_bundle.py --bundle /kaggle/input/.../CA-PFG_Frozen_Features_Kaggle_External.zip --output /kaggle/working/capfg_input

The bundle contains only precomputed image features, portable metadata and splits.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile, shutil

ROOT=Path(__file__).resolve().parents[1]
INDEX=json.loads((ROOT/'docs/FEATURE_CACHE_INDEX.json').read_text())['features']
MAPPING={
 'plantdoc_DINOv2':'features/dinov2_small/plantdoc_features.npy',
 'plantvillage_DINOv2':'features/dinov2_small/plantvillage_features.npy',
 'plantdoc_ResNet50':'features/resnet50/plantdoc_resnet50_features.npy',
 'plantvillage_ResNet50':'features/resnet50/plantvillage_resnet50_features.npy',
 'oxford102_ResNet50':'features/oxford102/oxford102_resnet50_features.npy',
}

def sha256_file(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(2**20),b''):h.update(chunk)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--bundle',required=True,type=Path)
 ap.add_argument('--output',type=Path,default=Path('/kaggle/working/capfg_input'))
 ap.add_argument('--verify-only',action='store_true',help='verify a previously extracted output; skip extraction')
 args=ap.parse_args()
 out=args.output.resolve()
 if not args.verify_only:
  with zipfile.ZipFile(args.bundle) as z:
   for member in z.infolist():
    name=member.filename
    if member.is_dir():continue
    target=(out/name).resolve()
    if not target.is_relative_to(out):raise ValueError('Unsafe archive path: '+name)
    target.parent.mkdir(parents=True,exist_ok=True)
    with z.open(member) as src,target.open('wb') as dst:shutil.copyfileobj(src,dst)
 print('External features path:',out)
 for key,filename in MAPPING.items():
  f=out/filename
  if not f.exists():raise FileNotFoundError(f)
  expected=INDEX[key]['sha256'];actual=sha256_file(f)
  assert actual==expected,(key,actual,expected)
  print('PASS',filename, 'SHA-256:',actual[:16])
 print('PASS: five frozen cache file hashes match Notebook provenance')
 print('All input filenames are discoverable by notebooks under:',out)
if __name__=='__main__':main()
