#!/usr/bin/env python3
"""Tune offline MuJoCo two-item gantry controller using previous true-contact successes.

Do not claim real Axis policy/robot performance: this is a synthetic MuJoCo scene
with privileged object-position sensing + Gaussian noise. No network, wallet, Hub.
"""
from pathlib import Path
import hashlib
p=Path("axis_mujoco_offline_20261018/run_benchmark.py")
s=p.read_text(encoding="utf-8")
edits=[
 ("val = 0.023 if closed and not self.disable_gripper else 0.0",
  "val = 0.030 if closed and not self.disable_gripper else 0.0"),
 ("grasp = np.array([measured[0], measured[1], 0.065])",
  "grasp = np.array([measured[0], measured[1], 0.095])"),
 ("self.step_many(round(0.7/DT))",
  "self.step_many(round(1.2/DT))"),
]
for old,new in edits:
 n=s.count(old)
 if n!=1:raise SystemExit("V4_PATCH_FAIL: "+repr(old)+" count="+str(n))
 s=s.replace(old,new)
p.write_text(s,encoding="utf-8")
print("V4_PHYSICAL_GRASP_CONTROLLER_PATCHED_SHA256",hashlib.sha256(s.encode()).hexdigest())
