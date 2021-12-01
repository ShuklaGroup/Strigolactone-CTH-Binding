import numpy as np
import mdtraj as md
import pyemma
import pickle
import glob
from natsort import natsorted

def get_samples(msm_obj, topfile, n=100):
    """Draw samples from each MSM state"""
    samples = msm_obj.sample_by_state(n)
    trajs = natsorted(glob.glob("lig_stripped/*"))
    #Save xtc files
    for i in range(len(samples)):
        state_samples = samples[i]
        state_traj = []
        for j in range(len(state_samples)):
            state_traj.append(md.load_frame(trajs[state_samples[j,0]], state_samples[j,1], top=topfile))
        md.join(state_traj).save_xtc("state_%d.xtc"%i)
    return samples
    

def id_associated_dissociated_states(samples):  #ask jiming how this one works
    """Identify ligand bound, unbound, and inverse bound states"""
    
    #ALRIGHT BOIZ!!!! For my own specific system, we will categorize states as either D3-D14 associated or dissociated!!! Yay!!!!

    #Ok for N terminus to A223 let's arbitrarily say we have association from 1.2 to 1.8 nm
    #For C terminus to A223 let's say between 0.8 and 2.1 nm

    N_223 = natsorted(glob.glob('lig_analysis/Helices/*n_terminus*'))
    C_229 = natsorted(glob.glob('lig_analysis/Other_Contacts/*c_terminus*229.npy'))
    C_238 = natsorted(glob.glob('lig_analysis/Other_Contacts/*c_terminus*238.npy'))
    R278_223 = natsorted(glob.glob('lig_analysis/Other_Contacts/*223_to_278*'))
 
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
        
        #maybe just do < or >??? Not an in between?
        
        #WE NEED TO TRY NEW FUN CUTOFF DISTANCESSSSSSSSSSS
        #FIX THIS STUFFFFFFFFFFFF
        #if all((np.min(n_a223_dist) > 1.2, np.min(n_a223_dist) < 1.8, np.min(c_238_dist) > 1.1, np.min(c_238_dist) < 1.7, np.min(c_229_dist) > 0.5, np.min(c_229_dist) < 1.2, np.min(r_a223_dist) < 1.1, np.min(r_a223_dist) > .4)):
        #    associated_states.append(i)
        if all((np.min(n_a223_dist) < 1.8, np.min(c_238_dist) < 1.7, np.min(c_229_dist) < 1.2, np.min(r_a223_dist) < 1.1)):
            associated_states.append(i)
        #elif ((np.min(n_a223_dist) < 1.0 or np.min(n_a223_dist) > 2.0) and (np.min(c_238_dist) < 0.9 or np.min(c_238_dist) > 1.9) and (np.min(c_229_dist) < 0.3 or np.min(c_229_dist) > 1.3) and (np.min(r_a223_dist) < .2 or np.min(r_a223_dist) > 1.2)):
        #    dissociated_states.append(i)
        elif all((np.min(n_a223_dist) > 2.0, np.min(c_238_dist) > 1.9, np.min(c_229_dist) > 1.4, np.min(r_a223_dist) > 1.2)):
            dissociated_states.append(i)
        else:
            intermediate_states.append(i)
            
     #how to get these cutoff points? Choose metrics (ex, helix dissociation)
     #for a check: see if cutoffs group states in a similar way as a metastable assignment
    print('intermediate')
    print(intermediate_states)

    return associated_states, dissociated_states

def id_bound_unbound_states(samples):
    """Identify ligand bound, unbound, and inverse bound states"""

    #use the oxygen ones!!!!!
    ABC_pocket_dist = natsorted(glob.glob("lig_analysis/oxygen/*a_ring*96*")) #Ligand pocket features
    D_ring_pocket_dist = natsorted(glob.glob("lig_analysis/oxygen/*d_ring*96*")) #both of these are good

    bound_states = []
    unbound_states = []
    inverse_bound_states = []

    #FIX UP THESE NUMBERSSSSSSSSSSSSS
    #CHECK THE 3 LOW FREE ENERGY SPOTS IN THE BINDING DIAGRAM

    for i in range(len(samples)):
        state_samples = samples[i]
        abc_dist = []
        d_dist = []
        for j in range(len(state_samples)):
            abc_dist.append(np.load(ABC_pocket_dist[state_samples[j,0]])[state_samples[j,1]])
            d_dist.append(np.load(D_ring_pocket_dist[state_samples[j,0]])[state_samples[j,1]])
        if all((np.min(d_dist) < 0.6, np.mean(abc_dist) > np.mean(d_dist))):
            bound_states.append(i)
        elif np.mean(abc_dist) > 1.5 and np.mean(d_dist) > 1.5:
            unbound_states.append(i)
        elif all((np.min(abc_dist) < 1.5, np.min(d_dist) < 1.5, np.mean(abc_dist) < np.mean(d_dist))):
            inverse_bound_states.append(i)

        inverse_bound_states, _, _ = trim_state_sets(inverse_bound_states, bound_states)

    return bound_states, unbound_states, inverse_bound_states

def id_anchored_states(samples):
    """Identify states where ligand is anchored to lid helices"""

    A_ring_T1_dist_top = natsorted(glob.glob("./lig_analysis/THelices/*ABC*T1*top*")) #did this
    A_ring_T2_dist_top = natsorted(glob.glob("./lig_analysis/THelices/*ABC*T2*top*")) #did this
    D_ring_T1_dist_bot = natsorted(glob.glob("./lig_analysis/THelices/*D-ring*T1*bot*")) #did this
    D_ring_T2_dist_bot = natsorted(glob.glob("./lig_analysis/THelices/*D-ring*T2*bot*")) #did this

    anchored_states = []

    #CHECK THESE NUMBERS

    for i in range(len(samples)):
        state_samples = samples[i]
        abc_t1_top = []
        abc_t2_top = []
        d_t1_bot = []
        d_t2_bot = []
        for j in range(len(state_samples)):
            abc_t1_top.append(np.load(A_ring_T1_dist_top[state_samples[j,0]])[state_samples[j,1]])
            abc_t2_top.append(np.load(A_ring_T2_dist_top[state_samples[j,0]])[state_samples[j,1]])
            d_t1_bot.append(np.load(D_ring_T2_dist_bot[state_samples[j,0]])[state_samples[j,1]])
            d_t2_bot.append(np.load(D_ring_T2_dist_bot[state_samples[j,0]])[state_samples[j,1]])
        #print(i)
        #print(np.mean(abc_t1_top))
        #print(np.mean(abc_t2_top))
        #print(np.mean(d_t1_bot))
        #print(np.mean(d_t2_bot))

        if all((np.min(abc_t1_top) < 0.9, np.min(abc_t2_top) < 0.9, np.min(d_t1_bot) < 1.0, np.min(d_t2_bot) < 1.0)):
            anchored_states.append(i)
    
    return anchored_states

def id_lig_helix_association(samples):
#resid 282 shows super high contact probability with GR24!!!
#Also try resid 278
    B282 = natsorted(glob.glob('./lig_analysis/Ligand3/*b_ring*282*'))
    B278 = natsorted(glob.glob('./lig_analysis/Ligand3/*b_ring*278*'))
    lig_helix_associated = []
    
    for i in range(len(samples)):
        state_samples = samples[i]
        #MAY NEED TO PLAY AROUND WITH THESE
        
        b_282_dist = []
        b_278_dist = []
 
        for j in range(len(state_samples)):
            b_282_dist.append(np.load(B282[state_samples[j,0]])[state_samples[j,1]])
            b_278_dist.append(np.load(B282[state_samples[j,0]])[state_samples[j,1]])
            
        if all((np.min(b_282_dist) < 0.9, np.min(b_278_dist) < 0.9)):
            lig_helix_associated.append(i)
            

    return lig_helix_associated


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

def trim_state_sets(setA, setB):
    """Remove overlapping states between two sets of states"""

    overlap = np.intersect1d(setA, setB)
    setA_trimmed = [i for i in setA if i not in overlap]  #removes overlapping points from set A
    setB_trimmed = [i for i in setB if i not in overlap]  #removes overlapping points from set B

    return setA_trimmed, setB_trimmed, overlap

def helix_position(ligA, ligB, ligC, ligD, ligE, helixA, helixD):

    ligand_sets = (ligA, ligB, ligC, ligD, ligE)
    ligand_labels = ['Productive_Binding', 'Unproductive_Binding', 'Anchored', 'Dissociated', 'Lig_Helix_Associated']
    helix_sets = (helixA, helixD)
    helix_labels = ['Helix_D14_Associated', 'Helix_D14_Dissociated']
    ten_sets = []
    for helixset in helix_sets:
        for oneset in ligand_sets:
            overlap = np.intersect1d(oneset, helixset)
            ten_sets.append(overlap)
            print("Helix set")
            print(helixset)
            print("Ligand set")
            print(oneset)
            print("Overlap")
            print(overlap)
            
    return ten_sets 

if __name__=="__main__":

    msm = pickle.load(open("msm-model.pkl",'rb'))
    #samples = get_samples(msm, topfile='stripped.6BRT_with_GR24.prmtop')
    #pickle.dump(samples, open("state_samples_holo.pkl",'wb'))
    samples = pickle.load(open("state_samples_holo.pkl",'rb')) 
    associated, dissociated = id_associated_dissociated_states(samples)   #see function above
    bound, unbound, inverse = id_bound_unbound_states(samples)
    anchored = id_anchored_states(samples)
    lig_helix_associated = id_lig_helix_association(samples)

    print("State assignments")
    print("Helix Associated")
    print(associated)
    print("Helix Dissociated")
    print(dissociated)
    print("Bound")
    print(bound)
    print("Unbound")
    print(unbound)
    print("Inverse Bound")
    print(inverse)
    print("Anchored")
    print(anchored)
    print("Ligand Helix Associated")
    print(lig_helix_associated)

    ##Trimmed states
    anchored_trimmed, bound_trimmed, overlap = trim_state_sets(anchored, bound)
    print("ANCHORED TRIMMED")
    print(anchored_trimmed)
    print("BOUND TRIMMED")
    print(bound_trimmed)
    print("PARTIAL BOUND")
    print(overlap)
 
    unproductive_bound, _, _ = trim_state_sets(inverse, bound)
    print("UNPRODUCTIVE BINDING")
    print(unproductive_bound)

    unbound_trimmed, _, _ = trim_state_sets(unbound, anchored_trimmed)
    print("UNBOUND AND NOT ANCHORED")
    print(unbound_trimmed)
    
    helix_associated, _, _ = trim_state_sets(lig_helix_associated, unbound_trimmed)
    print("Helix associated and unbound")
    print(helix_associated)

    all10sets = helix_position(bound_trimmed, unproductive_bound, anchored_trimmed, unbound_trimmed, helix_associated, associated, dissociated)

    productive_binding_associated = all10sets[0] #none
    unproductive_binding_associated = all10sets[1]  #few
    anchored_associated = all10sets[2] #none
    dissociated_associated = all10sets[3] #several
    lig_helix_associated_associated = all10sets[4] #one
    productive_binding_dissociated = all10sets[5] #none
    unproductive_binding_dissociated = all10sets[6] #few
    anchored_dissociated = all10sets[7]  #few
    dissociated_dissociated = all10sets[8]  #many
    lig_helix_associated_dissociated = all10sets[9] #one

    pcca_object = msm.pcca(10)
    print(msm.metastable_assignments)

    for state in range(10):
        print(state)
        microstates = [i for i, x in enumerate(msm.metastable_assignments) if x == state] #what even is this help
                #print which microstates are in each macrostate ig?
        print(microstates)
    
    #the previous 2 sections compare metastable assignments with PCCA to see if they're in agreements
    
    for j, eachoneset in enumerate(all10sets):
        print("This is state {0}".format(j))
        for i in eachoneset:
            print(msm.metastable_assignments[i])

    #print(associated)
    #for i in associated:
    #    print(msm.metastable_assignments[i])
    #print(dissociated)
    #for i in dissociated:
    #    print(msm.metastable_assignments[i])
        
        #shows which states we're calling active vs inactive. Ask Jiming about the particulars
        #which clusters got categorized as which macrostates
        #if these two agree well, we may have a good set of macrostates.

    print("State assignments")
    print("UNBOUND")
    print(unbound)
    print("BOUND")
    print(bound)
    print("INVERSE")
    print(inverse)
    print("ANCHORED")
    print(anchored)
    print("Dissociated Dissociated")
    print(dissociated_dissociated)
    print("Productive binding associated")
    print(productive_binding_associated)   
 
    print("Productive binding helix associated")
    tpt2, mfpt2, int2, path2 = calc_tpt(msm, dissociated_dissociated, productive_binding_associated)
    pickle.dump(tpt2, open("tpt_productive_binding_associated.pkl",'wb'))
    print("MFPT:")
    print(mfpt2)
    print(tpt2.rate)

    paths, fluxes = tpt2.pathways(fraction=1.0, maxiter=100000)
    print("Total binding flux (associated)")
    print(np.sum(fluxes))
    
    sets, tpt_cg = tpt2.coarse_grain([productive_binding_associated, unproductive_binding_associated, anchored_associated, dissociated_associated, lig_helix_associated_associated, 
        productive_binding_dissociated, unproductive_binding_dissociated, anchored_dissociated, dissociated_dissociated, lig_helix_associated_dissociated])
    
    for s in sets:
        print(s)

    flux = tpt_cg.flux
    print(flux)

    print(10*flux/(np.max(flux)))

    print("Equilibrium probabilities:")
    print(np.sum(msm.pi[productive_binding_associated]))
    print(np.sum(msm.pi[unproductive_binding_associated]))
    print(np.sum(msm.pi[anchored_associated]))
    print(np.sum(msm.pi[dissociated_associated]))
    print(np.sum(msm.pi[lig_helix_associated_associated]))
    print(np.sum(msm.pi[productive_binding_dissociated]))
    print(np.sum(msm.pi[unproductive_binding_dissociated]))
    print(np.sum(msm.pi[anchored_dissociated]))
    print(np.sum(msm.pi[dissociated_dissociated]))
    print(np.sum(msm.pi[lig_helix_associated_dissociated]))
    