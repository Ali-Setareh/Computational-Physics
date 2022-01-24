#metropolis
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,mean,sigma:(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-mean)**2)*1/sigma**2) #probability distribution
mean=0 #mean of gaussian distribution
sigma=0.4 #std of gaussian distribution
x=mean #initial position of metropolis alg
n=2*10**5 #number of random number which we will produce
#n=10**4
a=[]
ar={0.9:0.2, 0.8:0.4, 0.7:0.63, 0.6:0.86, 0.5:1.15, 0.4:1.55, 0.3:2.1, 0.2:3.2, 0.1:6}
desired_acceptance=0.7

alpha=ar[desired_acceptance] #alpha parameter
accept=0 #number of accepted moves

for i in range(n):
    y=x+alpha*np.random.uniform(-1,1) #our step
    px=f(x,mean,sigma) #caculating the probability of current position
    py=f(y,mean,sigma) #calculating the probability of next position
    w=min(1,py/px) #w parameter
    r=np.random.uniform(0,1) 
    if r<w:
        x=y
        accept+=1
    a.append(x)
#print(accept/n) #acceptance ratio
#plt.hist(a,bins=40)
#plt.show()
j=np.arange(0,len(a)//10**3,1)
cor=[]
for i in j:
    x=a[0:len(a)-i]
    y=a[i:len(a)]   
    cor.append(np.corrcoef(x,y)[0,1])#calculating correlation 
for count,item in enumerate(cor): #finding the Distance correlation
    if item<=1/np.exp(1):
        cor_distance=count
        break

#print(cor_distance)
plt.plot(j,cor)
plt.plot(cor_distance,cor[cor_distance],'ro')
#plt.xlabel('j')
#plt.ylabel('$cor_j$')
plt.show()