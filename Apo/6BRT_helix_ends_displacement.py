import glob
import numpy as np
import mdtraj as md

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.protein_helix_nohydrogen.prmtop"

for file in glob.glob('./stripped/*.strip.xtc'):
    t = md.load(file, top=targettopfile)
    d = md.compute_displacements(t,[[4131,4404]])     	# distance between the two atoms on helix terminal caps
    n_frames = t.n_frames
    print(np.shape(d))

    dis = np.empty([n_frames, 3])

    for i in range(n_frames):
        for j in range(3):
            dis[i,j]=d[i][0][j]

    np.save('./analysis/Orientation/'+file.split('/')[-1]+'whole_helix_orientation.npy',dis)
