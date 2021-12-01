import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import mdtraj as md
import glob
import pickle
from natsort import natsorted, ns

plt.rc('savefig', dpi=300)
matplotlib.rc('font',family='Helvetica-Normal',size=16)

def compute_contact_distances(traj_list, top, lig_resid): #"lig" resid here is the helix n-terminus (may do c later)
    #Generate lig-protein residue pairs
    contacts_list = []
    #for i in range(lig_resid):
    for i in range(287): #this is the number of all residues in protein NOT helix
        contacts_list.append([i, lig_resid])
    
    dist_all = []
    for traj_file in traj_list:
        traj = md.load(traj_file, top=top)
        dist_all.append(md.compute_contacts(traj, contacts=contacts_list, scheme='closest-heavy', ignore_nonprotein=False)[0])
    
    contact_distances = np.vstack(dist_all)

    return contact_distances

def compute_contact_probs(contact_distances, cutoff=0.45, weights=None):

    #Identify contacts
    contacts = contact_distances.copy() #Copy array
    debugging = np.isnan(contact_distances)
    np.save("debug.npy", debugging)
    print(contacts)
    print(contact_distances)
    print(cutoff)
    contacts[contact_distances > cutoff] = 0.0 #Not in contact
    contacts[contact_distances < cutoff] = 1.0 #In contact

    print(contacts)
    #Compute ligand contact probability by residue
    if weights is None:
        contact_probs = np.sum(contacts, axis=0)/np.shape(contacts)[0]
    else:
        contact_probs = np.matmul(contacts.T, weights)
        #contact_probs = probs/np.sum(probs)

    return contact_probs

#i get to delete a lot here hee hee (well at least for now)

def compute_eq_contact_probs(contact_distances, dtrajs, msm, cutoff=0.45):

    contacts = contact_distances.copy()
    contacts[contact_distances > cutoff] = 0.0 #Not in contact
    contacts[contact_distances < cutoff] = 1.0 #In contact#

    eq_dist = msm.pi
    dtrajs = np.hstack(dtrajs)

    contact_prob_per_state = np.zeros((np.shape(contacts)[1], np.shape(eq_dist)[0]))

    print(np.shape(contact_prob_per_state))

    for i in range(np.shape(contacts)[0]): #Count per-residue in each MSM state
        contact_prob_per_state[:,dtrajs[i]] += contacts[i,:].T

    for i in range(np.shape(eq_dist)[0]): #Normalize by MSM state count
        contact_prob_per_state[:,i] /= len(dtrajs[dtrajs==i])

    eq_contact_probs = np.matmul(contact_prob_per_state, eq_dist)

    return eq_contact_probs

def plot_contact_probs(contact_probs):

    plt.plot(contact_probs)
    plt.xlabel("Residue")
    yticks = [0.000, 0.06, 0.12, 0.18]
    #xlabels = ['0.000', '0.025', '0.050', '0.075', '0.100', '0.125', '0.150', '0.175']
    plt.yticks(yticks)
    #plt.set_xticklabels(xlabels)
    plt.ylabel("Contact Probability")
    plt.gca().set_aspect(aspect=(300/(.175*3)))
    plt.tight_layout()
    plt.savefig("contact_prob_lig_msm.png")

if __name__=="__main__":

    #contact_distances = compute_contact_distances(natsorted(glob.glob("../stripped/*")), "../stripped.ShHTL7_withGR24.prmtop", 269)
    
    contact_distances = compute_contact_distances(natsorted(glob.glob("./lig_stripped/*dcd")), "stripped.6BRT_with_GR24.prmtop", 288)
    np.save("6BRT_contact_distances_sorted.npy", contact_distances)

    contact_distances = np.load("6BRT_contact_distances_sorted.npy")
    msm_weights = pickle.load(open("./msm-traj-weights2.pkl",'rb'))
    contact_probs = compute_contact_probs(contact_distances)
    contact_probs = compute_contact_probs(contact_distances, weights=None, cutoff=0.4)

    #np.save("6BRT_contact_probs_weighted_4Acutoff.npy", contact_probs)

    #yeah nope
    msm = pickle.load(open("./msm-model2.pkl",'rb'))
    dtrajs = np.load("./time_series_lig.npy", allow_pickle=True)
    #dtrajs = [i for i in dtrajs]    

    #no msms here wwwww
    eq_contact_probs = compute_eq_contact_probs(contact_distances, dtrajs, msm, cutoff=0.4)
    np.save("eq_contact_probs_final.npy", eq_contact_probs)
    
    eq_contact_probs = np.load('eq_contact_probs_final.npy', allow_pickle=True)
    #contact_probs = np.load("6BRT_contact_probs_weighted_4Acutoff.npy")
    plot_contact_probs(eq_contact_probs)
