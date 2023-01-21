#!/usr/bin/env python3
'''This script contains the function ph() which obtains a filtration and computes its persistent homology given a weighted graph
as described in the paper Persistent entropy detects brain network topological structure.
The input is a text file with adjacency matrix, each row of the file corresponds to each row
of the matrix.
The output is a pair of text files with the information of the zero and one dimensional barcodes. The first
column contains the birth time of each homology class and the second column the death time. Optionally, barcodes 
can be plotted changing to True the values in the last tow lines of this script.  
Dionysus module is needed to compute persistent homology. Version 2 was used for this script and was downloaded 
via conda.'''
import numpy as np
import dionysus as d

def density(A): # This function is used to compute the density of the matrices
    s=len(A)    # which is used as index of the filtration
    return np.count_nonzero(A)/(s*(s-1))

def ph(filename):
    matrix=[]
    with open(filename) as f:
        lines=f.readlines()[1:] # matrices used in the study, and added to this repository, have a label first column which is ommited
        for line in lines:
            row=line.split(' ')
            del row[0]
            row2=[float(num) for num in row] 
            matrix.append(row2)
    A=matrix
    A=np.array(A)
    s=len(A)
    maximum=max(map(max, A))
    T=[]
    E=np.empty((0,3), float)
    n=1000 #This is the number of equally distributed steps of the filtration. 
    weights =np.linspace(0, maximum, n+1)  
    id=A==np.zeros((s, s))
    for r in range(n):
        r=r+1
        M=np.ones((s, s))*weights[-r]
        B=A>=M
        B[id]=0
        index=density(B)
        if r>1:
            M2=np.ones((s,s))*weights[-r+1]
            B2=np.logical_and(A>=M, A<M2)
            B2[id]=0
        else:
            B2=B #Edges added at time r
        [row, column]=np.nonzero(np.triu(B2))
        E=np.concatenate((E, np.concatenate((row[None].T, column[None].T, np.ones((len(row), 1))*index), axis=1)))
        for i in range(s-2):
            for j in range(i+1, s-1):
                if B[i][j]:
                    for k in range(j+1, s):
                        if B[i][k] and B[j][k] and (B2[i][j] or B2[i][k] or B2[j][k]):
                            T.append([i, j, k, index])
    V=np.concatenate((np.linspace(0, s-1, s)[None], np.zeros((s))[None]))
    V=V.T.tolist()
    E=E.tolist()
    ###persistent homology
    list = V + E + T
    simplices = []
    for row in list:
        simplices.append(([int(a) for a in row[0:-1]], row[-1]))
    f = d.Filtration()
    for vertices, time in simplices:
        f.append(d.Simplex(vertices, time))
    f.sort()
    m = d.homology_persistence(f, prime=2)
    diagrams = d.init_diagrams(m, f)
    filename=filename.replace('.txt', '')
    for j in range(2):
        file = open(filename + '_bc_' + str(j) + '.txt', 'w')
        for pt in diagrams[j]:
            file.write(f"{pt.birth} {pt.death}\n")
        file.close()
    d.plot.plot_bars(diagrams[0], show=False)
    d.plot.plot_bars(diagrams[1], show=False)
    
    
