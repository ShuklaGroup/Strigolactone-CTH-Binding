#idea: input coordinates of interest, have program select proper frames?
#don't load the frame of interest until the END

import numpy as np
import glob
import mdtraj as md
import argparse
import pickle as pkl
from natsort import natsorted, ns


targettopfile="stripped.6BRT_with_GR24.prmtop"

frames = 0
for file in glob.glob('./lig_stripped/*initial*dcd'):
    traj = md.load(file, top=targettopfile) #for each trajectory
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 1 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round2*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile) #for each trajectory
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 2 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round3*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 3 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round4*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 4 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round5*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 5 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round6*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 6 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round7*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 7 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round8*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 8 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round9*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 9 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round10*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 10 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round11*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 11 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round12*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 12 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./lig_stripped/*round13*dcd'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 13 has {0} microseconds'.format(microseconds))

#frames = 0
#for file in glob.glob('./lig_stripped/*round14*dcd'): #for each trajectory
#    traj = md.load(file, top=targettopfile)
#    frames = frames + traj.n_frames
    #frames is # of steps
#microseconds = frames * 70 / (10**6)
#print('Round 14 has {0} microseconds'.format(microseconds))

#frames = 0
#for file in glob.glob('./lig_stripped/*round15*dcd'): #for each trajectory
#    traj = md.load(file, top=targettopfile)
#    frames = frames + traj.n_frames
    #frames is # of steps
#microseconds = frames * 70 / (10**6)
#print('Round 15 has {0} microseconds'.format(microseconds))
