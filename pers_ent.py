#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function computes the persistent entropy as described in the paper. 
The input is a text file with the information of a barcode: each row
corresponds to a bar and consists of two entries, the birth and death 
time of the bar.
The output is a float number corresponding to the persistent entropy.
"""
import numpy as np
def pers_ent(filename):
    Bc = np.loadtxt(filename)
    m=max(Bc[np.where(Bc[:,1]!=np.inf)][:,1])
    Bc[Bc==np.inf]=m+1
    lengths=Bc[:,1]-Bc[:,0]
    L=sum(lengths)
    return(-1*float(sum((lengths/L)*(np.log(lengths/L)))))
