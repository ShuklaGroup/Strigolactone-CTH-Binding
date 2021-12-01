import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg") 
import numpy as np
#import mdshare
import pyemma
import glob
import argparse
from natsort import natsorted, ns


import argparse
#lets you add arguments when you call the program, changes how the program is run
import glob #finds all pathnames associated with a certain pattern
plt.rc('savefig', dpi=500) #dpi is resolution, dots per inch
matplotlib.rc('font',family='Helvetica-Normal',size=24) #controls font size, not too hard

def raw_plot(data1, data2, label1="Label Your Axes!", label2="Label Your Axes!", savename="fep.png"): #this function generates a plot

    plt.figure() #creates a new figure
    plt.hexbin(data1, data2, bins='log', mincnt=1, cmap='jet', vmin=0, vmax=3.0, extent=(0,6,0,1.4), gridsize=300)
    #this plot makes a bunch of hexagons, useful for free energy diagrams
    cbar = plt.colorbar()
    cbar.set_label("Probability Density")
    plt.tick_params(axis='both',labelsize=14)
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.xlim(0,6)
    plt.ylim(0,1.4)
    axes = plt.axes()
    axes.xaxis.set_major_locator(plt.MultipleLocator(1.0))
    plt.grid(linestyle=":")
    plt.savefig(savename)
    #the rest of this stuff is just aesthetics/labels

def get_prob_density(data1, data2, bins=300, binrange=[[0,1],[0,4]], weights=None): #

    if len(np.shape(data1)) > 1: #sees if there is more than one 
        data1 = np.asarray(data1)[:,0]
        data2 = np.asarray(data2)[:,0]

    hist, x_edges, y_edges = np.histogram2d(data1, data2, bins=300, range=binrange, weights=weights)

    prob_density = hist/np.sum(hist)
    x_coords = 0.5*(x_edges[:-1]+x_edges[1:]) 
    y_coords = 0.5*(y_edges[:-1]+y_edges[1:])

    return prob_density.T, x_coords, y_coords

def free_energy(data1, data2, T=300, weights=None, lims=(0,4,0,1), max_energy=6, label1="Label Your Axes!", label2="Label Your Axes!", savename="fe.png"):

    #makes the free energy plot. This function takes the parameters specified in args
    gas_constant = 0.00198588
    prob, x, y = get_prob_density(data1, data2, binrange=[[lims[0],lims[1]],[lims[2],lims[3]]], weights=weights)
    #parameters used are generated in the get_prob_density function seen above
    X, Y = np.meshgrid(x,y) #returns a matrix from the given coordinates
    free_energy = -gas_constant*T*np.log(prob) #calculates the free energy delta G
    free_energy -= np.min(free_energy) #calculates the free energy relative to the minimum 
    
    plt.figure() #make a new figure given the parameters below
    fig, ax = plt.subplots()
    #plt.scatter(X, Y, s=0.25, c=free_energy, vmin=0.0, vmax=6.0, cmap='nipy_spectral', edgecolors=None)
    #plt.scatter(X, Y, s=0.25, c=free_energy, vmin=0.0, vmax=5.0, cmap='jet', edgecolors=None)
    #plt.contour(X, Y, free_energy, np.linspace(0,6,6), colors='black', linewidth=0.01, linestyles='dotted')
    plt.contourf(X, Y, free_energy, np.linspace(0, max_energy, max_energy*5+1), vmin=0.0, vmax=max_energy, cmap='jet')
    cbar = plt.colorbar(ticks=range(max_energy+1))
    cbar.set_label("Free Energy (kcal/mol)",size=24)
    cbar.ax.set_yticklabels(range(max_energy+1))
    cbar.ax.tick_params(labelsize=20)
    plt.tick_params(axis='both',labelsize=14)
    plt.xlabel(label1)
    plt.ylabel(label2)
    #plt.xlim(lims[0],lims[1])
    #plt.ylim(lims[2],lims[3])
    #axes = plt.axes()

    if lims[1] - lims[0] <= 1:
        ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
    elif lims[1] - lims[0] <= 2:
        ax.xaxis.set_major_locator(plt.MultipleLocator(0.5))
    elif lims[1] - lims[0] > 100:
        ax.xaxis.set_major_locator(plt.MultipleLocator(100))
    else:
        ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))

    if lims[3] - lims[2] <= 1:
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
    elif lims[3] - lims[2] <= 2:
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
    elif lims[3] - lims[2] > 100:
        ax.yaxis.set_major_locator(plt.MultipleLocator(100))
    else:
        ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    #this whole thing creates the tick marks and scales them relative to the data points

    #plt.scatter(1.534, 215, marker='*', color='k', s=160.0)
    #plt.scatter(1.534, 215, marker='*', color='w', s=80.0)
    #plt.scatter(1.689, 358, marker='*', color='k', s=160.0)
    #plt.scatter(1.689, 358, marker='*', color='w', s=80.0)
    plt.xlim(lims[0],lims[1])
    plt.ylim(lims[2],lims[3])
    plt.grid(linestyle=":")
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    plt.gca().set_aspect(aspect=(lims[1]-lims[0])/(lims[3]-lims[2]), adjustable='box')
    fig.tight_layout()
    plt.savefig(savename, transparent=True)
    #more stuff for aesthetics

def get_args():

    parser = argparse.ArgumentParser() #these are all the things you can specify when running this program
    #parser.add_argument("--feat_dir", nargs=1, type=str, default="analysis", help="Directory containing featurization files")
    #parser.add_argument("--ax_files", nargs=2, type=str, help="Identifier for files")
    #parser.add_argument("--ax_labels", nargs=2, type=str, help="Axis labels")
    #parser.add_argument("--ax_lims", nargs=4, type=float, help="Axis limits")
    parser.add_argument("--max_energy", nargs=1, default=6, type=int, help="Maximum free energy")
    parser.add_argument("--weights", type=str, help="Pickle file containing MSM weights")
    #parser.add_argument("--savename", type=str, help="Output file name")
    #nargs means multiple command line arguments for a single action

    args = parser.parse_args()
    
    return args

if __name__=="__main__": #'__main__' is the name of the python module. Name is set to the name of the script or module

    args = get_args()

    datastuff = np.load('TICA_Data_v3_10.npy', allow_pickle=True)
    #TICA = datastuff.T
    col1 = []
    col2 = []
    for trajectory in datastuff:
        for frame in trajectory:
            col1.append(frame[0])
            col2.append(frame[2])

    TICA = np.vstack([col1, col2, col1, col1, col1, col1, col1, col1, col1, col1])
    print(len(TICA))

    all_coords = np.load('Coords_for_Features.npy', allow_pickle=True)

    #ax1_files = sorted(glob.glob('analysis/Other_Contacts/*130_to_286*'))
    #ax2_files = sorted(glob.glob('Helix_Bending.npy'))
    #returns a list of path names following the pattern, in alphabetical order

    funtimes = all_coords.T
    print(funtimes)

#    feature_label = ['n_terminus_coords', 'c_terminus_coords', 'helicity', 'helix_angle', 'helix_bend', 'CoM', 'N_266', 'Res229_278',
 #       'Res270_195', 'Res286_238', 'Res283_149', 'Res275_222', 'Res275_132', 'Res282_222', 'Res282_240', 'Res284_229'] 
    ax1_data = funtimes[9]
    thingy = TICA[0]
    pog = len(thingy)
    ax2_data = thingy.reshape(pog)
    free_energy(ax1_data, ax2_data, lims=(0, 6, -1, 3), max_energy=args.max_energy, label1='A223-M276 Distance (nm)', label2='TIC 1', savename='TICA_0_9_nice.png')

    ax1_data = funtimes[16]
    thingy = TICA[1]
    pog = len(thingy)
    ax2_data = thingy.reshape(pog)
    free_energy(ax1_data, ax2_data, lims=(0, 1.5, -4, 4), max_energy=args.max_energy, label1='D218-H247 Distance (nm)', label2='TIC 3', savename='TICA_2_16_nice.png')
                

    #fig = pyemma.plots.plot_feature_histograms(TICA, feature_labels=['0', '1', '2', '3'], ax=axes[0])
    #fig.savefig('idk.png', dpi=300)


#first tica related to input features, plot each TICA coordinate against each feature
#TICA data file has a list of numpy arrays
