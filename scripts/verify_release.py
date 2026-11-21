#!/usr/bin/env python3
"""Verify public CA-PFG release contents against manuscript task counts/means.

This script does not re-run models. It audits the already-frozen real CSV results.
"""
from pathlib import Path
import sys
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'results'
A=pd.read_csv(R/'test/main_task_metrics_TEST_ONLY.csv')
assert len(A)==480, f'main task rows: {len(A)}'
assert all(A.groupby(['backbone','method']).size()==60)
assert A[['test_macro_f1','test_nll','test_ece','test_brier']].notna().all().all()
assert not A.duplicated(['backbone','dataset','shot','seed','method']).any()
for bb in ['DINOv2-Small','ResNet-50']:
 task_keys=A[A.backbone==bb][['dataset','shot','seed']].drop_duplicates()
 assert len(task_keys)==60
# Manuscript Table 3 test means (4-decimal presentation precision).
expected={
 ('DINOv2-Small','LR-Real'):(.6643,1.0782,.1181,.4356),
 ('DINOv2-Small','PFG-UnweightedLR'):(.6563,1.2169,.1233,.4556),
 ('DINOv2-Small','PFG-NW-F1Only'):(.6647,1.0690,.1089,.4325),
 ('DINOv2-Small','CA-PFG-MO'):(.6643,1.0386,.0848,.4227),
 ('ResNet-50','LR-Real'):(.5445,1.5442,.1223,.5680),
 ('ResNet-50','PFG-UnweightedLR'):(.5398,1.8976,.1719,.6144),
 ('ResNet-50','PFG-NW-F1Only'):(.5445,1.5639,.1221,.5688),
 ('ResNet-50','CA-PFG-MO'):(.5443,1.5255,.0975,.5594),
}
summary=A.groupby(['backbone','method'])[['test_macro_f1','test_nll','test_ece','test_brier']].mean()
for key,vals in expected.items():
 actual=summary.loc[key].values
 for metric,x,y in zip(['F1','NLL','ECE','Brier'],actual,vals):
  assert abs(float(x)-y) < 0.000055,(key,metric,x,y)
# Main paired effects, directional validation with exact task alignment.
for b in ['DINOv2-Small','ResNet-50']:
 s=A[A.backbone==b].pivot(index=['dataset','shot','seed'],columns='method',values=['test_macro_f1','test_nll','test_ece'])
 gap=(s[('test_macro_f1','PFG-NW-F1Only')]-s[('test_macro_f1','PFG-UnweightedLR')]).mean()
 assert abs(gap-({'DINOv2-Small':.008353,'ResNet-50':.004701}[b]))<0.000003
D=pd.read_csv(R/'external_dc_fixed/dc_adapted_task_results.csv')
assert len(D)==60 and D['task_key'].nunique()==60
S=pd.read_csv(R/'external_dc_tuned/dc_C_selected_TEST.csv')
C=pd.read_csv(R/'external_dc_tuned/dc_C_candidate_VALIDATION.csv')
assert len(S)==120 and len(C)==300
assert S['task_key'].nunique()==C['task_key'].nunique()==60
assert (C.groupby('task_key').size()==5).all()
assert (S.groupby('task_key').size()==2).all()
assert set(C['C'])=={0.01,0.1,1.0,10.0,100.0}
assert set(S['selector'])=={'F1-only','F1-NLL-ECE'}
mo=S[S.selector=='F1-NLL-ECE']
for metric,ref in [('test_macro_f1',.4977),('test_nll',1.9432),('test_ece',.1661),('test_brier',.6458)]:
 assert abs(mo[metric].mean()-ref)<0.000055,(metric,mo[metric].mean(),ref)
assert mo.chosen_C.value_counts().to_dict()=={10.0:44,100.0:11,1.0:5}
print('PASS: 480 main rows, 60 tasks/backbone, manuscript Table 3 means')
print('PASS: corrected test-only normalized influence effects')
print('PASS: 60 fixed DC tasks, 300 candidate-validation records, 120 selected test records')
print('PASS: tuned external DC Table 6 means and C-selection frequencies')
print('CAUTION: this is postprocessing validation, not a full model re-run.')
