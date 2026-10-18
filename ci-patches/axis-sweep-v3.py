#!/usr/bin/env python3
"""Run real MuJoCo physical contact sweep offline: one object, no production Axis network.
Loads the SHA-verified baseline + deterministic v2 patch in the CI working tree.
Success is a settled physically-contacting object in the target, not mere finger contact.
"""
from __future__ import annotations
from collections import Counter
import json
from pathlib import Path
import sys
import numpy as np
import mujoco

PROJECT=Path('axis_mujoco_offline_20261018')
sys.path.insert(0, str(PROJECT.resolve()))
from run_benchmark import PhysicsTrial, SCENE, BOWL, DT

model=mujoco.MjModel.from_xml_path(str(SCENE))

def case(height, close, seed):
    t=PhysicsTrial(mujoco,model,seed,.002,False)
    measured=np.median([t.observe('a') for _ in range(5)],axis=0)
    x,y=measured[:2]
    result={'grasp_height':height,'close_target':close,'seed':seed,'failure':None}
    def snapshot(phase):
        fp=[t.data.geom_xpos[t.geom_ids[n]].round(4).tolist() for n in ('left_pad','right_pad')]
        qp=[round(float(t.data.qpos[t.model.jnt_qposadr[t.joints[n]]]),5) for n in ('finger_l','finger_r')]
        result[phase]={'object':t.position('a').round(4).tolist(),'pads':fp,'finger_qpos':qp,'grasp_contacts':t.grasp_contacts['a'],'floor_contacts':t.target_floor_contacts['a']}
    if not t.move_to([x,y,.24]):result['failure']='approach';return result
    if not t.move_to([x,y,height]):result['failure']='descent';return result
    snapshot('pre_grip')
    t.ctrl(motor_l=close,motor_r=close)
    t.step_many(round(.5/DT))
    snapshot('post_grip')
    if not t.move_to([x,y,.22]):result['failure']='lift_timeout';return result
    snapshot('post_lift')
    if not t.move_to([BOWL[0],BOWL[1],.22]):result['failure']='transport_timeout';return result
    snapshot('post_transport')
    if not t.move_to([BOWL[0],BOWL[1],.15]):result['failure']='descent_timeout';return result
    t.ctrl(motor_l=0,motor_r=0)
    t.step_many(round(1.2/DT))
    snapshot('post_release')
    result['success']=t.physically_in_target('a')
    result['distance_xy']=round(float(np.linalg.norm(t.position('a')[:2]-BOWL)),4)
    result['failure']='SUCCESS' if result['success'] else ('NO_GRASP_CONTACT' if t.grasp_contacts['a']==0 else 'MISSED_TARGET')
    return result

if __name__=='__main__':
    results=[]
    for z in (.062,.065,.070,.080,.095):
        for grip in (.023,.024,.025,.026,.027,.028,.030,.032):
            res=case(z,grip,20261018)
            results.append(res)
            print(f'z={z:.3f} grip={grip:.3f} failure={res["failure"]} dist={res.get("distance_xy")} grasp_contacts={res.get("post_grip",{}).get("grasp_contacts")} lift_z={res.get("post_lift",{}).get("object",[0,0,0])[2]}',flush=True)
    output={'engine':mujoco.__version__,'physics_executed':True,'scene':str(SCENE),'seed':20261018,'perception':'privileged object position with 0.002m Gaussian noise','total_cases':len(results),'successes':sum(r.get('success',False) for r in results),'failure_counts':dict(Counter(r['failure'] for r in results)),'cases':results}
    folder=PROJECT/'results'
    folder.mkdir(exist_ok=True)
    (folder/'contact_sweep_v3.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print('SWEEP_SUMMARY',output['successes'],len(results),output['failure_counts'])
