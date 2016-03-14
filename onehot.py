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

    y=yt.transpose()
    return y
