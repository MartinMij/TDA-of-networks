#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script gives the plots comparing the 0- and 1-persistence entropy of two groups as the ones showed in the 
paper Persistent entropy detects brain network topological structure.
Lists group1 and group2 contain strings corresponding to the filenames of the adjacency matrices of the 
networks of two groups. 
"""
import numpy as np
import matplotlib.pyplot as plt
from pers_ent import pers_ent
from phgraph import ph

group1 = []
group2 = []
files=group1+group2
n=len(group1)
m=len(group2)
ent=np.empty((0,2))

for i in range(n+m):
    ph(files[i])

for i in range(n+m):
    pe=np.array([[pers_ent(files[i].replace('.txt', '_bc_0.txt')), 
                  pers_ent(files[i].replace('.txt', '_bc_1.txt'))]])
    ent=np.concatenate((ent, pe))
plt.figure(figsize=(10, 12))
plt.subplot(211)
plt.plot(np.linspace(1, n, n), ent[0:n, 0], '.b', label="group1")
plt.plot(np.linspace(1, n+0.5, n), np.ones((n))*np.mean(ent[0:n, 0]), color=(0, 0.4470, 0.7410))
ctrl_l=np.ones((n))*np.mean(ent[0:n, 0])-np.ones((n))*np.std(ent[0:n, 0])
ctrl_u=np.ones((n))*np.mean(ent[0:n, 0])+np.ones((n))*np.std(ent[0:n, 0])
plt.plot(np.linspace(1, n+0.5, n), ctrl_u, '--', color=(0, 0.4470, 0.7410))
plt.plot(np.linspace(1, n+0.5, n), ctrl_l, '--', color=(0, 0.4470, 0.7410))
plt.fill_between(np.linspace(1, n+0.5, n),ctrl_l,ctrl_u, color=(0, 0.4470, 0.7410), alpha=0.2)
plt.plot(np.linspace(20, n+m, m), ent[n:n+m+1, 0], '.r', label="group2")
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
##
plt.subplot(212)
plt.plot(np.linspace(1, n, n), ent[0:n, 1], '.b', label="group1")
plt.plot(np.linspace(1, n+0.5, n), np.ones((n))*np.mean(ent[0:n, 1]), color=(0, 0.4470, 0.7410))
ctrl_l=np.ones((n))*np.mean(ent[0:n, 1])-np.ones((n))*np.std(ent[0:n, 1])
ctrl_u=np.ones((n))*np.mean(ent[0:n, 1])+np.ones((n))*np.std(ent[0:n, 1])
plt.plot(np.linspace(1, n+0.5, n), ctrl_u, '--', color=(0, 0.4470, 0.7410))
plt.plot(np.linspace(1, n+0.5, n), ctrl_l, '--', color=(0, 0.4470, 0.7410))
plt.fill_between(np.linspace(1, n+0.5, n),ctrl_l,ctrl_u, color=(0, 0.4470, 0.7410), alpha=0.2)
plt.plot(np.linspace(20, n+m, m), ent[n:n+m+1, 1], '.r', label="group2")
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