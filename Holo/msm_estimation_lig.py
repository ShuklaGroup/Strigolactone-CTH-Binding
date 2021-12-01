import matplotlib.pyplot as plt
import numpy as np
import mdshare
import pyemma
import pickle as pkl

time_series = np.load('time_series_lig.npy', allow_pickle=True)
tica_output = np.load('TICA_Data_Lig.npy', allow_pickle=True)
tica_feature_TIC_correlation = np.load('TICA_Feature_Correlation_Lig.npy', allow_pickle=True)
coords = np.load('Metric_Coords_Array_Lig.npy', allow_pickle=True)
coords = coords.tolist()

cluster = pyemma.coordinates.cluster_kmeans(coords, k=400, max_iter=100)
#its = pyemma.msm.its(cluster.dtrajs, lags=[1, 2, 3, 5, 7, 10], nits=3, errors='bayes')
its = pyemma.msm.its(cluster.dtrajs, errors='bayes', lags=800, nits=10)
#we want to see what how fast our processes are
#pyemma.plots.plot_implied_timescales(its, outfile="its_plot_holo.png", units='ns', dt=.07)

msm = pyemma.msm.estimate_markov_model(cluster.dtrajs, lag=214)
print('fraction of states used = {:.2f}'.format(msm.active_state_fraction))
print('fraction of counts used = {:.2f}'.format(msm.active_count_fraction))
#use chapman-kolmogorov test P(k*tau)=P^k*(tau) where P(tau) is transition matrix
#pyemma automatically estimates new msm transition matrix at k*tau and propogates  original by kth power
#use implied timescales plot as heuristic to estimate number of metastables states to test

"""
cktest = msm.cktest(2)
morefun, axes = pyemma.plots.plot_cktest(cktest)
morefun.savefig('msm-chapman-kolmogorov-holo.png', dpi=300)

#error stuff
bayesian_msm = pyemma.msm.bayesian_markov_model(cluster.dtrajs, lag=214, conf=0.95)
sample_mean = bayesian_msm.sample_mean('timescales', k=1)
sample_conf_l, sample_conf_r = bayesian_msm.sample_conf('timescales', k=1)

print('Mean of first ITS: {:f}'.format(sample_mean[0]))
print('Confidence interval: [{:f}, {:f}]'.format(sample_conf_l[0], sample_conf_r[0]))
print('fraction of states used = {:f}'.format(msm.active_state_fraction))
print('fraction of counts used = {:f}'.format(msm.active_count_fraction))
"""

#use pickle to save the regular msm, also the msm weights
pkl.dump(msm, open('msm-model2.pkl', 'wb'))
pkl.dump(msm.trajectory_weights(), open('msm-traj-weights2.pkl', 'wb'))

