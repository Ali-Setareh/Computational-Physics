import numpy as np
import matplotlib.pyplot as plt

n=20
lattice=np.zeros((2*n+2,2*n+2))
lattice[(2*n+2)//2,(2*n+2)//2]=1

total=0
def saw(x,y,j):
    global total
    global lattice
    #print(lattice,'\n',j)
    if j==0:
        total+=1
    else:
        if lattice[x+1,y]==0:
            lattice[x+1,y]=1
            saw(x+1,y,j-1)
        
        if lattice[x-1,y]==0:
            lattice[x-1,y]=1
            saw(x-1,y,j-1)

        if lattice[x,y+1]==0:
            lattice[x,y+1]=1
            saw(x,y+1,j-1)

        if lattice[x,y-1]==0:
            lattice[x,y-1]=1
            saw(x,y-1,j-1)
    lattice[x,y]=0
steps=np.arange(1,16)
data=open('data.txt','w')
for n in steps:
    lattice=np.zeros((2*n+2,2*n+2))
    lattice[(2*n+2)//2,(2*n+2)//2]=1
    total=0
    saw((2*n+2)//2,(2*n+2)//2,n)
    data.write('%i\n'%total)
data.close()

        


