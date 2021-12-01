import pyemma.plots as mplt
import pyemma.msm as msm
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
#let's use a fun "toy" system to help us learn!

#P = np.array([[0.8, 0.15, 0.05, 0.0, 0.0],
#              [0.1, 0.75, 0.05, 0.05, 0.05],
#              [0.05, 0.1, 0.8, 0.0, 0.05],
#              [0.0, 0.2, 0.0, 0.8, 0.0],
#              [0.0, 0.02, 0.02, 0.0, 0.96]])

M = pkl.load(open('msm-model.pkl', 'rb'))

#M = msm.markov_model(P)
pos = np.array([[2.0,-1.5],[1,0],[2.0,1.5],[0.0,-1.5],[0.0,1.5]])
#mplt.plot_markov_model(M, pos=pos)

A = [0]
B = [4]
tpt = msm.tpt(M, A, B)

F = tpt.gross_flux
print('Flux matrix is \n', F)
print('Matrix shape is', np.shape(F))
print('Forward committor \n', tpt.committor)
print('Backward committor \n', tpt.backward_committor)
# position states long y-axis according to committor
#tptpos = np.array([tpt.committor, [0,0,0.5,-0.5,0]]).transpose()
