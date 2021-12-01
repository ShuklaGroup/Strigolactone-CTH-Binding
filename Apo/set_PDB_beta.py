import numpy as np
import pickle
import argparse

def write_file(old_pdb, new_pdb, beta_vals):

    original_file = open(old_pdb, 'r')
    new_file = open(new_pdb,'w')
    for line in original_file:
        if line.split()[0] == "ATOM":
            resid = int(line.split()[5]) #ASSUMES 6TH COLUMN IS RESID
            #resid = int(line.split()[4]) #ASSUMES 5TH COLUMN IS RESID
            if resid < 268:
                new_file.write(line.replace("1.00  0.00","1.00  %.4f"%beta_vals[resid-1]))
            else:
                new_file.write(line)
        else:
            new_file.write(line)

def get_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--old_pdb", type=str, help="original PDB file")
    parser.add_argument("--new_pdb", type=str, help="new PDB file")
    parser.add_argument("--vals_file", type=str, help="File containing values")
    args = parser.parse_args()

    return args

if __name__=="__main__":

    args = get_args()
    #Load numbers:
    if args.vals_file[-3:] == "npy":  #you want to input the probability numpy file
        beta_vals = np.load(args.vals_file)
    elif args.vals_file[-3:] == "pkl":
        beta_vals = pickle.load(open(args.vals_file,'rb'))
    else:
        try:
            beta_vals = np.loadtxt(args.vals_file, usecols=(1,))
        except:
            raise ValueError("Input file type not recognized #disappointmentpanda")

    write_file(args.old_pdb, args.new_pdb, beta_vals)
