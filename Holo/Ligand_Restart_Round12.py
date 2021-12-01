import numpy as np
import glob
import mdtraj as md
import random
from natsort import natsorted, ns


index_1 = natsorted(glob.glob('lig_analysis/Helices/*initial*n_terminus*'))
index_2 = natsorted(glob.glob('lig_analysis/Helices/*round2*n_terminus*'))
index_3 = natsorted(glob.glob('lig_analysis/Helices/*round3*n_terminus*'))
index_4 = natsorted(glob.glob('lig_analysis/Helices/*round4*n_terminus*'))
index_5 = natsorted(glob.glob('lig_analysis/Helices/*round5*n_terminus*'))
index_6 = natsorted(glob.glob('lig_analysis/Helices/*round6*n_terminus*'))
index_7 = natsorted(glob.glob('lig_analysis/Helices/*round7*n_terminus*'))
index_8 = natsorted(glob.glob('lig_analysis/Helices/*round8*n_terminus*'))
index_9 = natsorted(glob.glob('lig_analysis/Helices/*round9*n_terminus*'))
index_10 = natsorted(glob.glob('lig_analysis/Helices/*round10*n_terminus*'))
index_11 = natsorted(glob.glob('lig_analysis/Helices/*round11*n_terminus*'))
index_12 = natsorted(glob.glob('lig_analysis/Helices/*round12*n_terminus*'))
index_13 = natsorted(glob.glob('lig_analysis/Helices/*round13*n_terminus*'))

Run_Num = []
Frame_Num = []
Round_Num = []

roundno = 1
p = 1
for datafile in index_1:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 2
p = 1
for datafile in index_2:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 3
p = 1
for datafile in index_3:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 4
p = 1
for datafile in index_4:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 5
p = 1
for datafile in index_5:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 6
p = 1
for datafile in index_6:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 7
p = 1
for datafile in index_7:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
   
roundno = 8
p = 1
for datafile in index_8:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
  
roundno = 9
p = 1
for datafile in index_9:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1  

roundno = 10
p = 1
for datafile in index_10:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1  

roundno = 11
p = 1
for datafile in index_11:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1  

roundno = 12
p = 1
for datafile in index_12:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

#Let's load this TICA bad boi

TICA = np.load('TICA_Data_Lig.npy', allow_pickle=True)

print(TICA)
#print(TICA[0])

datafun = []
datafun2 = []

for trajectory in TICA:
    for frame in trajectory:
        datafun.append(frame[0])
        datafun2.append(frame[2])

print(len(datafun), len(datafun2))

#resid220 = natsorted(glob.glob('lig_analysis/Contacts_For_TICA/*246_to_219*'))
#data_metric = []

#for datafile in resid220:
#    data_metric.extend(np.load(datafile))

#data_metric = np.array(data_metric)

#if len(np.shape(data_metric)) > 1:
#    data_metric = data_metric[:,0]

x_mins = [.8, 1.9, 2.1, 3.1]
x_maxs = [1.4, 2.5, 3.1, 3.6]
y_mins = [.6, -.05, 1, 1]
y_maxs = [.8, 1.1, 2, 2]

Final_Points = []

for j in range(4):
    temppoints = []
    for i in range(len(datafun)):
       Frame = int(Frame_Num[i])
       Run = int(Run_Num[i])
       Rounds = int(Round_Num[i])
       if (y_mins[j] <= datafun[i] <= y_maxs[j]) and (x_mins[j] <= datafun2[i] <= x_maxs[j]):
           temppoints.append([Frame, Run, Rounds])
    for p in range(50):
       togami = random.choice(temppoints)
       Final_Points.append(togami)

r = 1
for entry in Final_Points:
    Round = entry[2]
    Run = entry[1]
    Frame = entry[0]
    if Round == 1:
        # NEW FILE LOCATION: /home/jimingc2/ds02/Briana-CTH/trajectories etc
        traj_file = ("/home/jimingc2/ds02/Briana-CTH/lig_trajectories/6BRT_apo_helix_GR24_initial_run.dcd")
        traj_frame = md.load_frame(traj_file, Frame, top='6BRT_with_GR24.prmtop')
        if traj_frame.unitcell_volumes == None:
            continue
        else:
            traj_frame.save_amberrst7("/home/sobecks2/6BRT/Production_Runs/Ligand/Ligand_Round13/6BRT_apo_helix_GR24_round_13_run_"+str(r))
            print(traj_frame)
            r += 1
    else:
        traj_file = ("/home/jimingc2/ds02/Briana-CTH/lig_trajectories/6BRT_apo_helix_GR24_round{0}_{1}.nc".format(Round, Run))
        traj_frame = md.load_frame(traj_file, Frame, top='6BRT_with_GR24.prmtop')
        if traj_frame.unitcell_volumes == None:
            continue
        else:
            traj_frame.save_amberrst7("/home/sobecks2/6BRT/Production_Runs/Ligand/Ligand_Round13/6BRT_apo_helix_GR24_round_13_run_"+str(r))
            print(traj_frame)
            r += 1
