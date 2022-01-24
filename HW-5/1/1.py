import numpy as np
import matplotlib.pyplot as plt

def rand(N):
    height=np.zeros(10)
    for i in range(N):
        random=np.random.randint(0,10)
        height[random]+=1
    return height
start=100
end=6000
N=np.arange(start,end,1000)
rel_std=np.zeros(np.shape(N)[0])
counter=0
h=[]
for item in N:
    h.append(rand(item))
 #   rel_std[counter]=np.std(rand(item))/item #for plotting the std 
  #  counter+=1
'''
plt the std:
'''
#plt.plot(N,rel_std,'ro',color='y',label='$\\frac{\sigma}{N}$')
#plt.plot(N,0.3/(np.sqrt(N)),'-',color='r',label='$\\frac{0.3}{\sqrt{N}}$')
#plt.legend(fontsize=9,loc='upper left')
#plt.xlabel('N')
'''
plt the histograms:
'''
fig,ax=plt.subplots(3,2)
x=np.arange(0,10)
counter=0
for i in range(0,3):
    for j in range(0,2):
        ax[i,j].bar(x,h[counter])
        ax[i,j].set_title(label='N=%i'%N[counter])
        counter+=1
plt.show()
