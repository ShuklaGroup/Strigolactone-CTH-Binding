#idea: input coordinates of interest, have program select proper frames?
#don't load the frame of interest until the END

import numpy as np
import glob
import mdtraj as md
import argparse
import pickle as pkl
from natsort import natsorted, ns

Round_Num = []
Run_Num = []
Frame_Num = []
Traj_Data = []

#get the list of the runs in each round
#you're gonna have to manually edit this over time sorry
    
round1n = natsorted(glob.glob('analysis/Helices/*initial*n_terminus*'))
round2n = natsorted(glob.glob('analysis/Helices/*round2*n_terminus*'))
round3n = natsorted(glob.glob('analysis/Helices/*round3*n_terminus*'))
round4n = natsorted(glob.glob('analysis/Helices/*round4*n_terminus*'))
round5n = natsorted(glob.glob('analysis/Helices/*round5*n_terminus*'))
round6n = natsorted(glob.glob('analysis/Helices/*round6*n_terminus*'))
round7n = natsorted(glob.glob('analysis/Helices/*round7*n_terminus*'))
round8n = natsorted(glob.glob('analysis/Helices/*round8*n_terminus*'))
round9n = natsorted(glob.glob('analysis/Helices/*round9*n_terminus*'))
round10n = natsorted(glob.glob('analysis/Helices/*round10*n_terminus*'))
round11n = natsorted(glob.glob('analysis/Helices/*round11*n_terminus*'))

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
        j +=1
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
    
    
bois = np.stack((Round_Num, Run_Num, Frame_Num), axis=-1)
#print(bois)
    

def get_args():

    parser = argparse.ArgumentParser() #these are all the things you can specify when running this program
    parser.add_argument("--coord_lims", nargs=4, type=float, help="Input a range of coordinates (x,y) for checking the limit")
    parser.add_argument("--col_no", type=int, help="Put the column of TICA data you wanna see")
    parser.add_argument("--savename", type=str)
    #nargs means multiple command line arguments for a single action

    args = parser.parse_args()
    
    return args


if __name__=="__main__": #'__main__' is the name of the python module. Name is set to the name of the script or module   

    datastuff = np.load('TICA_Data.npy')
    TICA = datastuff.T
    
    Calc_N = natsorted(glob.glob('analysis/Helices/*n_terminus*'))
    Data_SetN = []   
 
    for datafile in Calc_N:
        Data_SetN.extend(np.load(datafile))

    Data_SetN = np.array(Data_SetN)

    if len(np.shape(Data_SetN)) > 1:
        Data_SetN = Data_SetN[:,0]
    
    #we input the x and y coordinates we're looking for and get them here
    args = get_args()
    x_min, x_max = args.coord_lims[0], args.coord_lims[1]
    y_min, y_max = args.coord_lims[2], args.coord_lims[3]
    
    col = args.col_no
    
    yeet = TICA[col]
    pog = len(yeet)
    datafun = yeet.reshape(pog)
    
    #now scan for all data points within the rectangle formed by these 4 coordinates
    Frames_to_Load = []
    
    for i in range(len(Run_Num)):
        Frame = int(Frame_Num[i])
        Run = int(Run_Num[i])
        Rounds = int(Round_Num[i])
        if (x_min <= Data_SetN[i] <= x_max) and (y_min <= datafun[i] <= y_max):
            Frames_to_Load.append([Frame, Run, Rounds])
            #print(Frame, Run, Rounds)
            
    print(Frames_to_Load)
    pickle_out = open(args.savename, "wb")
    pkl.dump(Frames_to_Load, pickle_out)
    pickle_out.close()
