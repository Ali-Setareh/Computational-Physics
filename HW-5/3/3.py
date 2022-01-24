import numpy as np
import matplotlib.pyplot as plt

n=[5,10,100,1000]
#n=np.arange(10,1000,50) #for plotting standard deviation
mean=[]
for i in n:
    x=[np.mean(np.random.randint(0,10,i)) for j in range(10000)]
    mean.append(x)
fig,ax=plt.subplots(len(n)//2,2,figsize=(8,8))
k=0
for i in range(0,len(n)//2):
    for j in range(0,2):
        ax[i,j].hist(mean[k],100,density=True)
        ax[i,j].set_title(label='N=%i'%n[k])
        k+=1
'''
plotting std vs N
'''
#standard_deviation=[np.std(mean[k]) for k in range(len(n))]
#fig2,ax2=plt.subplots()
#ax2.plot(n,standard_deviation,'ro',color='y')
#ax2.set_xlabel('N')
#ax2.set_ylabel('$\\sigma$')
plt.show()