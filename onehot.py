# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:08:16 2016

@author: Administrator
"""

import numpy as np

def one_hot(x,dim):
    shape = x.shape
    nshape=list(shape)
    nshape.append(dim)
   
    y = np.zeros((nshape)) 
        
    xt=x.transpose()
    yt=y.transpose()
    
    for i in range(xt.shape[0]):    
        yt[:,i]=(xt[i]==range(dim)).reshape(dim,1)
#    for y[]
    y=yt.transpose()
    return y