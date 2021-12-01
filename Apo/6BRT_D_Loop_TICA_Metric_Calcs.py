import glob
import numpy as np
import mdtraj as md

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.protein_helix_nohydrogen.prmtop"

#contact_1 = [270, 286, 283, 275, 275, 282, 282, 284]
contact_2 = [215, 216, 217, 218, 219, 220, 221]

for i in range(7):
    res1 = 246
    res2 = contact_2[i]
    for file in glob.glob('./stripped/*'):
        t = md.load(file, top=targettopfile)
        d = md.compute_contacts(t,[[res1,res2]], scheme='ca')[0]
    	# distance between the two residues on helix T3 and T1 respectively
        n_frames = t.n_frames

        dis = np.empty([n_frames, 1])

        for i in range(n_frames):
            dis[i,0:1]=d[i][0]

        np.save('./analysis/Contacts_for_TICA/'+file.split('/')[-1]+'_resid_{0}_to_{1}.npy'.format(res1, res2),dis)
