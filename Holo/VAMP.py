import matplotlib.pyplot as plt
import numpy as np
import mdshare
import pyemma
import pickle as pkl

score_data = pkl.load(open('score_results_lig.pkl', 'rb'))

def plot_cv_scores(score_results, n_tica=5, cls_per_tica=8):
    plt.figure()
    fig, ax = plt.subplots()
    for i in range(n_tica):
        plot_data = np.zeros((cls_per_tica, 3))
        scores = score_results[i*cls_per_tica:(i+1)*cls_per_tica]
        tica_label = scores[0][0]
        for j in range(len(scores)):
              plot_data[j,0] = scores[j][1]
              plot_data[j,1] = np.mean(np.exp(scores[j][2]))
              plot_data[j,2] = np.std(scores[j][2])*plot_data[j,1]
    #plt.plot(plot_data[:,0], plot_data[:,1])
        plt.errorbar(plot_data[:,0], plot_data[:,1], plot_data[:,2], capsize=2, label="%d TICs"%tica_label)
        plt.xlim(100,500)
        plt.ylim(60,160)
        plt.legend(fancybox=True, frameon=True, edgecolor='k', fontsize=14)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        ax.spines['top'].set_linewidth(2)
        ax.spines['right'].set_linewidth(2)
        plt.xlabel("Number of Clusters")
        plt.ylabel("exp(GMRQ)")
        plt.savefig("cv_scores_hq_lig.png", transparent=True)

if __name__=="__main__": 
    plot_cv_scores(score_data)

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
#pkl.dump(msm.tr

