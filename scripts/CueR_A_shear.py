#Cite paper
#PyRosetta: a script-based interface for implementing molecular modeling algorithms using Rosetta
import random
from random import *
from rosetta import *
from rosetta.protocols.simple_moves import *

rosetta.init()

template = Pose()
target = Pose()

template = pose_from_pdb("1q07_A.pdb")

#making an initial pose with A chain of CueR
make_pose_from_sequence(target, "MNISDVAKITGLTSKAIRFYEEKGLVTPPMRSENGYRTYTQQHLNELTLLRQARQVGFNLEESGELVNLFNDPQRH","centroid_rot")
#make_pose_from_sequence(target, "TTCCPSIVARSNFNVCRLPGTSEAICATYTGCIIIPGATCPGDYAN", "fa")
#p = Pose()
#p.assign(init_pose)

#setup score function
scorefxn = ScoreFunction()
scorefxn.set_weight(hbond_lr_bb, 1.0)
scorefxn.set_weight(vdw, 1.0)
#scorefxn.set_weight(env, 1.0)
#scorefxn.set_weight(pair, 1.0)
#scorefxn.set_weight(cbeta, 1.0)

#set up simulation parameters
ncycles = 10000
kT = 1.0
mc = MonteCarlo(target, scorefxn, kT)

#set up Mover
movemap = MoveMap()
movemap.set_bb(True)

for i in range(target.n_residue()):
    target.set_secstruct(i, "H")
#defining setting angles
def set_bb(pose):
    resnum = randint(1, pose.total_residue())
    target.set_phi(resnum, template.phi(resnum)-10+random()*20)
    target.set_psi(resnum, template.psi(resnum)-10+random()*20)
    print "set phi to: ", target.phi(resnum), "set psi to: ", target.psi(resnum)
    return target

#frag_mover = ClassicFragmentMover(fragset, movemap)

#run simulation
for i in range(1, ncycles):
	print i
        set_bb(target)
	mc.boltzmann(target)
	mc.show_scores()
	mc.show_counters()
	mc.show_state()

#dump into pdb file
mc.recover_low(target)
dump_pdb(target, "result_1.pdb")
