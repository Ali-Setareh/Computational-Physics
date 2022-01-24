import numpy as np
import matplotlib.pyplot as plt

def rand(N):
    i=0
    b=0
    height=np.zeros(10)
    while i<N:
        random=np.random.randint(0,10)
        if random==4:
            random=np.random.randint(0,10)
            i+=1
            height[random]+=1
    return height

start=100
end=10000
N=np.array([1000,2000,4000,8000])
rel_std=np.zeros(np.shape(N)[0])
counter=0
h=[]
for item in N:
    h.append(rand(item))
    #rel_std[counter]=np.std(rand(item))/item # for plt std vs N
    #counter+=1
x=np.arange(0,10)
fig,ax=plt.subplots(2,2)
counter=0
for i in range(0,2):
    for j in range(0,2):
        ax[i,j].bar(x,h[counter])
        ax[i,j].set_xticks(np.arange(0,10))
        ax[i,j].set_title(label='N=%i'%N[counter])
        counter+=1
plt.show()
'''
plt the std vs N:
'''
#plt.plot(N,rel_std,'ro',color='y',label='$\\frac{\sigma}{N}$')
#plt.plot(N,0.3/(np.sqrt(N)),'-',color='r',label='$\\frac{0.3}{\sqrt{N}}$')
#plt.legend(fontsize=9,loc='upper left')
#plt.xlabel('N')

