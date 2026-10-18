#!/usr/bin/env python3
"""Offline v5 tuned two-item policy using 15/20 first-object holdout config.
Only applies to SHA-verified synthetic MuJoCo project. No Axis account access.
"""
from pathlib import Path
import hashlib
p=Path("axis_mujoco_offline_20261018/run_benchmark.py")
s=p.read_text(encoding="utf-8")
edits=[
 ("val = 0.030 if closed and not self.disable_gripper else 0.0",
  "val = 0.023 if closed and not self.disable_gripper else 0.0"),
 ("grasp = np.array([measured[0], measured[1], 0.095])",
  "grasp = np.array([measured[0], measured[1], 0.080])"),
]
for old,new in edits:
 count=s.count(old)
 if count!=1:raise SystemExit(f'V5_PATCH_GUARD_FAIL {count}: {old}')
 s=s.replace(old,new)
p.write_text(s,encoding="utf-8")
print("V5_TWO_ITEM_BEST_SINGLE_HOLDOUT_CONFIG sha256",hashlib.sha256(s.encode()).hexdigest())
