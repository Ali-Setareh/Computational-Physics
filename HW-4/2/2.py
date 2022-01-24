import numpy as np
import random
import matplotlib.pyplot as plt
from fractions import Fraction
def random_walk(time,p): #random walk function
    #coin=[-1,1]
    coin=[1]*(p.numerator)
    coin.extend([-1]*(1-p).numerator)
    T=time
    current=0
    for t in range(0,T):
        current=current+random.choice(coin)
    return current
p=Fraction(1,2)
T=[100]
sampling_size=100000
position=np.zeros(sampling_size)
#data=open('2.txt','a')
for t in T:
    #data.write('t=%i\n'%t)
    for s in range(sampling_size):
        position[s]=random_walk(t,p)
    unique, counts = np.unique(position, return_counts=True) #calculate clusters surface
    position_count=dict(zip(unique, counts))
    #data.write('P=%f: mean:%f var:%f\n'%(p,np.mean(position),np.var(position)))

plt.bar(position_count.keys(),np.asarray(list(position_count.values()))/sampling_size)
plt.xlabel('positions')
plt.ylabel('positions probability distribution')


#data.close()
plt.show()