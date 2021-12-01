import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg") 
import numpy as np
#import mdshare
import pyemma
import glob
import argparse
from natsort import natsorted, ns

#let's do a yummy yummy MSM using helix terminal distances for a first metric pair
n_terminus_coords = []
n_group = natsorted(glob.glob('./analysis/Helices/*n_terminus*'))
for datafile in n_group:
    n_terminus_coords.extend(np.load(datafile))
n_terminus_coords = np.array(n_terminus_coords)
if len(np.shape(n_terminus_coords)) > 1:
    n_terminus_coords = n_terminus_coords[:,0]

c_terminus_coords = []
c_group = natsorted(glob.glob('./analysis/Helices/*c_terminus*'))
for datafile in c_group:
    c_terminus_coords.extend(np.load(datafile))
c_terminus_coords = np.array(c_terminus_coords)
if len(np.shape(c_terminus_coords)) > 1:
    c_terminus_coords = c_terminus_coords[:,0]
    
helicity = []
helix_group = natsorted(glob.glob('./analysis/Helical/*alpha*'))
for datafile in helix_group:
    helicity.extend(np.load(datafile))
helicity = np.array(helicity)
if len(np.shape(helicity)) > 1:
    helicity = helicity[:,0]

helix_angle = []
angle_group = natsorted(glob.glob('Whole_Helix*Sort.npy'))
for datafile in angle_group:
    helix_angle.extend(np.load(datafile))
helix_angle = np.array(helix_angle)
if len(np.shape(helix_angle)) > 1:
   helix_angle = helix_angle[:,0]   

helix_bend = []
bend_group = natsorted(glob.glob('./analysis/Helices/*between*'))
for datafile in bend_group:
    helix_bend.extend(np.load(datafile))
helix_bend = np.array(helix_bend)
if len(np.shape(helix_bend)) > 1:
   helix_bend = helix_bend[:,0]   
   
CoM = []
CoM_group = natsorted(glob.glob('CoM_Distance_Sort.npy'))
for datafile in CoM_group:
    CoM.extend(np.load(datafile))
CoM = np.array(CoM)
if len(np.shape(CoM)) > 1:
   CoM = CoM[:,0]  
    
N_266 = []
N266_group = natsorted(glob.glob('./analysis/Other_Contacts/*n_terminus*'))
for datafile in N266_group:
    N_266.extend(np.load(datafile))
N_266 = np.array(N_266)
if len(np.shape(N_266)) > 1:
   N_266 = N_266[:,0]     
    
Res229_278 = []
Res229_278_group = natsorted(glob.glob('./analysis/Other_Contacts/*229*278*'))
for datafile in Res229_278_group:
    Res229_278.extend(np.load(datafile))
Res229_278 = np.array(Res229_278)
if len(np.shape(Res229_278)) > 1:
   Res229_278 = Res229_278[:,0] 
   
all_coords = np.vstack((n_terminus_coords, c_terminus_coords, helicity, helix_angle, helix_bend, CoM, N_266, Res229_278)).T
print(all_coords)
np.save('Metric_Coords_Array.npy', all_coords)

cluster_kmeans = pyemma.coordinates.cluster_kmeans(all_coords, k=100, stride=5)
print (cluster_kmeans.dtrajs)
np.save('time_series', cluster_kmeans.dtrajs)

#slowest motion = rare events/events traveling a larger kinetic distance/slow processes

#use TICA to get new coordinates
#use for example only 8 dimensions to describe a system after feeding in 30 dimensions
#maybe try 8 starting metrics just for funsies?
tica = pyemma.coordinates.tica(all_coords, dim=4, lag=1)
tica_output = tica.get_output()
print(tica_output)
tica_feature_TIC_correlation = tica.feature_TIC_correlation
print(tica_feature_TIC_correlation)
#TICS outputs more metrics so can plot pairs of them

np.save('TICA_Data.npy', tica_output)
np.save('TICA_Feature_Correlation.npy', tica_feature_TIC_correlation)

#fig, axes = plt.subplots(1, 2, figsize=(10, 4))
#pyemma.plots.plot_feature_histograms(all_coords, feature_labels=['$x$', '$y$'], ax=axes[0])
#for i, dim in enumerate(['y', 'x']):
#    axes[0].plot(all_coords[:300, 1 - i], np.linspace(-0.2 + i, 0.8 + i, 300), color='C2', alpha=0.6)
#    axes[0].annotate(
#        '${}$(time)'.format(dim),
#        xy=(3, 0.6 + i),
#        xytext=(3, i),
#        arrowprops=dict(fc='C2', ec='None', alpha=0.6, width=2))
#pyemma.plots.plot_density(*all_coords.T, ax=axes[1])
#axes[1].set_xlabel('$x$')
#axes[1].set_ylabel('$y$')
#axes[1].set_xlim(0, 6)
#axes[1].set_ylim(0, 6)
#axes[1].set_aspect('equal')
#fig.tight_layout()
#fig.savefig('msm-data-set-1.png', dpi=300)

