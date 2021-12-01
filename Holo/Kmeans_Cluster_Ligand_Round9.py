import sklearn
from sklearn.cluster import KMeans
import numpy as np
import glob
import random
import mdtraj as md
from natsort import natsorted, ns

#Generate clusters from these 4 metrics
Data_File1 = natsorted(glob.glob('lig_analysis/Helices/*n_terminus*'))
Data_File2 = natsorted(glob.glob('lig_analysis/Ligand3/*b_ring*282*'))
Data_File3 = natsorted(glob.glob('lig_analysis/Ligand/*d_ring*resid_96.npy'))
Data_File4 = natsorted(glob.glob('lig_analysis/Other_Contacts/*229_to_278*'))
Data_File5 = natsorted(glob.glob('lig_analysis/Helicity/*alpha*'))
#INCLUDE HELICAL CONTENT METRIC!!!!

Data_Set1 = []
Data_Set2 = []
Data_Set3 = []
Data_Set4 = []
Data_Set5 = []

for datafile in Data_File1:
    Data_Set1.extend(np.load(datafile))

Data_Set1 = np.array(Data_Set1)

if len(np.shape(Data_Set1)) > 1:
    Data_Set1 = Data_Set1[:,0]

for datafile in Data_File2:
    Data_Set2.extend(np.load(datafile))

Data_Set2 = np.array(Data_Set2)

if len(np.shape(Data_Set2)) > 1:
    Data_Set2 = Data_Set2[:,0]
    
for datafile in Data_File3:
    Data_Set3.extend(np.load(datafile))

Data_Set3 = np.array(Data_Set3)

if len(np.shape(Data_Set3)) > 1:
    Data_Set3 = Data_Set3[:,0]
    
for datafile in Data_File4:
    Data_Set4.extend(np.load(datafile))

Data_Set4 = np.array(Data_Set4)

if len(np.shape(Data_Set4)) > 1:
    Data_Set4 = Data_Set4[:,0]
    
for datafile in Data_File5:
    Data_Set5.extend(np.load(datafile))

Data_Set5 = np.array(Data_Set4)

if len(np.shape(Data_Set5)) > 1:
    Data_Set5 = Data_Set5[:,0]

All_Data = np.vstack((Data_Set1, Data_Set2, Data_Set3, Data_Set4, Data_Set5)).T

kmeans = KMeans(n_clusters=200, random_state=0).fit(All_Data)

print(kmeans.cluster_centers_)

original_cluster_centers = kmeans.cluster_centers_
Kmeans_values = kmeans.labels_

np.save('kmeans_lig_round9.npy', kmeans.labels_)

#Match index from the kmeans file with the number in the list of all trajectory frames
 
Original_List_Index = []
for r in range(len(Kmeans_values)):
    Original_List_Index.append(r)

#Get a list of all the round, frame and run numbers

index_1 = natsorted(glob.glob('lig_analysis/Helices/*initial*n_terminus*'))
index_2 = natsorted(glob.glob('lig_analysis/Helices/*round2*n_terminus*'))
index_3 = natsorted(glob.glob('lig_analysis/Helices/*round3*n_terminus*'))
index_4 = natsorted(glob.glob('lig_analysis/Helices/*round4*n_terminus*'))
index_5 = natsorted(glob.glob('lig_analysis/Helices/*round5*n_terminus*'))
index_6 = natsorted(glob.glob('lig_analysis/Helices/*round6*n_terminus*'))
index_7 = natsorted(glob.glob('lig_analysis/Helices/*round7*n_terminus*'))
index_8 = natsorted(glob.glob('lig_analysis/Helices/*round8*n_terminus*'))
index_9 = natsorted(glob.glob('lig_analysis/Helices/*round9*n_terminus*'))

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

#Filter out boring clusters

filtered_cluster_centers = []
filtered_cluster_label_index = []

this_cluster_number = 0
for entry in original_cluster_centers:
    if(entry[1] < 3 and entry[2] < 3):
        filtered_cluster_centers.append(entry)
        filtered_cluster_label_index.append(this_cluster_number)
    this_cluster_number += 1

print(filtered_cluster_label_index)

clust_of_interest = random.sample(filtered_cluster_label_index, 20)
print(clust_of_interest)
np.save('lig_cluster_nums_round9.npy', clust_of_interest)
np.save('run_num_r9.npy', Run_Num)
np.save('frame_num_r9.npy', Frame_Num)
np.save('round_num_r9.npy', Round_Num)
np.save('original_indices_r9.npy', Original_List_Index)

#apply filters to the numbers, but store both the actual array and the filtered array
#Gameplan: metrics 2 and 3 represent the ligand distance. We want to make it so that the distance
    #between each ligand ring and the S97 is less than 3 nm
