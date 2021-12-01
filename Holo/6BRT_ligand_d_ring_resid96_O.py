import glob
import numpy as np
import mdtraj as md

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.6BRT_with_GR24.prmtop"

for file in glob.glob('lig_stripped/*.strip.dcd'):
    t = md.load(file, top=targettopfile)
    d = md.compute_distances(t,[[1488,4428]])     	# distance between the two residues on helix T3 and T1 respectively
    n_frames = t.n_frames

    dis = np.empty([n_frames, 1])

    for i in range(n_frames):
      dis[i,0:1]=d[i]

    np.save('./lig_analysis/oxygen/'+file.split('/')[-1]+'_GR24_d_ring_to_resid_96.npy',dis)
