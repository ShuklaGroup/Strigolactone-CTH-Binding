#idea: input coordinates of interest, have program select proper frames?
#don't load the frame of interest until the END

import numpy as np
import glob
import mdtraj as md
import argparse
import pickle as pkl
from natsort import natsorted, ns
    
round1n = natsorted(glob.glob('lig_analysis/Helices/*initial*n_terminus*'))
#round1c = natsorted(glob.glob('analysis/Helices/*initial*c_terminus*'))
round2n = natsorted(glob.glob('lig_analysis/Helices/*round2*n_terminus*'))
#round2c = natsorted(glob.glob('analysis/Helices/*round2*c_terminus*'))
round3n = natsorted(glob.glob('lig_analysis/Helices/*round3*n_terminus*'))
#round3c = natsorted(glob.glob('analysis/Helices/*round3*c_terminus*'))
round4n = natsorted(glob.glob('lig_analysis/Helices/*round4*n_terminus*'))
round5n = natsorted(glob.glob('lig_analysis/Helices/*round5*n_terminus*'))
round6n = natsorted(glob.glob('lig_analysis/Helices/*round6*n_terminus*'))
round7n = natsorted(glob.glob('lig_analysis/Helices/*round7*n_terminus*'))
round8n = natsorted(glob.glob('lig_analysis/Helices/*round8*n_terminus*'))
round9n = natsorted(glob.glob('lig_analysis/Helices/*round9*n_terminus*'))
round10n = natsorted(glob.glob('lig_analysis/Helices/*round10*n_terminus*'))
round11n = natsorted(glob.glob('lig_analysis/Helices/*round11*n_terminus*'))
round12n = natsorted(glob.glob('lig_analysis/Helices/*round12*n_terminus*'))
round13n = natsorted(glob.glob('lig_analysis/Helices/*round13*n_terminus*'))


frames = 0
for datafile in round1n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 1 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round2n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 2 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round3n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 3 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round4n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 4 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round5n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 5 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round6n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 6 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round7n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 7 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round8n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 8 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round9n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 9 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round10n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 10 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round11n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 11 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round12n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 12 has {0} microseconds'.format(microseconds)

frames = 0
for datafile in round13n: #for each trajectory
    frames = frames += datafile.n_frames
    #frames is # of steps
microseconds = frames * 2 / (10**9)
print('Round 13 has {0} microseconds'.format(microseconds)
