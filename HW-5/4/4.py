import numpy as np 
import matplotlib.pyplot as plt
import collections
from mpl_toolkits.mplot3d import Axes3D
def gaussian(x1,x2,sigma):
    r=np.sqrt(-2*sigma**2*np.log(x1))
    theta=2*np.pi*x2
    return r,theta
x=[]
y=[]
sigma=0.2
sample_size=10000
for i in range(sample_size):
    x1=np.random.rand()
    x2=np.random.rand()
    r,theta=gaussian(x1,x2,sigma)
    x.append(r*np.cos(theta))
    y.append(r*np.sin(theta))
fig=plt.figure()
ax=fig.add_subplot(2,2,1)
ax.scatter(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(label=1)
ax=fig.add_subplot(2,2,2)
ax.hist(x,100)
ax.set_xlabel('x')
ax.set_title(label=2)
ax=fig.add_subplot(2,2,3)
ax.hist(y,100)
ax.set_xlabel('y')
ax.set_title(label=3)
#fig,ax=plt.subplots(2,2)
'''
plot distribution
'''
Output = collections.defaultdict(int) 
position=[[tuple(['{:.2f}'.format(x[i]),'{:.2f}'.format(y[i])])] for i in range(sample_size)]
for elem in position: 
      Output[elem[0]] += 1

xy=list(Output.keys())
x=[i[0] for i in xy ]
y=[i[1] for i in xy ]
z=list(Output.values())
x=[float(i) for i in x]
y=[float(i) for i in y]

ax = fig.add_subplot(224,projection='3d')
ax.plot(x,y,z,'ro',color='b',ms=2)
ax.set_title(label=4)
plt.show()