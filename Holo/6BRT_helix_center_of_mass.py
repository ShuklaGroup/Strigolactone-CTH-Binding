import glob
import numpy as np
import mdtraj as md
from mdtraj.geometry import _geometry
import math

#targettopfile="../prmtop_stripped/stripped.active1_noh.prmtop"
#targettopfile="stripped.4ih4_withlig_noh.prmtop"
#targettopfile="stripped.striga-CLIM-inactive.prmtop"
targettopfile="stripped.6BRT_with_GR24.prmtop"

#def imaging(traj, anchor_mols, other_mols):
#    unitcells = traj.unitcell_vectors

 #   anchor_mol_indices = []
 #   for mol in range(len(anchor_mols)):
 #       anchor_mol_indices.append(anchor_mols[mol])
 #   other_mol_indices = []
 #   for val in range(len(other_mols)):
 #       other_mol_indices.append(other_mols[val])
 #   anchor_mol_indices = np.asarray(anchor_mol_indices)
 #   other_mol_indices = np.asarray(anchor_mol_indices)

 #   result = traj

 #   sort_bonds = sorted(traj._topology.bonds, key=lambda bond: bond[0].index)
 #   sort_bonds = np.asarray([[b0.index, b1.index] for b0, b1 in sort_bonds])

 #   box_part = np.asarray(result.unitcell_vectors, order='c')
 #   _geometry.image_molecules(result.xyz, box_part, anchor_mol_indices, other_mol_indices, sort_bonds)
 #   return traj

#def get_displacement(x1, y1, z1, x2, y2, z2):
#    dis = [x2-x1, y2-y1, z2-z1]
#    return dis

#def manual_imaging(trajfile, topfile):
#    box_dim = trajfile.unitcell_lengths
#    ref_atom = trajfile.atom_slice([3408])
#    helix = topfile.select("resid 269 to 287")
#    helix_atoms = trajfile.atom_slice(helix)
#    print(helix_atoms)
#    test_com = md.compute_center_of_mass(helix_atoms)
#    print(test_com)
                       #problem_children_z = []
#    for frame in range(trajfile.n_frames):
#        x1 = ref_atom.xyz[frame][0][0]
#        y1 = ref_atom.xyz[frame][0][1]
#        z1 = ref_atom.xyz[frame][0][2]
                     #helix_atoms.make_molecules_whole(inplace=True)
#        for one_atom in range(len(helix)):
#            x2 = helix_atoms.xyz[frame][one_atom][0]
#            y2 = helix_atoms.xyz[frame][one_atom][1]
#            z2 = helix_atoms.xyz[frame][one_atom][2]
#            x_len = box_dim[frame][0]
#            y_len = box_dim[frame][1]
#            z_len = box_dim[frame][2]
#            displacement = get_displacement(x1, y1, z1, x2, y2, z2)
                        #note from Jiming: shits coordinates of atom j per minimum image convention
#            if displacement[0] < -x_len/2:
                            #    print(frame, one_atom, x2)
#                helix_atoms.xyz[frame][one_atom][0] += (int(x2/x_len) + 1)*x_len
                          #   print(frame, one_atom, x2)
#            elif displacement[0] > x_len/2:
                           #  print(frame, one_atom, x2)
#                helix_atoms.xyz[frame][one_atom][0] -= (int(x2/x_len) + 1)*x_len
                           # print(frame, one_atom, x2)

#            if displacement[1] < -y_len/2:
#                helix_atoms.xyz[frame][one_atom][1] += (int(y2/y_len) + 1)*y_len
                           #  print(frame, one_atom)
#            elif displacement[1] > y_len/2:
#                helix_atoms.xyz[frame][one_atom][1] -= (int(y2/y_len) + 1)*y_len
                         #  print(frame, one_atom)

#            if displacement[2] < -z_len/2:
                       # print(frame, one_atom, helix_atoms.xyz[frame][one_atom][2], z_len, z_len/2)
                       #   print(frame, one_atom, helix_atoms.xyz[frame][one_atom][2])
#                helix_atoms.xyz[frame][one_atom][2] += (int(z2/z_len) + 1)*z_len
                       #print(helix_atoms.xyz[frame][one_atom][2])
                      # problem_children_z.append(frame, one_atom)
#            elif displacement[2] > z_len/2:
#                helix_atoms.xyz[frame][one_atom][2] -= (int(z2/z_len) + 1)*z_len
                        #    print(frame, one_atom)
#        helix_atoms.make_molecules_whole(inplace=True)
#    print(helix_atoms.xyz[247])
#    return helix_atoms    
test_data = glob.glob('./lig_stripped/*.dcd')

for file in test_data:
#for file in glob.glob('./stripped/*.strip.dcd'):
    q = md.load(file, top=targettopfile)
    top = md.load(file, top=targettopfile).topology
    #t = manual_imaging(q, top)
    r = top.select("resid 269 to 287")
    t = q.atom_slice(r)
    #print(t)
    d = md.compute_center_of_mass(t)  
    n_frames = t.n_frames
    #print(np.shape(d))

    dis = np.empty([n_frames, 3])

    for i in range(n_frames):
        for j in range(3):
            dis[i,j]=d[i][j]
    
#    checking=top.select("resid 269 to 287")
#    danny= q.atom_slice(checking)
#    radio_rebel = t.xyz
#    im_lemonade_mouth = danny.xyz
    #print(im_lemonade_mouth.shape)

#    for i in range(n_frames):
#        print(radio_rebel[i][264], im_lemonade_mouth[i][264], i)

    #print(radio_rebel[944][24], im_lemonade_mouth[944][24])
#    print(radio_rebel[247][277], im_lemonade_mouth[247][277])
#    print(d[247]) 
 
   # print(t.xyz[0][8]) 
   # t.xyz[0][8][0] = 20
   # print(t.xyz[0][8])

    np.save('./lig_analysis/Mass/'+file.split('/')[-1]+'_lig_helix_center_of_mass.npy',dis)
