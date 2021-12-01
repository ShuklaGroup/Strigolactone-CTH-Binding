import pickle as pkl
import mdtraj as md
import glob
import argparse



def get_args():

    parser = argparse.ArgumentParser() 
    parser.add_argument("--pickle_data", type=str, help="What file do you want, aho?")
    parser.add_argument("--savename", type=str, help="Name the file, baka")

    args = parser.parse_args()
    
    return args

if __name__=="__main__":

    args = get_args()
    
    pickle_in = open(args.pickle_data, "rb")
    le_file = pkl.load(pickle_in)
    print(len(le_file))

    print(le_file[0])
    print(le_file[0][0])

    targettopfile = "stripped.6BRT_with_GR24.prmtop"
    first = le_file[0][1]
    if le_file[0][2] == 1:
        traj_file = "lig_stripped/6BRT_apo_helix_GR24_initial_run.strip.dcd"
        old_frame = md.load_frame(traj_file, le_file[0][0], top=targettopfile)
        print(le_file[0])
        print(old_frame)
    else:
        roundno = le_file[0][2]
        traj_file = "lig_stripped/6BRT_apo_helix_GR24_round{0}_{1}.strip.dcd".format(roundno, first)
        old_frame = md.load_frame(traj_file, le_file[0][0], top=targettopfile)
        print(le_file[0])
        print(old_frame)

    for i in range(1, len(le_file)):    
        if le_file[i][2] == 1:
            q = le_file[i][1]
            traj_file = "lig_stripped/6BRT_apo_helix_GR24_initial_run.strip.dcd"
            newest_frame = md.load_frame(traj_file, le_file[i][0], top=targettopfile)
            if newest_frame.unitcell_volumes == None:
                continue
            else:
                all_frames = newest_frame.join(old_frame)
                print(le_file[i])
                print(all_frames)
                old_frame = all_frames
        else:
            q = le_file[i][1]
            roundno = le_file[i][2]
            traj_file = "lig_stripped/6BRT_apo_helix_GR24_round{0}_{1}.strip.dcd".format(roundno, q)
            newest_frame = md.load_frame(traj_file, le_file[i][0], top=targettopfile)
            if newest_frame.unitcell_volumes == None:
                continue
            else:
                all_frames = newest_frame.join(old_frame)
                print(le_file[i])
                print(all_frames)
                old_frame = all_frames
        
    all_frames.save_xtc(args.savename)

#save all frames to xtc , can open in VMD or Gromacs
#can do individual xtc frames (or PDB) or save all as one object in xtc
#use stripped trajectories instead bc easier
#good to look at a few different regions, minima and rare events
