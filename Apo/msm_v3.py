import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg") 
import numpy as np
#import mdshare
import pyemma
import glob
import argparse
from natsort import natsorted, ns
import pickle as pkl


"""
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
   
Res270_195 = []
Res270_195_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*270*195*'))
for datafile in Res270_195_group:
    Res270_195.extend(np.load(datafile))
Res270_195 = np.array(Res270_195)
if len(np.shape(Res270_195)) > 1:
   Res270_195 = Res270_195[:,0] 
   
Res286_238 = []
Res286_238_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*286*238*'))
for datafile in Res286_238_group:
    Res286_238.extend(np.load(datafile))
Res286_238 = np.array(Res286_238)
if len(np.shape(Res286_238)) > 1:
   Res286_238 = Res286_238[:,0] 
   
Res283_149 = []
Res283_149_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*283*149*'))
for datafile in Res283_149_group:
    Res283_149.extend(np.load(datafile))
Res283_149 = np.array(Res283_149)
if len(np.shape(Res283_149)) > 1:
   Res283_149 = Res283_149[:,0] 
 
Res275_222 = []
Res275_222_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*275*222*'))
for datafile in Res275_222_group:
    Res275_222.extend(np.load(datafile))
Res275_222 = np.array(Res275_222)
if len(np.shape(Res275_222)) > 1:
   Res275_222 = Res275_222[:,0] 

Res275_132 = []
Res275_132_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*275*132*'))
for datafile in Res275_132_group:
    Res275_132.extend(np.load(datafile))
Res275_132 = np.array(Res275_132)
if len(np.shape(Res275_132)) > 1:
   Res275_132 = Res275_132[:,0] 

Res282_222 = []
Res282_222_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*282*222*'))
for datafile in Res282_222_group:
    Res282_222.extend(np.load(datafile))
Res282_222 = np.array(Res282_222)
if len(np.shape(Res282_222)) > 1:
   Res282_222 = Res282_222[:,0] 

Res282_240 = []
Res282_240_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*282*240*'))
for datafile in Res282_240_group:
    Res282_240.extend(np.load(datafile))
Res282_240 = np.array(Res282_240)
if len(np.shape(Res282_240)) > 1:
   Res282_240 = Res282_240[:,0] 

Res284_229 = []
Res284_229_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*284*229*'))
for datafile in Res284_229_group:
    Res284_229.extend(np.load(datafile))
Res284_229 = np.array(Res284_229)
if len(np.shape(Res284_229)) > 1:
   Res284_229 = Res284_229[:,0] 

Res246_215 = []
Res246_215_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*215*'))
for datafile in Res246_215_group:
    Res246_215.extend(np.load(datafile))
Res246_215 = np.array(Res246_215)
if len(np.shape(Res246_215)) > 1:
   Res246_215 = Res246_215[:,0]
   
Res246_216 = []
Res246_216_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*216*'))
for datafile in Res246_216_group:
    Res246_216.extend(np.load(datafile))
Res246_216 = np.array(Res246_216)
if len(np.shape(Res246_216)) > 1:
   Res246_216 = Res246_216[:,0]
   
Res246_217 = []
Res246_217_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*217*'))
for datafile in Res246_217_group:
    Res246_217.extend(np.load(datafile))
Res246_217 = np.array(Res246_217)
if len(np.shape(Res246_217)) > 1:
   Res246_217 = Res246_217[:,0]

Res246_218 = []
Res246_218_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*218*'))
for datafile in Res246_218_group:
    Res246_218.extend(np.load(datafile))
Res246_218 = np.array(Res246_218)
if len(np.shape(Res246_218)) > 1:
   Res246_218 = Res246_218[:,0]
   
Res246_219 = []
Res246_219_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*219*'))
for datafile in Res246_219_group:
    Res246_219.extend(np.load(datafile))
Res246_219 = np.array(Res246_219)
if len(np.shape(Res246_219)) > 1:
   Res246_219 = Res246_219[:,0]
   
Res246_220 = []
Res246_220_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*220*'))
for datafile in Res246_220_group:
    Res246_220.extend(np.load(datafile))
Res246_220 = np.array(Res246_220)
if len(np.shape(Res246_220)) > 1:
   Res246_220 = Res246_220[:,0]

Res246_221 = []
Res246_221_group = natsorted(glob.glob('./analysis/Contacts_for_TICA/*246*221*'))
for datafile in Res246_221_group:
    Res246_221.extend(np.load(datafile))
Res246_221 = np.array(Res246_221)
if len(np.shape(Res246_221)) > 1:
   Res246_221 = Res246_221[:,0]

"""

#jiming code starts here

feat_identifiers = []

#broken up for readability
feat_identifiers.extend(['./analysis/Helices/*n_terminus*', './analysis/Helices/*c_terminus*', './analysis/Helical/*alpha*', './analysis/Helices/*between*', './analysis/Other_Contacts/*n_terminus*']) 
feat_identifiers.extend(['./analysis/Other_Contacts/*229*278*', './analysis/Contacts_for_TICA/*270*195*', './analysis/Contacts_for_TICA/*286*238*', './analysis/Contacts_for_TICA/*283*149*', './analysis/Contacts_for_TICA/*275*222*']) 
feat_identifiers.extend(['./analysis/Contacts_for_TICA/*275*132*', './analysis/Contacts_for_TICA/*282*222*', './analysis/Contacts_for_TICA/*282*240*', './analysis/Contacts_for_TICA/*284*229*']) 
feat_identifiers.extend(['./analysis/Contacts_for_TICA/*246*215*', './analysis/Contacts_for_TICA/*246*216*', './analysis/Contacts_for_TICA/*246*217*', './analysis/Contacts_for_TICA/*246*218*']) 
feat_identifiers.extend(['./analysis/Contacts_for_TICA/*246*219*', './analysis/Contacts_for_TICA/*246*220*', './analysis/Contacts_for_TICA/*246*221*']) 

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

#all_coords = np.vstack((n_terminus_coords, c_terminus_coords, helicity, helix_angle, helix_bend, CoM, N_266, Res229_278,
#    Res270_195, Res286_238, Res283_149, Res275_222, Res275_132, Res282_222, Res282_240, Res284_229, Res246_215, Res246_216, 
#    Res246_217, Res246_218, Res246_219, Res246_220, Res246_221)).T
#print(all_coords)
np.save('Metric_Coords_Array_v3_10.npy', feat_all)

cluster_kmeans = pyemma.coordinates.cluster_kmeans(feat_all, k=300, stride=5)
print (cluster_kmeans.dtrajs)
np.save('time_series_10', cluster_kmeans.dtrajs)

#slowest motion = rare ievents/events traveling a larger kinetic distance/slow processes

#use TICA to get new coordinates
#now we have 16 inputs and 8 outputs
tica = pyemma.coordinates.tica(feat_all, dim=10, lag=1)
tica_output = tica.get_output()
print(tica_output)
tica_feature_TIC_correlation = tica.feature_TIC_correlation
print(tica_feature_TIC_correlation)
#TICS outputs more metrics so can plot pairs of them

np.save('TICA_Data_v3_10.npy', tica_output)
np.save('TICA_Feature_Correlation_v3_10.npy', tica_feature_TIC_correlation)
pkl.dump(tica_output, open('TICA_Data_v3_10.pkl', 'wb'))

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

