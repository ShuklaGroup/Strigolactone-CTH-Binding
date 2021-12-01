import numpy as np
import glob
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm
import math
#from natsort import natsorted, ns

Point1s = sorted(glob.glob('lig_analysis/Mass/*helix_center*'))
Point2s = sorted(glob.glob('lig_analysis/Mass/*223*'))

Data_Set1 = []
Data_Set2 = []

for datafile in Point1s:
    Data_Set1.extend(np.load(datafile))

Data_Set1 = np.array(Data_Set1)

#if len(np.shape(Data_SetN)) > 1:
    #Data_SetN = Data_SetN[:,0]
    
for datafile in Point2s:
    Data_Set2.extend(np.load(datafile))

Data_Set2 = np.array(Data_Set2)

#if len(np.shape(Data_SetC)) > 1:
 #   Data_SetC = Data_SetC[:,0]

Distance = []
matrix_shape = np.shape(Data_Set1)
num_terms = matrix_shape[0]

def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt(math.pow(x1 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2) * 1.0)
    return(d)

for i in range(num_terms):
    x1 = Data_Set1[i][0]
    y1 = Data_Set1[i][1]
    z1 = Data_Set1[i][2]
    x2 = Data_Set2[i][0]
    y2 = Data_Set2[i][1]
    z2 = Data_Set2[i][2]

    dist = distance(x1, y1, z1, x2, y2, z2)
    Distance.append(dist)            

np.save('CoM_Distance_Lig.npy', Distance)
