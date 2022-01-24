'''
HW-3
EX-2
Fall 2021
Ali Setareh Kokab
'''
import numpy as np
import matplotlib.pyplot as plt

P=[0.3] #the probability with which each cell becomes on/off
L=[200]
repetition=1


for l in L:
    p_count=0
    for p in P:
        for r in range(0,repetition):
            k=0
            Z=np.random.rand(l,l) 
            Z=(Z<p).astype(int)
            Z=np.insert(Z,0,np.zeros(l),axis=1) #add a culumn of ones as a boundry condition
            Z=np.insert(Z,l+1,np.zeros(l)-1,axis=1)
            Z=np.insert(Z,0,np.zeros(l+2),axis=0)
            Z=np.insert(Z,l+1,np.zeros(l+2),axis=0)
            #print(Z,'\n')
            for j in range(1,l+2):
                for i in range(1,l+1):
                    if Z[i,j]:
                        above=Z[i-1,j]
                        left=Z[i,j-1]
                        if above==0 and left==0:
                            k+=1
                            Z[i,j]=k 
                        elif above!=0 and left==0:
                            Z[i,j]=above
                        elif above==0 and left!=0:
                            Z[i,j]=left
                        else:
                            Z[i,j]=left
                            Z[Z==above]=left
            percolation=np.intersect1d(Z[1:l+1,1],Z[1,l+1])
            if percolation:
                print('percolation!')
        p_count+=1
X=np.linspace(0,L[0]+3,L[0]+3) 
X=np.repeat([X],L[0]+3,axis=0) #X grid for pcolormesh
Y=np.linspace(0,L[0]+3,L[0]+3)
Y=np.transpose(np.repeat([Y],L[0]+3,axis=0)) #Y grid for pcolormesh

plt.pcolormesh(X,Y,Z)
plt.show()