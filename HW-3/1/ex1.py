'''
HW-3
EX-1
Fall 2021
Ali Setareh Kokab
'''
import numpy as np
import matplotlib.pyplot as plt
l=20
p=0.8
X=np.linspace(1,l,l)
X=np.repeat([X],l,axis=0)
Y=np.linspace(1,l,l)
Y=np.transpose(np.repeat([Y],l,axis=0))
Z=np.random.rand(l-1,l-1)
Z=(Z<p).astype(int)
#print(Z)
plt.pcolormesh(X,Y,Z,cmap='gray_r')
plt.show()