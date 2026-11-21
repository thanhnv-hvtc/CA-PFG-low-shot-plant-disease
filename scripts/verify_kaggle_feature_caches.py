#!/usr/bin/env python3
"""Audit the five frozen feature arrays mounted in a Kaggle Notebook.

Usage:
  python scripts/verify_kaggle_feature_caches.py --root /kaggle/input
  python scripts/verify_kaggle_feature_caches.py --root /kaggle/input --full-hash

No changes to arrays, no training and no external downloads.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

EXPECTED = {
    'plantdoc_DINOv2': ('plantdoc_features.npy', (8887,384), '7659c87115f5679367f3def9d86b96c530c6848a98736ded647c2a7fd29007e9'),
    'plantvillage_DINOv2': ('plantvillage_features.npy', (54284,384), '360f74a8ce2d6c1b4678c30cffd422f1b09019217b1fb6e2eb77788fbeaf8e4a'),
    'plantdoc_ResNet50': ('plantdoc_resnet50_features.npy', (8887,2048), '01845ff963f01027b120210fbc4871ae1fb34890a6f4cdf66c423b3ac2ac88d9'),
    'plantvillage_ResNet50': ('plantvillage_resnet50_features.npy', (54284,2048), 'cfc4b34a0b08c369483db66c8dc1c6438babcf473aeabd539a6983d3734eae30'),
    'oxford102_ResNet50': ('oxford102_resnet50_features.npy', (8189,2048), 'd9f1b2b64739e8b5a7323ef1b52e9a066f4f76330878ca81d6ffea3ca18d7046'),
}

def digest(path: Path):
    sha = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(4*1024*1024), b''):
            sha.update(chunk)
    return sha.hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path('/kaggle/input'))
    ap.add_argument('--full-hash',action='store_true')
    args=ap.parse_args()
    if not args.root.is_dir():
        print('ERROR: input root is not a directory:',args.root)
        return 2
    passed=0
    failed=0
    for key,(filename, shape, expected_hash) in EXPECTED.items():
        matches=sorted(args.root.rglob(filename))
        if len(matches)!=1:
            print(f'FAIL {key}: expected exactly one {filename}, found {len(matches)}')
            for p in matches: print('  ',p)
            failed+=1
            continue
        path=matches[0]
        try:
            arr=np.load(path,mmap_mode='r',allow_pickle=False)
            shape_ok=tuple(arr.shape)==shape
            dtype_ok=str(arr.dtype)=='float32'
            hash_ok=(digest(path)==expected_hash) if args.full_hash else None
            ok=shape_ok and dtype_ok and (hash_ok is not False)
            print(('PASS' if ok else 'FAIL'),key,'shape',arr.shape,'dtype',arr.dtype,'file',path)
            if args.full_hash: print('  sha256_matches_reference:',hash_ok)
            if ok: passed+=1
            else: failed+=1
        except Exception as exc:
            print('FAIL',key,repr(exc))
            failed+=1
    print(f'SUMMARY: {passed}/5 passed; {failed} failed; full_hash={args.full_hash}')
    return 0 if failed==0 else 1

if __name__=='__main__':
    sys.exit(main())
