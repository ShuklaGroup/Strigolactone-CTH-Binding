import glob
import numpy as np
import mdtraj as md

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.protein_helix_nohydrogen.prmtop"

for file in glob.glob('./stripped/*.strip.xtc'):
    t = md.load(file, top=targettopfile)
    d = md.compute_displacements(t,[[3408,4397]])     	# distance between the two residues on helix T3 and T1 respectively
    n_frames = t.n_frames
    print(np.shape(d))

    dis = np.empty([n_frames, 3])

    for i in range(n_frames):
        for j in range(3):
            dis[i,j]=d[i][0][j]

    np.save('./analysis/Displacement/'+file.split('/')[-1]+'_c_terminus_resid_222_displacement.npy',dis)
