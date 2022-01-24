import numpy as np
import random
import matplotlib.pyplot as plt
import collections
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

Output = collections.defaultdict(int) 

def two_D_random_walk(time,l):
    coin=[-2,-1,1,2]
    T=time
    current_x=0
    current_y=0
    for t in range(0,T):
        flip=random.choice(coin)
        if flip==-1 or flip==1:
            current_x=current_x+flip*l
        else:
            current_y=current_y+(flip/2)*l

    return current_x,current_y
data=open('5.txt','a')
t=100
sampling_size=100000
position=[]
variance=[]
step_length=4
T=[10,20,30,40,50,60,70,80,90,100]
for t in T:
    variance=[]
    for s in range(sampling_size):
        variance.append(two_D_random_walk(t,step_length)[0]**2+two_D_random_walk(t,step_length)[1]**2)
        #position.append([two_D_random_walk(t)]) # for plotting the distribution function
    data.write('%f\n'%np.mean(variance))
data.close()    
'''
plot the distributaion function:
'''
#for elem in position: 
 #     Output[elem[0]] += 1

#xy=list(Output.keys())
#x=[i[0] for i in xy ]
#y=[i[1] for i in xy ]
#z=list(Output.values())

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x, y, z)


