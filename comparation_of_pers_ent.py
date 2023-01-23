#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script gives the plots comparing the 0- and 1-persistence entropy of two groups as the ones showed in the 
paper Persistent entropy detects brain network topological structure.
Lists group1 and group2 contain strings corresponding to the filenames of the adjacency matrices of the 
networks of two groups. In our study we used the files listed in the commented groups. These files are 
found in the compressed folder matrices.zip.
"""
import numpy as np
import matplotlib.pyplot as plt
from pers_ent import pers_ent
from phgraph import ph

group1 = []
group2 = []
#group1 = ['01_g4s01.txt', '02_g4s05.txt', '03_g4s11.txt', '04_g5s01.txt', '05_g5s02.txt', '06_g5s06.txt',
#          '07_g5s08.txt', '08_g5s10.txt', '09_g5s12.txt', '10_g5s13.txt', '11_g6s01.txt', '12_g6s04.txt',
#          '13_g6s06.txt', '14_g6s08.txt', '15_g6s09.txt', '16_g6s13.txt', '17_g6s14.txt', '18_g7c01.txt',
#          '19_g7c04.txt']
#group2 = ['20_g7s01.txt', '21_g7s02.txt', '22_g7s03.txt', '23_g7s05.txt', '24_g7s06.txt', '25_g7s08.txt',
#          '26_g7s09.txt', '27_g7s10.txt', '28_g7s11.txt', '29_g7s12.txt', '30_g7s13.txt', '32_g7s16.txt',
#          '33_g7s17.txt', '34_g7s18.txt', '35_g7s19.txt', '36_g7s22.txt', '37_g7s23.txt', '38_g7s24.txt',
#          '39_g7s25.txt', '40_g7s26.txt', '41_g7s28.txt', '42_g7s29.txt', '43_g7s30.txt']
files=group1+group2
n=len(group1)
m=len(group2)
ent=np.empty((0,2))

for i in range(n+m):   # This loop computes the persistent homology of all the networks
    ph(files[i])       # and writes the resulting barcodes to text files.

for i in range(n+m):   # This loop computes the persistent entropy for all barcodes.
    pe=np.array([[pers_ent(files[i].replace('.txt', '_bc_0.txt')), 
                  pers_ent(files[i].replace('.txt', '_bc_1.txt'))]])
    ent=np.concatenate((ent, pe))
plt.figure(figsize=(10, 12))
## Plot in dimension zero
plt.subplot(211)
plt.plot(np.linspace(1, n, n), ent[0:n, 0], '.b', label="group1")
plt.plot(np.linspace(1, n+0.5, n), np.ones((n))*np.mean(ent[0:n, 0]), color=(0, 0.4470, 0.7410))
ctrl_l=np.ones((n))*np.mean(ent[0:n, 0])-np.ones((n))*np.std(ent[0:n, 0])
ctrl_u=np.ones((n))*np.mean(ent[0:n, 0])+np.ones((n))*np.std(ent[0:n, 0])
plt.plot(np.linspace(1, n+0.5, n), ctrl_u, '--', color=(0, 0.4470, 0.7410))
plt.plot(np.linspace(1, n+0.5, n), ctrl_l, '--', color=(0, 0.4470, 0.7410))
plt.fill_between(np.linspace(1, n+0.5, n),ctrl_l,ctrl_u, color=(0, 0.4470, 0.7410), alpha=0.2)
plt.plot(np.linspace(n+1, n+m, m), ent[n:n+m+1, 0], '.r', label="group2")
plt.plot(np.linspace(n+0.5, n+m, m), np.ones((m))*np.mean(ent[n:n+m+1, 0]), color=(0.8500, 0.3250, 0.0980)) 
isad_u=np.ones((m))*np.mean(ent[n:n+m+1, 0])+np.ones((m))*np.std(ent[n:n+m+1, 0])
isad_l=np.ones((m))*np.mean(ent[n:n+m+1, 0])-np.ones((m))*np.std(ent[n:n+m+1, 0])
plt.plot(np.linspace(n+0.5, n+m, m), isad_u, '--', color=(0.8500, 0.3250, 0.0980) )
plt.plot(np.linspace(n+0.5, n+m, m), isad_l, '--', color=(0.8500, 0.3250, 0.0980))
plt.fill_between(np.linspace(n+0.5, n+m, m), isad_l, isad_u, color=(0.8500, 0.3250, 0.0980), alpha=0.2)
plt.legend(loc='upper right')
plt.title('0-Persistence etropy')
plt.xlabel('Subject ID')
plt.ylabel('0-persistence entropy')
## Plot in dimension one
plt.subplot(212)
plt.plot(np.linspace(1, n, n), ent[0:n, 1], '.b', label="group1")
plt.plot(np.linspace(1, n+0.5, n), np.ones((n))*np.mean(ent[0:n, 1]), color=(0, 0.4470, 0.7410))
ctrl_l=np.ones((n))*np.mean(ent[0:n, 1])-np.ones((n))*np.std(ent[0:n, 1])
ctrl_u=np.ones((n))*np.mean(ent[0:n, 1])+np.ones((n))*np.std(ent[0:n, 1])
plt.plot(np.linspace(1, n+0.5, n), ctrl_u, '--', color=(0, 0.4470, 0.7410))
plt.plot(np.linspace(1, n+0.5, n), ctrl_l, '--', color=(0, 0.4470, 0.7410))
plt.fill_between(np.linspace(1, n+0.5, n),ctrl_l,ctrl_u, color=(0, 0.4470, 0.7410), alpha=0.2)
plt.plot(np.linspace(n+1, n+m, m), ent[n:n+m+1, 1], '.r', label="group2")
plt.plot(np.linspace(n+0.5, n+m, m), np.ones((m))*np.mean(ent[n:n+m+1, 1]), color=(0.8500, 0.3250, 0.0980)) 
isad_u=np.ones((m))*np.mean(ent[n:n+m+1, 1])+np.ones((m))*np.std(ent[n:n+m+1, 1])
isad_l=np.ones((m))*np.mean(ent[n:n+m+1, 1])-np.ones((m))*np.std(ent[n:n+m+1, 1])
plt.plot(np.linspace(n+0.5, n+m, m), isad_u, '--', color=(0.8500, 0.3250, 0.0980) )
plt.plot(np.linspace(n+0.5, n+m, m), isad_l, '--', color=(0.8500, 0.3250, 0.0980))
plt.fill_between(np.linspace(n+0.5, n+m, m), isad_l, isad_u, color=(0.8500, 0.3250, 0.0980), alpha=0.2)
plt.legend(loc='upper right')
plt.title('1-Persistence etropy')
plt.xlabel('Subject ID')
plt.ylabel('1-persistence entropy')
