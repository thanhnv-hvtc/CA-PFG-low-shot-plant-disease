#!/usr/bin/env python3
"""Check the portable manuscript split and feature-row metadata (no image download needed)."""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
m=pd.read_csv(ROOT/'splits/manifest_split.csv',low_memory=False)
assert len(m)==63171 and m.image_id.is_unique
exp={('PlantDoc','train'):7175,('PlantDoc','validation'):1268,('PlantDoc','test'):444,('PlantVillage','train'):38003,('PlantVillage','validation'):5430,('PlantVillage','test'):10851}
assert m.groupby(['dataset','split']).size().to_dict()==exp
ref=m.set_index('image_id')
for bb in ['dinov2_small','resnet50']:
 for ds,n in [('plantdoc',8887),('plantvillage',54284)]:
  name=f'{ds}_metadata.csv' if bb=='dinov2_small' else f'{ds}_resnet50_metadata.csv'
  d=pd.read_csv(ROOT/'metadata'/bb/name,low_memory=False)
  assert len(d)==n and d.image_id.is_unique
  assert np.array_equal(d.feature_row.to_numpy(),np.arange(n))
  r=ref.loc[d.image_id]
  for c in ['sha1','class_id','split']:
   assert d[c].astype(str).to_numpy().tolist()==r[c].astype(str).to_numpy().tolist(),(bb,ds,c)
  print('PASS',bb,ds,n)
a=pd.read_csv(ROOT/'metadata/oxford102/oxford102_metadata.csv')
assert len(a)==8189 and a.source_class_id.nunique()==102 and a.sample_id.is_unique
assert a.image_path.str.startswith('jpg/').all()
print('PASS Oxford102 8189 rows, 102 classes; all metadata checks successful')
