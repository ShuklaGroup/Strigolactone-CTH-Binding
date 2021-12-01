import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg") 
import numpy as np
#import mdshare
import pyemma
import glob
import argparse
from natsort import natsorted, ns

"""
#let's do a yummy yummy MSM using helix terminal distances for a first metric pair
n_terminus_coords = []
n_group = natsorted(glob.glob('./lig_analysis/Helices/*n_terminus*'))
for datafile in n_group:
    n_terminus_coords.extend(np.load(datafile))
n_terminus_coords = np.array(n_terminus_coords)
if len(np.shape(n_terminus_coords)) > 1:
    n_terminus_coords = n_terminus_coords[:,0]

c_terminus_coords = []
c_group = natsorted(glob.glob('./lig_analysis/Helices/*c_terminus*'))
for datafile in c_group:
    c_terminus_coords.extend(np.load(datafile))
c_terminus_coords = np.array(c_terminus_coords)
if len(np.shape(c_terminus_coords)) > 1:
    c_terminus_coords = c_terminus_coords[:,0]
    
helicity = []
helix_group = natsorted(glob.glob('./lig_analysis/Helicity/*alpha*'))
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
bend_group = natsorted(glob.glob('./lig_analysis/Helices/*between*'))
for datafile in bend_group:
    helix_bend.extend(np.load(datafile))
helix_bend = np.array(helix_bend)
if len(np.shape(helix_bend)) > 1:
   helix_bend = helix_bend[:,0]   
   
CoM = []
CoM_group = natsorted(glob.glob('CoM_Distance_Lig_Sort.npy'))
for datafile in CoM_group:
    CoM.extend(np.load(datafile))
CoM = np.array(CoM)
if len(np.shape(CoM)) > 1:
   CoM = CoM[:,0]  
    
N_266 = []
N266_group = natsorted(glob.glob('./lig_analysis/Other_Contacts/*n_terminus*'))
for datafile in N266_group:
    N_266.extend(np.load(datafile))
N_266 = np.array(N_266)
if len(np.shape(N_266)) > 1:
   N_266 = N_266[:,0]     
    
Res229_278 = []
Res229_278_group = natsorted(glob.glob('./lig_analysis/Other_Contacts/*229*278*'))
for datafile in Res229_278_group:
    Res229_278.extend(np.load(datafile))
Res229_278 = np.array(Res229_278)
if len(np.shape(Res229_278)) > 1:
   Res229_278 = Res229_278[:,0] 
   
Res130_286 = []
Res130_286_group = natsorted(glob.glob('./lig_analysis/Other_Contacts/*130_to_286*'))
for datafile in Res130_286_group:
    Res130_286.extend(np.load(datafile))
Res130_286 = np.array(Res130_286)
if len(np.shape(Res130_286)) > 1:
   Res130_286 = Res130_286[:,0] 
   
D96 = []
D96_group = natsorted(glob.glob('./lig_analysis/Ligand/*d_ring*96*'))
for datafile in D96_group:
    D96.extend(np.load(datafile))
D96 = np.array(D96)
if len(np.shape(D96)) > 1:
   D96 = D96[:,0] 
 
D195 = []
D195_group = natsorted(glob.glob('./lig_analysis/Ligand/*d_ring*195*'))
for datafile in D195_group:
    D195.extend(np.load(datafile))
D195 = np.array(D195)
if len(np.shape(D195)) > 1:
   D195 = D195[:,0] 

A96 = []
A96_group = natsorted(glob.glob('./lig_analysis/Ligand/*a_ring*96*'))
for datafile in A96_group:
    A96.extend(np.load(datafile))
A96 = np.array(A96)
if len(np.shape(A96)) > 1:
   A96 = A96[:,0] 

D222 = []
D222_group = natsorted(glob.glob('./lig_analysis/Ligand2/*d_ring*222*'))
for datafile in D222_group:
    D222.extend(np.load(datafile))
D222 = np.array(D222)
if len(np.shape(D222)) > 1:
   D222 = D222[:,0] 

A222 = []
A222_group = natsorted(glob.glob('./lig_analysis/Ligand2/*a_ring*222*'))
for datafile in A222_group:
    A222.extend(np.load(datafile))
A222 = np.array(A222)
if len(np.shape(A222)) > 1:
   A222 = A222[:,0]

D284 = []
D284_group = natsorted(glob.glob('./lig_analysis/Ligand3/*d_ring*284*'))
for datafile in D284_group:
    D284.extend(np.load(datafile))
D284 = np.array(D284)
if len(np.shape(D284)) > 1:
   D284 = D284[:,0]
   
B282 = []
B282_group = natsorted(glob.glob('./lig_analysis/Ligand3/*b_ring*282*'))
for datafile in B282_group:
    B282.extend(np.load(datafile))
B282 = np.array(B282)
if len(np.shape(B282)) > 1:
   B282 = B282[:,0]

Res246_215 = []
Res246_215_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*215*'))
for datafile in Res246_215_group:
    Res246_215.extend(np.load(datafile))
Res246_215 = np.array(Res246_215)
if len(np.shape(Res246_215)) > 1:
   Res246_215 = Res246_215[:,0]
   
Res246_216 = []
Res246_216_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*216*'))
for datafile in Res246_216_group:
    Res246_216.extend(np.load(datafile))
Res246_216 = np.array(Res246_216)
if len(np.shape(Res246_216)) > 1:
   Res246_216 = Res246_216[:,0]
   
Res246_217 = []
Res246_217_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*217*'))
for datafile in Res246_217_group:
    Res246_217.extend(np.load(datafile))
Res246_217 = np.array(Res246_217)
if len(np.shape(Res246_217)) > 1:
   Res246_217 = Res246_217[:,0]

Res246_218 = []
Res246_218_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*218*'))
for datafile in Res246_218_group:
    Res246_218.extend(np.load(datafile))
Res246_218 = np.array(Res246_218)
if len(np.shape(Res246_218)) > 1:
   Res246_218 = Res246_218[:,0]
   
Res246_219 = []
Res246_219_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*219*'))
for datafile in Res246_219_group:
    Res246_219.extend(np.load(datafile))
Res246_219 = np.array(Res246_219)
if len(np.shape(Res246_219)) > 1:
   Res246_219 = Res246_219[:,0]
   
Res246_220 = []
Res246_220_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*220*'))
for datafile in Res246_220_group:
    Res246_220.extend(np.load(datafile))
Res246_220 = np.array(Res246_220)
if len(np.shape(Res246_220)) > 1:
   Res246_220 = Res246_220[:,0]

Res246_221 = []
Res246_221_group = natsorted(glob.glob('./lig_analysis/Contacts_for_TICA/*246*221*'))
for datafile in Res246_221_group:
    Res246_221.extend(np.load(datafile))
Res246_221 = np.array(Res246_221)
if len(np.shape(Res246_221)) > 1:
   Res246_221 = Res246_221[:,0]
"""

#jiming code starts here

feat_identifiers = []

#broken up for readability
feat_identifiers.extend(['./lig_analysis/Helices/*n_terminus*', './lig_analysis/Helices/*c_terminus*', './lig_analysis/Helicity/*alpha*', './lig_analysis/Helices/*between*', './lig_analysis/Other_Contacts/*n_terminus*']) 
feat_identifiers.extend(['./lig_analysis/Other_Contacts/*229*278*', './lig_analysis/Other_Contacts/*130_to_286*', './lig_analysis/Ligand/*d_ring*96*', './lig_analysis/Ligand/*d_ring*195*', './lig_analysis/Ligand/*a_ring*96*']) 
feat_identifiers.extend(['./lig_analysis/Ligand2/*d_ring*222*', './lig_analysis/Ligand2/*a_ring*222*', './lig_analysis/Ligand3/*d_ring*284*', './lig_analysis/Ligand3/*b_ring*282*']) 
feat_identifiers.extend(['./lig_analysis/Contacts_for_TICA/*246*215*', './lig_analysis/Contacts_for_TICA/*246*216*', './lig_analysis/Contacts_for_TICA/*246*217*', './lig_analysis/Contacts_for_TICA/*246*218*']) 
feat_identifiers.extend(['./lig_analysis/Contacts_for_TICA/*246*219*', './lig_analysis/Contacts_for_TICA/*246*220*', './lig_analysis/Contacts_for_TICA/*246*221*']) 

file_lists = []

#params_used = open("Parameters.txt",'w')
for ft in feat_identifiers:
    #params_used.write("%s \n"%ft)
    file_lists.append(natsorted(glob.glob(ft)))

feat_all = []
for i in range(len(file_lists[0])): #Iterate through features
    feat = [] #Initialize feature for j-th trajectory
    for j in range(len(file_lists)):
        #print(file_lists[j][i])
        #print(np.shape(np.load(file_lists[j][i])))
        feat.append(np.load(file_lists[j][i])) #Load i-th feature for j-th trajectory
    feat_all.append(np.hstack(feat))

print(len(feat_all))


#out of here

   #[270, 287, 283, 275, 275, 282, 282, 284]   
   #[195, 238, 149, 222, 132, 222, 240, 229]
   
#all_coords = np.vstack((n_terminus_coords, c_terminus_coords, helicity, helix_angle, helix_bend, CoM, N_266, Res229_278,
#    Res130_286, D96, D195, A96, D222, A222, D284, B282, Res246_215, Res246_216, 
#    Res246_217, Res246_218, Res246_219, Res246_220, Res246_221)).T
#print(all_coords)
np.save('Metric_Coords_Array_Lig.npy', feat_all)

cluster_kmeans = pyemma.coordinates.cluster_kmeans(feat_all, k=400, stride=5)
print (cluster_kmeans.dtrajs)
np.save('time_series_lig', cluster_kmeans.dtrajs)

#slowest motion = rare events/events traveling a larger kinetic distance/slow processes

#use TICA to get new coordinates
#now we have 16 inputs and 8 outputs
tica = pyemma.coordinates.tica(feat_all, dim=6, lag=1)
tica_output = tica.get_output()
print(tica_output)
tica_feature_TIC_correlation = tica.feature_TIC_correlation
print(tica_feature_TIC_correlation)
#TICS outputs more metrics so can plot pairs of them

np.save('TICA_Data_Lig.npy', tica_output)
np.save('TICA_Feature_Correlation_Lig.npy', tica_feature_TIC_correlation)

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

