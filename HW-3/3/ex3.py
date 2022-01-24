'''
Color Perculation
EX-3
Fall 2021
Ali Setareh Kokab
'''
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import colors 
import csv

P=np.linspace(0,1,21) #the probability with which each cell becomes on/off
'''
Graphics
'''
#fig,ax=plt.subplots()
#label=['L=10','L=100','L=200']
#ms=4
#plt.plot(P,np.loadtxt('mean Q10.txt'),'ro',color='r',ms=ms,label=label[0])
#plt.plot(P,np.loadtxt('mean Q100.txt'),'ro',color='y',ms=ms,label=label[1])
#plt.plot(P,np.loadtxt('mean Q200.txt'),'ro',color='g',ms=ms,label=label[2])
#plt.plot(P,np.loadtxt('data80.txt'),'ro',color='b',ms=ms,label=label[3])
#plt.plot(P,np.loadtxt('data160.txt'),'ro',color='black',ms=ms,label=label[4])

#plt.xlabel('p')
#plt.ylabel('Q')
#plt.show()





L=[200]
repetition=100
Q=np.zeros((repetition,np.shape(P)[0]))
Q_mean=np.zeros((len(L),np.shape(P)[0]))
Q_std=np.zeros((len(L),np.shape(P)[0]))

data=open('mean Q200.txt','w')

temp_q=0
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
                Q[r,p_count]=1
        p_count+=1
        print(p)
    Q_mean[temp_q,:]=np.mean(Q,axis=0)
    Q_std[temp_q,:]=np.std(Q,axis=0)
    temp_q+=1
np.savetxt(data,Q_mean,delimiter=',')
data.close()
    #print(l)      
#color=['r','y','b']
#label=['L=10','L=100','L=200']
#fig,ax=plt.subplots()
#for i in range(0,3):    
 #   ax.plot(P,Q_mean[i,:],'ro',color=color[i],ms=3,label=label[i])
#plt.xlabel('p')
#plt.ylabel('Q')
#plt.title('Q vs P')
# get handles
#handles, labels = ax.get_legend_handles_labels()
# use them in the legend
#ax.legend(handles, labels, loc='upper left',numpoints=1)
#plt.show()


