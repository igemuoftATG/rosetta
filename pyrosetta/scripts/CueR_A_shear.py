#Cite paper
#PyRosetta: a script-based interface for implementing molecular modeling algorithms using Rosetta
import random
from random import *
from rosetta import *
rosetta.init()


init_pose = Pose()

#making an initial pose with A chain of CueR
#make_pose_from_sequence(init_pose, "MNISDVAKITGLTSKAIRFYEEKGLVTPPMRSENGYRTYTQQHLNELTLLRQARQVGFNLEESGELVNLFNDPQRHSADVKRRTLEKVAEIERHIEELQSMRDQLLALANACPGDDSADCPIIENLSGCCHHRAG","centroid_rot")
make_pose_from_sequence(init_pose, "MNISDVAKITGLTSKAIRFYEEKGLVTPPMRSENGYRTYTQQHLNELTLLRQARQVGFNLEESGELVNLFNDPQRHSADVKRRTLEKVAEIERHIEELQSMRDQLLALANACPGDDSADCPIIENLSGCCHHRAG","centroid")

p = Pose()
p.assign(init_pose)

#Checking initial phi, psi angle
for i in range(1, p.total_residue() + 1):
	print i, " phi = ", p.phi(i), "psi = ", p.psi(i)

#setup score function
scorefxn = ScoreFunction()
scorefxn.set_weight(hbond_lr_bb, 1.0)
scorefxn.set_weight(vdw, 1.0)
scorefxn.set_weight(env, 1.0)
scorefxn.set_weight(pair, 1.0)
scorefxn.set_weight(cbeta, 1.0)

#set up simulation parameters
ncycles = 50000
kT = 1.0
mc = MonteCarlo(p, scorefxn, kT)

#set up Mover
movemap = MoveMap()
movemap.set_bb(True)
shear_mover = ShearMover(movemap, kT, 5)

#run simulation
for i in range(1, ncycles):
	print i
	shear_mover.apply(p)
	mc.boltzmann(p)
	mc.show_scores()
	mc.show_counters()
	mc.show_state()

#dump into pdb file
mc.recover_low(p)
dump_pdb(p, "../models/CueR_shear_1.pdb")
