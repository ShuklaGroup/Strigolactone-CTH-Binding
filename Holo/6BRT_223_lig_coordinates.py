import glob
import numpy as np
import mdtraj as md

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.6BRT_with_GR24.prmtop"

for file in glob.glob('./lig_stripped/*.strip.dcd'):
    q = md.load(file, top=targettopfile)
    p = q.make_molecules_whole(inplace=True)
    #top = md.load(file, top=targettopfile).topology
    r = [3408]
    t = p.atom_slice(r)
    print(t)
    d = t.xyz  
    n_frames = t.n_frames
    print(np.shape(d))

    dis = np.empty([n_frames, 3])

    for i in range(n_frames):
        for j in range(3):
            dis[i,j]=d[i][0][j]

    np.save('./lig_analysis/Mass/'+file.split('/')[-1]+'_223_coordinates.npy',dis)
