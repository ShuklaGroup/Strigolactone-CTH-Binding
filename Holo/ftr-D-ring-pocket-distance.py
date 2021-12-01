import glob
import numpy as np
import mdtraj as md

#targettopfile="./stripped.4ih4_withlig_noh.prmtop"
#targettopfile="./stripped.ShHTL7_withGR24.prmtop"
#targettopfile="./stripped.AtD14_withMeCLA.prmtop"
#targettopfile="./stripped.AtD14_active_withGR24.prmtop"
targettopfile="./stripped.6BRT_with_GR24.prmtop"

for file in glob.glob('./lig_stripped/*dcd'):
    t = md.load(file, top=targettopfile)
    d = md.compute_distances(t,[[1496,4428]]) #Ligand O4-Ser97 OG (D14)
    #d = md.compute_distances(t,[[1438,4084]]) #Ligand O3-Ser97 OG (D14 with MeCLA)
    #d = md.compute_distances(t,[[1438,4173]]) #Ligand O4-Ser95 OG (KAI2/HTL)
    n_frames = t.n_frames

    dis = np.empty([n_frames, 1])

    for i in range(n_frames):
      dis[i,0:1]=d[i][0]

    np.save('./lig_analysis/oxygen/'+file.split('/')[-1]+'_ftr-D-ring-pocket-distance.npy',dis)
