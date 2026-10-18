#!/usr/bin/env python3
"""Independent 20-seed holdout of single-object grasp and placement in MuJoCo.

The four parameter pairs were picked from training seed 20261018 sweep,
and holdout starts at 20261040 to avoid tuning on test seeds.
All movement is through MuJoCo native physics with collision, friction & gravity.
"""
import importlib.util
from collections import Counter
import json
from pathlib import Path

p=Path("ci-patches/axis-sweep-v3.py")
spec=importlib.util.spec_from_file_location("axis_sweep_v3",str(p))
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
candidates=[(0.080,0.023),(0.095,0.027),(0.095,0.030),(0.095,0.032)]
seeds=range(20261040,20261060)
rows=[]
for z,grip in candidates:
    outcomes=[mod.case(z,grip,seed) for seed in seeds]
    tally=dict(Counter(o["failure"] for o in outcomes))
    print(f"INDEPENDENT_FIRST_OBJECT_HOLDOUT grasp_z={z} pinch={grip} successes={sum(o.get('success',False) for o in outcomes)}/{len(outcomes)} failures={tally}",flush=True)
    rows.append({"grasp_height":z,"close_target":grip,"seeds":list(seeds),"successes":sum(o.get('success',False) for o in outcomes),"trials":len(outcomes),"failure_counts":tally,"details":outcomes})
out={"engine_version":mod.mujoco.__version__,"physics_executed":True,"holdout_seed_start":20261040,"holdout_seed_end":20261059,"training_seed":20261018,"privileged_ground_truth_sensing":True,"items_tested_per_trial":1,"candidate_count":len(candidates),"results":rows}
dest=Path("axis_mujoco_offline_20261018/results/holdout_first_object_v4.json")
dest.write_text(json.dumps(out,indent=2))
print("HOLDOUT_REPORT_SAVED",dest)
