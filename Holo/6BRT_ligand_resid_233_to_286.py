import glob
import numpy as np
import mdtraj as md

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.6BRT_with_GR24.prmtop"

for file in glob.glob('lig_stripped/*.strip.dcd'):
    t = md.load(file, top=targettopfile)
    d = md.compute_contacts(t,[[233,286]], scheme='ca')[0]
    	# distance between the two residues on helix T3 and T1 respectively
    n_frames = t.n_frames

    dis = np.empty([n_frames, 1])

    for i in range(n_frames):
      dis[i,0:1]=d[i][0]

    np.save('./lig_analysis/Other_Contacts/'+file.split('/')[-1]+'_resid_233_to_286.npy',dis)
