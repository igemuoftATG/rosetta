#Cite paper
#PyRosetta: a script-based interface for implementing molecular modeling algorithms using Rosetta
import random
from random import *
from rosetta import *
rosetta.init()


1q07_A = Pose()
target = Pose()

1q06_A = pose_from_pdb("1q07_A.pdb")
#making an initial pose with A chain of CueR
make_pose_from_sequence(target, "MNISDVAKITGLTSKAIRFYEEKGLVTPPMRSENGYRTYTQQHLNELTLLRQARQVGFNLEESGELVNLFNDPQRHSADVKRRTLEKVAEIERHIEELQSMRDQLLALANACPGDDSADCPIIENLSGCCHHRAG","centroid_rot")


#setup score function
scorefxn = ScoreFunction()
scorefxn.set_weight(hbond_lr_bb, 1.0)
scorefxn.set_weight(vdw, 1.0)
#scorefxn.set_weight(env, 1.0)
#scorefxn.set_weight(pair, 1.0)
#scorefxn.set_weight(cbeta, 1.0)

#set up simulation parameters
ncycles = 5000
kT = 1.0
mc = MonteCarlo(target, scorefxn, kT)

#set up Mover
movemap = MoveMap()
movemap.set_bb(True)
#small_mover = SmallMover(movemap, kT, 5)

#defining perturb_bb (dont use)
def perturb_bb (pose):
	resnum = randint(1, pose.total_residue())
	target.set_phi(resnum, 1q07_A.phi(resnum)-25+random()*50)
	target.set_psi(resnum, 1q07_A.psi(resnum)-25+random()*50)
        print "set phi to: ", target.phi(resum), "set psi to: ", target.psi(resum)
        #pose.set_phi(resnum, -57)
	#pose.set_psi(resnum, -47)
	return target 

#run simulation
for i in range(1, ncycles):
	print i
	#small_mover.apply(p)
	perturb_bb(target)
	mc.boltzmann(target)
	mc.show_scores()
	mc.show_counters()
	mc.show_state()

#dump into pdb file
mc.recover_low(p)
dump_pdb(target, "result_1.pdb")
