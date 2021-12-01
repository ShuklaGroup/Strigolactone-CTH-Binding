import glob
import numpy as np
import mdtraj as md

targettopfile="./stripped.4ih4_withlig_noh.prmtop"
#targettopfile="./stripped.ShHTL7_withGR24.prmtop"
#targettopfile="./stripped.AtD14_withMeCLA.prmtop"
#targettopfile="./stripped.AtD14_active_withGR24.prmtop"

for file in glob.glob('./stripped/*.xtc'):
    t = md.load(file, top=targettopfile)
    d = md.compute_distances(t,[[1496,4411]]) #Ligand C4-Ser97 OG (D14)
    #d = md.compute_distances(t,[[1438,4071]]) #Ligand C5-Ser97 OG (D14 with MeCLA)
    #d = md.compute_distances(t,[[1438,4156]]) #Ligand C4-Ser97 OG (ShHTL7)
    n_frames = t.n_frames

    dis = np.empty([n_frames, 1])

    for i in range(n_frames):
      dis[i,0:1]=d[i][0]

    np.save('./analysis/'+file.split('/')[-1]+'_ftr-ABC-pocket-distance.npy',dis)
