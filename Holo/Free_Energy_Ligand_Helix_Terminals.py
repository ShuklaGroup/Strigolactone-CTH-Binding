import numpy as np #adding some packages to use
import matplotlib
matplotlib.use("Agg") 
#use figure as an RGBA buffer (red, green, blue, alpha) convert to array, render through Pillow
import matplotlib.pyplot as plt

import argparse
#lets you add arguments when you call the program, changes how the program is run
import glob #finds all pathnames associated with a certain pattern
plt.rc('savefig', dpi=500) #dpi is resolution, dots per inch
matplotlib.rc('font',family='Helvetica-Normal',size=20) #controls font size, not too hard

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
    cbar.set_label("Free Energy (kcal/mol)",size=20)
    cbar.ax.set_yticklabels(range(max_energy+1))
    cbar.ax.tick_params(labelsize=16)
    plt.tick_params(axis='both',labelsize=16)
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
    parser.add_argument("--ax_labels", nargs=2, type=str, help="Axis labels")
    parser.add_argument("--ax_lims", nargs=4, type=float, help="Axis limits")
    parser.add_argument("--max_energy", nargs=1, default=6, type=int, help="Maximum free energy")
    parser.add_argument("--weights", type=str, help="Pickle file containing MSM weights")
    parser.add_argument("--savename", type=str, help="Output file name")
    #nargs means multiple command line arguments for a single action

    args = parser.parse_args()
    
    return args

if __name__=="__main__": #'__main__' is the name of the python module. Name is set to the name of the script or module

    args = get_args()

    ax1_files = sorted(glob.glob('lig_analysis/Helices/*n_terminus*'))
    ax2_files = sorted(glob.glob('lig_analysis/Helices/*c_terminus*'))
    #returns a list of path names following the pattern, in alphabetical order

    ax1_data = []
    ax2_data = []

    for data_file in ax1_files: #for every file in the first list made
        ax1_data.extend(np.load(data_file)) #adds every data point from the file into the ax1_data array

    ax1_data = np.array(ax1_data)

    if len(np.shape(ax1_data)) > 1: #if the matrix has more than 1 entry
        ax1_data = ax1_data[:,0] #puts a zero at the end

    for data_file in ax2_files: #same as above but for the second list
        ax2_data.extend(np.load(data_file))

    ax2_data = np.array(ax2_data)    

    if len(np.shape(ax2_data)) > 1:
        ax2_data = ax2_data[:,0]

    print(np.shape(ax1_data)) #print new matrix sizes
    print(np.shape(ax2_data))

    if args.weights == None: #if we didn't provide a file with the weights
        free_energy(ax1_data, ax2_data, lims=(args.ax_lims[0], args.ax_lims[1], args.ax_lims[2], args.ax_lims[3]), max_energy=args.max_energy, label1=args.ax_labels[0], label2=args.ax_labels[1], savename=args.savename)
        #we added an argument above called ax_lims to determine the limit of the axes
    else:
        import pickle #if we did provide the file, this will run
        weights_all = pickle.load(open(args.weights,'rb')) #open the file
        weights = [] #make array
        for traj in weights_all: #for a trajectory in the array
            weights.extend(traj) #add trajectories to the array
        weights = np.array(weights)
        print(np.shape(weights)) #print array shape
        free_energy(ax1_data, ax2_data, lims=(args.ax_lims[0], args.ax_lims[1], args.ax_lims[2], args.ax_lims[3]), max_energy=args.max_energy, label1='N Term-A223 Distance (nm)', label2='C Term-A223 Distance (nm)', savename=args.savename, weights=weights)
