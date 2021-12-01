import pickle as pkl
import mdtraj as md
import glob

#pickle_in = open("Frames_to_Load.pickle", "rb")
#le_file = pkl.load(pickle_in)
#print(len(le_file))

targettopfile = "stripped.protein_helix_nohydrogen.prmtop"
#first = le_file[0][1]
#traj_file = "stripped/6BRT_apo_helix_inactive_round2_{0}.strip.dcd".format(first)
#old_frame = md.load_frame(traj_file, le_file[0][0], top=targettopfile)
#print(le_file[0])
#print(old_frame)

#for i in range(0, len(le_file)):    
 #   q = le_file[i][1]
 #   r = le_file[i][0]
traj_file = "stripped/6BRT_apo_helix_inactive_initial_run.strip.dcd"
newest_frame = md.load_frame(traj_file, 100, top=targettopfile)
newest_frame.save_pdb('hopefully_not_broken_6BRT_PDB.pdb')
#    newest_frame.save_pdb("PDB_Files/Analysis_Group3/Round2_Run{0}_Frame{1}.pdb".format(q, r))
#    print(le_file[i])
#    print(newest_frame)
    
        


#save all frames to xtc , can open in VMD or Gromacs
#can do individual xtc frames (or PDB) or save all as one object in xtc
#use stripped trajectories instead bc easier
#good to look at a few different regions, minima and rare events
