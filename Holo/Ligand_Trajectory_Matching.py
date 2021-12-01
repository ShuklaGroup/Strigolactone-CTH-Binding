#idea: input coordinates of interest, have program select proper frames?
#don't load the frame of interest until the END

import numpy as np
import glob
import mdtraj as md
import argparse
import pickle as pkl
from natsort import natsorted, ns

#Calc_C = natsorted(glob.glob('lig_analysis/Helicity/*alpha*')) #partial or alpha
#Calc_C = natsorted(glob.glob('lig_analysis/oxygen/*D-ring*'))
#Calc_C = glob.glob('Whole_Helix_vs_Protein_Angle_Lig_Sort.npy')
Calc_C = natsorted(glob.glob('lig_analysis/Ligand/*d_ring*195*'))
Calc_N = natsorted(glob.glob('lig_analysis/Ligand2/*a_ring*137*'))
#Calc_N = natsorted(glob.glob('lig_analysis/oxygen/*ABC*'))
#Calc_N = natsorted(glob.glob('lig_analysis/Other_Contacts/*c_terminus*141*'))
#Calc_N = natsorted(glob.glob('lig_analysis/Helices/*n_terminus*222*'))
#Calc_C = natsorted(glob.glob('lig_analysis/Helices/*c_terminus*222*'))
#Calc_N = natsorted(glob.glob('lig_analysis/Contacts_for_TICA/*246_to_217*'))
#Calc_C = natsorted(glob.glob('lig_analysis/Other_Contacts/*96_to_246*'))
#Calc_N = natsorted(glob.glob('lig_analysis/Other_Contacts/*200_to_286*'))
#Calc_N = natsorted(glob.glob('lig_analysis/Other_Contacts/*229_to_278*'))
#Calc_C = natsorted(glob.glob('Lig_Helix_Bending.npy'))
#Calc_N = natsorted(glob.glob('lig_analysis/Other_Contacts/*resid_266*'))

Data_SetN = []
Data_SetC = []
Round_Num = []
Run_Num = []
Frame_Num = []
Traj_Data = []

#get the list of the runs in each round
#you're gonna have to manually edit this over time sorry
    
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

#Makes an array of the N terminus compute contacts distances
#Also makes an array of all run numbers 
#we will now add the round number as well

roundno = 1
p = 1
for datafile in round1n:
    #Data_SetN.extend(np.load(datafile))
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 2
p = 1
for datafile in round2n:
    #Data_SetN.extend(np.load(datafile))
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 3
p = 1
for datafile in round3n:
    #Data_SetN.extend(np.load(datafile))
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 4
p = 1
for datafile in round4n:
    #Data_SetN.extend(np.load(datafile))
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 5
p = 1
for datafile in round5n:
    #Data_SetN.extend(np.load(datafile))
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 6
p = 1
for datafile in round6n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 7
p = 1
for datafile in round7n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j =+1
    p +=1

roundno = 8
p = 1
for datafile in round8n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 9
p = 1
for datafile in round9n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

roundno = 10
p = 1
for datafile in round10n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 11
p = 1
for datafile in round11n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 12
p = 1
for datafile in round12n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1
    
roundno = 13
p = 1
for datafile in round13n:
    j = 1
    for q in range(len(np.load(datafile))):
        Run_Num.append(p)
        Frame_Num.append(j)
        Round_Num.append(roundno)
        j +=1
    p +=1

#Data_SetN = np.array(Data_SetN)

#if len(np.shape(Data_SetN)) > 1:
#    Data_SetN = Data_SetN[:,0]
    
bois = np.stack((Round_Num, Run_Num, Frame_Num), axis=-1)
print(bois)
    
#Makes an array of the C terminus compute contacts distances

for datafile in Calc_N:
    Data_SetN.extend(np.load(datafile))

Data_SetN = np.array(Data_SetN)

if len(np.shape(Data_SetN)) > 1:
    Data_SetN = Data_SetN[:,0]
    
for datafile in Calc_C:
    Data_SetC.extend(np.load(datafile))

Data_SetC = np.array(Data_SetC)

if len(np.shape(Data_SetC)) > 1:
    Data_SetC = Data_SetC[:,0]


def get_args():

    parser = argparse.ArgumentParser() #these are all the things you can specify when running this program
    parser.add_argument("--coord_lims", nargs=4, type=float, help="Input a range of coordinates (x,y) for checking the limit")
    parser.add_argument("--savename", type=str)
    #nargs means multiple command line arguments for a single action

    args = parser.parse_args()
    
    return args

if __name__=="__main__": #'__main__' is the name of the python module. Name is set to the name of the script or module   

   #we input the x and y coordinates we're looking for and get them here
    args = get_args()
    x_min, x_max = args.coord_lims[0], args.coord_lims[1]
    y_min, y_max = args.coord_lims[2], args.coord_lims[3]
    
    print(len(Data_SetN))
    print(len(Data_SetC))
    print(len(Run_Num))    

    #now scan for all data points within the rectangle formed by these 4 coordinates
    Frames_to_Load = []
    
    for i in range(len(Run_Num)):
        Frame = int(Frame_Num[i])
        Run = int(Run_Num[i])
        Rounds = int(Round_Num[i])
        if (x_min <= Data_SetN[i] <= x_max) and (y_min <= Data_SetC[i] <= y_max):
            Frames_to_Load.append([Frame, Run, Rounds])
#            print(Frame, Run, Rounds)
        #if i == 1092838:
        #    print(Frame, Run, Rounds)
        #if i == 1093518:
        #    print(Frame, Run, Rounds)    
    
    print(Frames_to_Load)
    pickle_out = open(args.savename, "wb")
    pkl.dump(Frames_to_Load, pickle_out)
    pickle_out.close()
