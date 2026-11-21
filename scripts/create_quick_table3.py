#!/usr/bin/env python3
"""Recreate Table 3 descriptive means and standard deviations from test-only columns."""
from pathlib import Path
import pandas as pd
R=Path(__file__).resolve().parents[1]
src=R/'results/test/main_task_metrics_TEST_ONLY.csv'
df=pd.read_csv(src)
cols=['test_macro_f1','test_nll','test_ece','test_brier']
t=df.groupby(['backbone','method'],sort=False)[cols].agg(['mean','std'])
print(t.to_string(float_format=lambda x:f'{x:.4f}'))
