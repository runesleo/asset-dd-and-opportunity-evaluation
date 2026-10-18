#!/usr/bin/env python3
"""Bounded offline MuJoCo controller patch v2; no Axis network/account operations.
The v1 tar.xz is verified by SHA before applying this exact text patch.
"""
from pathlib import Path
import hashlib
p = Path('axis_mujoco_offline_20261018/run_benchmark.py')
s = p.read_text(encoding='utf-8')
changes = [
    # v1 had 1.2 cm of gripper penetration into each side of a 2.3-cm-radius ball.
    ("val = 0.032 if closed and not self.disable_gripper else 0.0",
     "val = 0.023 if closed and not self.disable_gripper else 0.0"),
    # v1 fingers were vertically above object centre when closing, causing ejection.
    ("grasp = np.array([measured[0], measured[1], 0.095])",
     "grasp = np.array([measured[0], measured[1], 0.065])"),
    ("self.events.append({\"event\":f\"grasp_{item}\", \"contacts\":self.grasp_contacts[item]})",
     "self.events.append({\"event\":f\"grasp_{item}\", \"contacts\":self.grasp_contacts[item], \"object_pos\":self.position(item).round(4).tolist()})"),
    ("if not self.move_to([measured[0],measured[1],0.25]): failure=f\"LIFT_TIMEOUT_{item}\"; break",
     "if not self.move_to([measured[0],measured[1],0.22]): failure=f\"LIFT_TIMEOUT_{item}\"; break\n                self.events.append({\"event\":f\"post_lift_{item}\", \"object_pos\":self.position(item).round(4).tolist()})"),
    ("if not self.move_to([BOWL[0],BOWL[1],0.22]): failure=f\"TRANSPORT_TIMEOUT_{item}\"; break",
     "if not self.move_to([BOWL[0],BOWL[1],0.22]): failure=f\"TRANSPORT_TIMEOUT_{item}\"; break\n                self.events.append({\"event\":f\"post_transport_{item}\", \"object_pos\":self.position(item).round(4).tolist()})"),
]
for old, new in changes:
    if s.count(old) != 1:
        raise SystemExit(f'PATCH_CONTRACT_FAILED occurrence={s.count(old)}: {old[:95]}')
    s = s.replace(old, new)
p.write_text(s, encoding='utf-8')
print('CI_PATCH_V2_APPLIED sha256=', hashlib.sha256(s.encode()).hexdigest())
