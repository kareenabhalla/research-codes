#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:24:56 2022

@author: kareenabhalla
"""

import numpy as np
from gauelim_pivot import *

dataxs = np.linspace(0,1,6)
datays = np.array([3.085, 3.123, 3.224, 3.360, 3.438, 3.569])
datasigs = np.array([0.048, 0.053, 0.02, 0.005, 0.023, 0.07])

dataxsplot = np.linspace(-1,1)

def phi(n,k,x): 
    if n in range(2,5):
        val = x**k
    return val

def normalfit(dataxs,datays,datasigs,n):
    N = dataxs.size
    A = np.zeros((N,n))
    for k in range(n):
        A[:,k] = phi(n,k,dataxs)/datasigs
    bs = datays/datasigs
    cs = gauelim_pivot(A.T@A, A.T@bs)
    chisq = np.sum((bs - A@cs)**2)
    return cs, chisq
    
import matplotlib.pyplot as plt
import math

def pfit(cs,n,x):
    a = []
    for k in range(n):
        a.append(phi(n,k,x))
    a = np.array(a)
    p = np.sum(cs*a)
    return p

def pfitL(cs,n,dataxsplot):
    pL = []
    for x in dataxsplot:
        pL.append(pfit(cs,n,x))
    pL = np.array(pL)
    return pL

if __name__ == '__main__':
    for n in range(2,5):
        cs, chisq = normalfit(dataxs,datays,datasigs,n)
        print(cs)
        print(chisq/(dataxs.size-cs.size)); print(" ")
        plt.scatter(dataxs,datays)
        plt.errorbar(dataxs,datays,yerr=datasigs,fmt="o")
        x = ("linear", "quadratic", "cubic")
        plt.plot(dataxsplot,pfitL(cs,n,dataxsplot), label= x[n-2])

plt.legend()
plt.show()