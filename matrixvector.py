import numpy as np

A= np.array([
    [.9,.07,.02,.01],
    [0,.93,0.05,0.02],
    [0,0,.85,0.15],
    [0,0,0,1.00]
])

x= np.array([
   [.85,.10,.05,0] 
])

ATranspose = A.T
#print(ATranspose)

xTranspose = x.T
#print(xTranspose)

print(A.T @ x.T)