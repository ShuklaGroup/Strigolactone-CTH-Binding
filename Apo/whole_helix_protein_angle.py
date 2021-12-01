import numpy as np
import glob
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

Vector1s = sorted(glob.glob('analysis/Orientation/*whole_helix*'))
Vector2s = sorted(glob.glob('analysis/Orientation/*223*'))

Data_Set1 = []
Data_Set2 = []

for datafile in Vector1s:
    Data_Set1.extend(np.load(datafile))

Data_Set1 = np.array(Data_Set1)

#if len(np.shape(Data_SetN)) > 1:
    #Data_SetN = Data_SetN[:,0]
    
for datafile in Vector2s:
    Data_Set2.extend(np.load(datafile))

Data_Set2 = np.array(Data_Set2)

#if len(np.shape(Data_SetC)) > 1:
 #   Data_SetC = Data_SetC[:,0]

Helix_Bend_Angle = []
matrix_shape = np.shape(Data_Set1)
num_terms = matrix_shape[0]

for i in range(num_terms):
    vec1 = Data_Set1[i]
    vec2 = Data_Set2[i]
    c = dot(vec1, vec2)/norm(vec1)/norm(vec2)
    bend_angle = arccos(clip(c, -1, 1))
    Helix_Bend_Angle.append(bend_angle)
            

np.save('Whole_Helix_vs_Protein_Angle.npy', Helix_Bend_Angle)
