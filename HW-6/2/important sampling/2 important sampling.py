#important sampling
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def integral_is(a,b,f,g,n):
    l1=[]
    l2=[]
    l=[]
    ran=np.random.uniform(a,b,n)
    ran=-np.log(1-(1-np.exp(-2))*(ran/2))
    l1=list(map(f,ran))
    l2=list(map(g,ran))
    l=[l1[i]/l2[i] for i in range(len(l1))]
    mean=np.mean(l)
   
    return mean
def g(x): #our function which we use for important sampling 
    if (x>0 and x<2):
        return (1/(1-np.exp(-2)))*np.exp(-x)
    else:
        return 0

f=lambda x:np.exp(-x**2) #function which we want to integrate
b=2 #upper limit
a=0 #lower limit
#n=np.arange(0,1100,100)
n=[1000000]
fig=plt.figure(figsize=(15,8))
ax=fig.add_subplot(111)
integral=[]
error=[]
error_m=[]
real_value=0.8820813907624217
for item in n:
    inte=[]
    inte=[integral_is(a,b,f,g,item) for i in range(0,10)]
    std=np.std(inte) #calculate the standard deviation
    inte=np.mean(inte)
    print(inte)
    print(std)
    #integral.append(inte)
    #error.append(std)
    #error_m.append(abs(inte-real_value)) #the differenece between real value and our algorithm
    #ax.plot(item,std,'ro')
    #ax.set_xlabel('N')
    #ax.set_ylabel('std')
#print(inte)
'''
plot histogram of integral solution:
'''
#ax.hist(inte,bins=100) 
'''
creating the data frame:
'''
#columns=['n','I','delta I','delta I_m']
#n=[i for i in n]
#df = pd.DataFrame(list(zip(n[1:],integral,error,error_m)), columns =columns)
#print(df)
#df.to_excel('is.xlsx')
'''
end data frame
'''
#plt.show()