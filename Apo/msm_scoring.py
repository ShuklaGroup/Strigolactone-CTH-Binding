import matplotlib.pyplot as plt
import numpy as np
import mdshare
import pyemma
import pickle as pkl

#tica_output = np.load('TICA_Data_16.npy')
coords = np.load('Metric_Coords_Array_v3.npy', allow_pickle=True)
#tica_output = pkl.load(open('TICA_Data_16.pkl', 'rb'))
#print(type(tica_output))
coords = coords.tolist()

def one_run(coords, n_tica_components=10, n_clusters=100):
    tica_object = pyemma.coordinates.tica(data=coords, lag=15, dim=n_tica_components)
    tica_output = tica_object.get_output()
    cluster = pyemma.coordinates.cluster_mini_batch_kmeans(tica_output, k=n_clusters, max_iter=300)
    dtrajs = cluster.assign(tica_output)
    msm = pyemma.msm.estimate_markov_model(dtrajs, 214, dt_traj='70 ps', score_method='VAMP1', score_k=10)
    score = msm.score_cv(dtrajs, score_method='VAMP1', score_k=5)
    return score

def parameter_search(coords, tica_list, clusters_list):
    score_results = []
    for n_tica in tica_list:
        for n_cls in clusters_list:
            score = one_run(coords, n_tica_components=n_tica, n_clusters=n_cls)
            score_results.append((n_tica, n_cls, score))
    return score_results

if __name__=="__main__": 
    num_clust = [100, 150, 200, 250, 300, 350, 400, 450]
    num_tica= [2, 4, 6, 8, 10]
    score_results = parameter_search(coords, num_tica, num_clust)
    pkl.dump(score_results, open('score_results.pkl', 'wb'))


#cluster = pyemma.coordinates.cluster_kmeans(coords, k=50, max_iter=50)
#its = pyemma.msm.its(cluster.dtrajs, errors='bayes', lags=800, nits=10)
#we want to see what how fast our processes are
#pyemma.plots.plot_implied_timescales(its, outfile="its_plot_apo.png", units='ns', dt=.07)

#msm = pyemma.msm.estimate_markov_model(cluster.dtrajs, lag=15)
#print('fraction of states used = {:.2f}'.format(msm.active_state_fraction))
#print('fraction of counts used = {:.2f}'.format(msm.active_count_fraction))
#use chapman-kolmogorov test P(k*tau)=P^k*(tau) where P(tau) is transition matrix
#pyemma automatically estimates new msm transition matrix at k*tau and propogates  original by kth power
#use implied timescales plot as heuristic to estimate number of metastables states to test
#cktest = msm.cktest(2)
#morefun, axes = pyemma.plots.plot_cktest(cktest)
#morefun.savefig('msm-chapman-kolmogorov-apo.png', dpi=300)

#error stuff
#bayesian_msm = pyemma.msm.bayesian_markov_model(cluster.dtrajs, lag=15, conf=0.95)
#sample_mean = bayesian_msm.sample_mean('timescales', k=1)
#sample_conf_l, sample_conf_r = bayesian_msm.sample_conf('timescales', k=1)

#print('Mean of first ITS: {:f}'.format(sample_mean[0]))
#print('Confidence interval: [{:f}, {:f}]'.format(sample_conf_l[0], sample_conf_r[0]))
#print('fraction of states used = {:f}'.format(msm.active_state_fraction))
#print('fraction of counts used = {:f}'.format(msm.active_count_fraction))

#use pickle to save the regular msm, also the msm weights
#pkl.dump(msm, open('msm-model.pkl', 'wb'))
#pkl.dump(msm.trajectory_weights(), open('msm-traj-weights.pkl', 'wb'))



