#velghasht ba tale
import numpy as np
import random
import matplotlib.pyplot as plt
def trapped_rw(length,inittal):
    coin=[-1,1]
    current=inittal
    t=0
    while abs(current)<=length:
        current=current+random.choice(coin)
        t+=1
    return t

l=20
init_position=np.arange(-l/2,l/2+1)
sampling_size=10000
time_position=np.zeros((sampling_size,init_position.shape[0]))
temp=0
for i in init_position:
    for s in range(sampling_size):
        time_position[s][temp]=trapped_rw(l/2,i)
    temp+=1
fig,ax=plt.subplots()
ax.plot(init_position,time_position.mean(axis=0),'ro')
plt.xlabel('initial position')
plt.ylabel('life time')
p=np.polyfit(init_position,time_position.mean(axis=0),2)
print(p)
plt.show()


