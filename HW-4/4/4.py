import numpy as np
import matplotlib.pyplot as plt
l=20
rw=np.zeros(l+3)
temp=np.zeros(l+3)
rw[int(5)]=1
s=0
t=0
death=0

init=np.arange(1,l+2)

x=np.zeros(l+2)
for u in init:
    rw=np.zeros(l+3)
    temp=np.zeros(l+3)
    rw[u]=1
    t=0
    death=0
    death_time=0
   
    while death<0.99:
        temp[:]=0
        t+=1
        for i in range (l+3):
            if rw[i]==0:
                if i==0:
                    temp[i]=rw[i+1]*(0.5**t) 
                elif i==l+2:
                    temp[i]=rw[i-1]*(0.5**t) 
                else:
                    temp[i]=(rw[i-1]+rw[i+1])
            if temp[0]!=0 or temp[l+2]!=0:
                death_time=death_time+(temp[0]+temp[l+2])*t
                death=death+(temp[0]+temp[l+2])
                temp[0]=0
                temp[l+2]=0
        rw=np.copy(temp)
    x[u]=death_time

plt.plot(init-11,x[1:l+2],'ro')
p=np.polyfit(init-11,x[1:l+2],2)
print(p)
plt.xlabel('initial position')
plt.ylabel('life time')
plt.show()
