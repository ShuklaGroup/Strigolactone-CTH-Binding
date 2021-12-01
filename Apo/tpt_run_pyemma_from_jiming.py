import numpy as np
import mdtraj as md
import pyemma
import pickle
import glob
from natsort import natsorted

def get_samples(msm_obj, topfile, n=100):
    """Draw samples from each MSM state"""
    samples = msm_obj.sample_by_state(n)
    trajs = natsorted(glob.glob("stripped/*"))
    #Save xtc files
    for i in range(len(samples)):
        state_samples = samples[i]
        state_traj = []
        for j in range(len(state_samples)):
            state_traj.append(md.load_frame(trajs[state_samples[j,0]], state_samples[j,1], top=topfile))
        md.join(state_traj).save_xtc("state_%d.xtc"%i)
    return samples
    
   
    """
    for i in range(len(samples)):
        state_samples = samples[i] #gets all samples from one state
        print(state_samples)
        state_traj = []
        for j in range(len(state_samples)):
            group = entry[j]
            #print(group)
            Frame = group[2]
            Run = group[1]
            Round = group[0]
            i#print(Round, Run, Frame)
            if Round == 1:
                traj_file = "stripped/6BRT_apo_helix_inactive_initial_run.strip.xtc"
            else:
                traj_file = "stripped/6BRT_apo_helix_inactive_round{0}_{1}.strip.xtc".format(Round, Run)
            state_traj.append(md.load_frame(traj_file, Frame, top=topfile))
            print(state_traj)           
    """
            #state_traj.append(md.load_frame(trajs[state_samples[j,0]], state_samples[j,1], top=topfile)) #add the frame we want to the trajectory xtc object
        #selects the proper trajectory, the frame index, and the topology file

def id_associated_dissociated_states(samples):  #ask jiming how this one works
    """Identify ligand bound, unbound, and inverse bound states"""
    
    #ALRIGHT BOIZ!!!! For my own specific system, we will categorize states as either D3-D14 associated or dissociated!!! Yay!!!!

    #Ok for N terminus to A223 let's arbitrarily say we have association from 1.2 to 1.8 nm
    #For C terminus to A223 let's say between 0.8 and 2.1 nm

    N_223 = natsorted(glob.glob('analysis/Helices/*n_terminus*'))
    C_229 = natsorted(glob.glob('analysis/Other_Contacts/*c_terminus*229.npy'))
    C_238 = natsorted(glob.glob('analysis/Other_Contacts/*c_terminus*238.npy'))
    R278_223 = natsorted(glob.glob('analysis/Other_Contacts/*222_to_278*'))
 
    #T1_T3_dist = sorted(glob.glob("../analysis/*T1-T3-distance-1*")) #Ligand pocket features
    #Helical_Content = sorted(glob.glob("../analysis/*helical-content-unfolded*")) #Ligand pocket features
    #T1_ext = sorted(glob.glob("../analysis/*T1-T2-hinge-contact-1*")) #Ligand pocket features
    #D_loop = sorted(glob.glob("../analysis/*loop-distance-3*")) #Ligand pocket features
    
    associated_states = []
    dissociated_states = []
    intermediate_states = []
    
    for i in range(len(samples)):
        state_samples = samples[i]
        #FILL IN NEW METRICS HEREEEEEEEEEEE
        
        n_a223_dist = []
        c_229_dist = []
        c_238_dist = []
        r_a223_dist = []
        #helical = []
        #t1_ext = []
        #dloop_dist = []
        for j in range(len(state_samples)):
            n_a223_dist.append(np.load(N_223[state_samples[j,0]])[state_samples[j,1]])
            c_229_dist.append(np.load(C_229[state_samples[j,0]])[state_samples[j,1]])
            c_238_dist.append(np.load(C_238[state_samples[j,0]])[state_samples[j,1]])
            r_a223_dist.append(np.load(R278_223[state_samples[j,0]])[state_samples[j,1]])
            #t1t3_dist.append(np.load(T1_T3_dist[state_samples[j,0]])[state_samples[j,1]])
            #helical.append(np.load(Helical_Content[state_samples[j,0]])[state_samples[j,1]])
            #t1_ext.append(np.load(T1_ext[state_samples[j,0]])[state_samples[j,1]])
            #dloop_dist.append(np.load(D_loop[state_samples[j,0]])[state_samples[j,1]])
        
        #WE NEED TO TRY NEW FUN CUTOFF DISTANCESSSSSSSSSSS
        #FIX THIS STUFFFFFFFFFFFF
        if all((np.mean(n_a223_dist) > 1.2, np.mean(n_a223_dist) < 1.8, np.mean(c_238_dist) > 0.3, np.mean(c_238_dist) < 2.4, np.mean(c_229_dist) > 0.6, np.mean(c_229_dist) < 2.7, np.mean(r_a223_dist) < .7, np.mean(r_a223_dist) > .4)):
        #if all((np.mean(t1t3_dist) < 1.3, np.mean(helical) < 0.6, np.mean(t1_ext) < 0.75, np.mean(dloop_dist) > 1.0)):
            associated_states.append(i)
        elif ((np.mean(n_a223_dist) < 1.0 or np.mean(n_a223_dist) > 2.0) and (np.mean(c_238_dist) < 0.1 or np.mean(c_238_dist) > 2.6) and (np.mean(c_229_dist) < 0.4 or np.mean(c_229_dist) > 2.9) and (np.mean(r_a223_dist) < .2 or np.mean(r_a223_dist) > .9)):
        #elif all((np.mean(t1t3_dist) > 2.0, np.mean(helical) > 0.7, np.mean(t1_ext) > 0.9, np.mean(dloop_dist) < 0.8)):
            dissociated_states.append(i)
        else:
            intermediate_states.append(i)
            
     #how to get these cutoff points? Choose metrics (ex, helix dissociation)
     #for a check: see if cutoffs group states in a similar way as a metastable assignment
    print('intermediate')
    print(intermediate_states)

    return associated_states, dissociated_states

def coarse_grain(msm):

    pcca_object = msm.pcca(10)

    return pcca_object

def calc_tpt(msm, source, sink):

    tpt_object = pyemma.msm.tpt(msm, source, sink) #source is where the transition starts, sink is where it ends
           #in jiming's case we are transitioning from inactive to active form
           #for my case we are transitioning from associated to dissociated (make sure to reverse which is which!)
    mfpt = tpt_object.mfpt
    intermediates = tpt_object.I
    pathways = tpt_object.pathways

    return tpt_object, mfpt, intermediates, pathways


#We don't care about this function for 6BRT!!!!
def pathway_fluxes(pathways, capacities, anchored):

    sticky_paths = []
    direct_paths = []
    sticky_flux = []
    direct_flux = []

    for i in range(len(pathways)):
        if any(j in anchored for j in pathways[i]): #"in" operator returns a boolean if the element is present
                  #"any" operator returns statements that are true, nonzero, etc
                  #so if a value in pathways[i] is also in anchored an dthat value is nonzero, add its pathway and capacity
                  #pathways gives the path and capacities gives the flux
            sticky_paths.append(pathways[i])
            sticky_flux.append(capacities[i])
        else:
            direct_paths.append(pathways[i])
            direct_flux.append(capacities[i])
    
    return sticky_paths, direct_paths, sticky_flux, direct_flux

if __name__=="__main__":

    msm = pickle.load(open("msm-model-10.pkl",'rb'))
    #samples = get_samples(msm, topfile="../stripped.4ih4_withlig_noh.prmtop")    #see function above
    samples = get_samples(msm, topfile='stripped.protein_helix_nohydrogen.prmtop')
    #samples = get_samples(msm, topfile="../stripped.4ih4_modelled_active.prmtop")
    #samples = get_samples(msm, topfile="../stripped.ShHTL7_apo_inactive.prmtop")
    pickle.dump(samples, open("state_samples_apo-10.pkl",'wb'))
    samples = pickle.load(open("state_samples_apo-10.pkl",'rb')) 
    associated, dissociated = id_associated_dissociated_states(samples)   #see function above

    print("State assignments")
    print(associated)
    print(dissociated)

    pcca_object = msm.pcca(10)
    print(msm.metastable_assignments)

    for state in range(10):
        print(state)
        microstates = [i for i, x in enumerate(msm.metastable_assignments) if x == state] #what even is this help
                #print which microstates are in each macrostate ig?
        print(microstates)
    
    #the previous 2 sections compare metastable assignments with PCCA to see if they're in agreements
    
    print(associated)
    for i in associated:
        print(msm.metastable_assignments[i])
    print(dissociated)
    for i in dissociated:
        print(msm.metastable_assignments[i])
        
        #shows which states we're calling active vs inactive. Ask Jiming about the particulars
        #which clusters got categorized as which macrostates
        #if these two agree well, we may have a good set of macrostates.

    print("Association vs Dissociation")
    tpt1, mfpt1, int1, path1 = calc_tpt(msm, associated, dissociated) #inactive is source, active is sink
            #well now associated is source, dissociated is sink
    pickle.dump(tpt1, open("tpt_bound-10.pkl",'wb'))
    print("MFPT:")
    print(mfpt1)
    print(int1)
    print(path1)

    paths, fluxes = tpt1.pathways(fraction=1.0, maxiter=100000)
    print("Total binding flux")
    print(np.sum(fluxes))
    
    #EVERYTHING BELOW HERE ISN'T IMPORTANT TO ME
    
    #sticky_paths, direct_paths, sticky_flux, direct_flux = pathway_fluxes(paths, fluxes, anchored)
    #sticky_frac = np.sum(sticky_flux)/(np.sum(sticky_flux) + np.sum(direct_flux))

    #loop_paths, direct_paths, loop_flux, direct_flux = pathway_fluxes(paths, fluxes, loop_anchored)
    #loop_frac = np.sum(loop_flux)/(np.sum(loop_flux) + np.sum(direct_flux))
    #print("T1/T2 anchoring fraction")
    #print(sticky_frac)
    #print("Loop anchoring fraction")
    #print(loop_frac)

    #print("Inverse binding")
    #tpt2, mfpt2, int2, path2 = calc_tpt(msm, unbound, inverse)
    #pickle.dump(tpt2, open("tpt_inverse_bound.pkl",'wb'))
    #print("MFPT:")
    #print(mfpt2)
    #print(int2)
    #print(path2)

    #tpt2, mfpt2, int2, path2 = calc_tpt(msm, unbound, inverse)
    #paths, fluxes = tpt2.pathways(fraction=1.0, maxiter=100000)
    #print("Total inverse binding flux")
    #print(np.sum(fluxes))

    #sticky_paths, direct_paths, sticky_flux, direct_flux = pathway_fluxes(paths, fluxes, inverse_anchored)
    #sticky_frac = np.sum(sticky_flux)/(np.sum(sticky_flux) + np.sum(direct_flux))
    #print("Inverse anchoring fraction")
    #print(sticky_frac)

    #print("Bound to inverse bound")
    #tpt3, mfpt3, int3, path3 = calc_tpt(msm, bound, inverse)
    #paths, fluxes = tpt3.pathways(fraction=1.0, maxiter=100000)
    #print("Total bound to inverse flux")
    #print(np.sum(fluxes))

    #print("Equilibrium probabilities:")
    #print(np.sum(msm.pi[unbound]))
    #print(np.sum(msm.pi[bound]))
    #print(np.sum(msm.pi[inverse]))
    #print(np.sum(msm.pi[anchored]))
    #print(np.sum(msm.pi[inverse_anchored]))
    #print(np.sum(msm.pi[loop_anchored]))
