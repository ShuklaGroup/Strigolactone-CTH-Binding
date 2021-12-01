#idea: input coordinates of interest, have program select proper frames?
#don't load the frame of interest until the END

import numpy as np
import glob
import mdtraj as md
import argparse
import pickle as pkl
from natsort import natsorted, ns


targettopfile="stripped.protein_helix_nohydrogen.prmtop"

frames = 0
for file in glob.glob('./stripped/*initial*xtc'):
    traj = md.load(file, top=targettopfile) #for each trajectory
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 1 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round2*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile) #for each trajectory
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 2 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round3*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 3 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round4*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 4 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round5*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 5 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round6*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 6 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round7*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 7 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round8*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 8 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round9*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 9 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round10*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 10 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round11*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 11 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round12*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 12 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round13*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 13 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round14*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 14 has {0} microseconds'.format(microseconds))

frames = 0
for file in glob.glob('./stripped/*round15*xtc'): #for each trajectory
    traj = md.load(file, top=targettopfile)
    frames = frames + traj.n_frames
    #frames is # of steps
microseconds = frames * 70 / (10**6)
print('Round 15 has {0} microseconds'.format(microseconds))
