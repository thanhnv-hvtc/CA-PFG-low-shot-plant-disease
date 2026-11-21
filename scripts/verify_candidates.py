#!/usr/bin/env python3
"""Audit supplied notebook candidate-level VALIDATION-only records.

This checks shapes/coverage/grids, NOT that model training can be replayed.
Historical selected_by / selected_as fields are single-valued and may be
non-comprehensive when multiple selectors chose the same candidate row.
"""
from pathlib import Path
import json
import pandas as pd
R=Path(__file__).resolve().parents[1]/'results'/'candidates'
a=pd.read_csv(R/'NB10_DINOv2_candidate_VALIDATION.csv')
b=pd.read_csv(R/'NB11_ResNet50_candidate_VALIDATION.csv')
assert len(a)==2520 and a.task_key.nunique()==60
assert len(b)==1080 and b.task_key.nunique()==60
assert (a.groupby('task_key').size()==42).all()
assert (b.groupby('task_key').size()==18).all()
assert set(b['method_pool'])=={'LR-Real','PFG-UnweightedLR','PFG-NW'}
assert set(a['method'])=={'LR-Real','PFG-UnweightedLR','PFG-NW','Reliability-v2','CF-Scale-NWLR-MO'}
assert set(a['C'])=={10.0,30.0,100.0}
assert set(b['C'])=={10.0,30.0,100.0}
assert a[['validation_macro_f1','validation_nll','validation_ece']].notna().all().all()
assert b[['validation_macro_f1','validation_nll','validation_ece']].notna().all().all()
rep=json.loads((R/'NB11_completion_report.json').read_text())
assert rep['all_protocol_pass'] and rep['completed_unique_tasks']==60
cfg=json.loads((R/'NB11_frozen_config.json').read_text())
assert cfg['logreg_c_grid']==[10.,30.,100.]
assert cfg['synthetic_total_weight_grid']==[0.125,0.25,0.5,1.0]
assert rep['config_hash']==(R/'NB11_frozen_config_hash.txt').read_text().strip()
print('PASS: NB10: 2520 validation-only rows, 60 tasks × 42 candidates')
print('PASS: NB11: 1080 validation-only rows, 60 tasks × 18 candidates')
print('PASS: ResNet-50 frozen configuration and completion report consistent')
print('NOTE: Exploratory NB10 candidates are NOT additional manuscript methods.')
