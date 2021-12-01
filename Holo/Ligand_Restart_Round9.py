import numpy as np
import glob
import mdtraj as md
import random
from natsort import natsorted, ns

#Now find five random frames from each of our 40 randomly selected filtered clusters
clust_of_interest = []
clust_of_interest.extend(np.load('lig_cluster_nums_round9.npy'))
Round_Num = []
Run_Num = []
Frame_Num = []
Original_List_Index = []
Run_Num.extend(np.load('run_num_r9.npy'))
Frame_Num.extend(np.load('frame_num_r9.npy'))
Round_Num.extend(np.load('round_num_r9.npy'))
Original_List_Index.extend(np.load('original_indices_r9.npy'))
Kmeans_values = []
Kmeans_values.extend(np.load('kmeans_lig_round9.npy'))

r = 1
for cluster_number in clust_of_interest:
    j=1
    all_points_in_cluster = []
    for v in range(len(Original_List_Index)):
        h = Kmeans_values[v]
        if h == cluster_number:
            all_points_in_cluster.append([Kmeans_values[v], Original_List_Index[v], Round_Num[v], Run_Num[v], Frame_Num[v]])
        else:
            continue                
    while j <= 5:
        if len(all_points_in_cluster) == 0:
            break
        else:
            current_frame = random.choice(all_points_in_cluster)
            print(current_frame)
            Round = current_frame[2]
            Run = current_frame[3]
            Frame = current_frame[4]
            if Round == 1:
                ##PUT NEW FILE LOCATION INFO HEREEEEEEE   /home/jimingc2/ds02/Briana-CTH/lig_trajectories etc
                traj_file = ("/home/jimingc2/ds02/Briana-CTH/lig_trajectories/6BRT_apo_helix_GR24_initial_run.dcd")
                traj_frame = md.load_frame(traj_file, Frame, top='6BRT_with_GR24.prmtop')
                if traj_frame.unitcell_volumes == None:
                    continue
                else:
                    traj_frame.save_amberrst7("/home/sobecks2/6BRT/Production_Runs/Ligand/Ligand_Round10/6BRT_apo_helix_inactive_round_10_run_"+str(r))
                    print(traj_frame)
                    r +=1
                    j +=1
            else:
                traj_file = ("/home/jimingc2/ds02/Briana-CTH/lig_trajectories/6BRT_apo_helix_GR24_round{0}_{1}.nc".format(Round, Run)) 
                traj_frame = md.load_frame(traj_file, Frame, top='6BRT_with_GR24.prmtop')
                if traj_frame.unitcell_volumes == None:
                    continue
                else:
                    traj_frame.save_amberrst7("/home/sobecks2/6BRT/Production_Runs/Ligand/Ligand_Round10/6BRT_apo_helix_GR24_round_10_run_"+str(r))
                    print(traj_frame)
                    r +=1
                    j +=1
            if j == 6:
                break
                
TICA = np.load('TICA_Data_Lig.npy')

yeet = TICA[0]
pog = yeet.T
datafun = pog[0]
datafun2 = pog[2]

x_mins = [-.5, -.8, -.5, .2]
x_maxs = [0, -.4, .1, .7]
y_mins = [.9, 1.7, 2.5, 1.2]
y_maxs = [1.2, 2.1, 4, 1.8]

Final_Points = []

for j in range(4):
   temppoints = []
   n = 25
   for i in range(len(datafun)):
       Frame = int(Frame_Num[i])
       Run = int(Run_Num[i])
       Rounds = int(Round_Num[i])
       if (y_mins[j] <= datafun[i] <= y_maxs[j]) and (x_mins[j] <= datafun2[i] <= x_maxs[j]):
           temppoints.append([Frame, Run, Rounds])
   for p in range(25):
       togami = random.choice(temppoints)
       Final_Points.append(togami)
          
print(Final_Points)

   
#Now take points

for entry in Final_Points:
    Round = entry[2]
    Run = entry[1]
    Frame = entry[0]
    if Round == 1:
        # NEW FILE LOCATION: /home/jimingc2/ds02/Briana-CTH/trajectories etc
        traj_file = ("/home/jimingc2/ds02/Briana-CTH/trajectories/6BRT_apo_helix_inactive_initial_run.nc")
        traj_frame = md.load_frame(traj_file, Frame, top='6BRT_with_GR24.prmtop')
        if traj_frame.unitcell_volumes == None:
            continue
        else:
            traj_frame.save_amberrst7("/home/sobecks2/6BRT/Production_Runs/Ligand/Ligand_Round10/6BRT_apo_helix_GR24_round_10_run_"+str(r))
            print(traj_frame)
            r += 1
    else:
        traj_file = ("/home/jimingc2/ds02/Briana-CTH/lig_trajectories/6BRT_apo_helix_GR24_round{0}_{1}.nc".format(Round, Run))
        traj_frame = md.load_frame(traj_file, Frame, top='6BRT_with_GR24.prmtop')
        if traj_frame.unitcell_volumes == None:
            continue
        else:
            traj_frame.save_amberrst7("/home/sobecks2/6BRT/Production_Runs/Ligand/Ligand_Round10/6BRT_apo_helix_GR24_round_10_run_"+str(r))
            print(traj_frame)
            r += 1
