#simple sampling monte carlo
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import timeit

def integral_ss(a,b,f,n): #simple sampling alghorithm
    ran=np.random.uniform(a,b,n)
    mean=np.mean(list(map(f,ran)))
    return (b-a)*mean

f=lambda x:np.exp(-x**2) #function which we want to integrate
b=2 #upper limit
a=0 #lower limit
#n=np.arange(0,1100,100) #number of samples
n=[1000000] 
fig=plt.figure(figsize=(15,8))
ax=fig.add_subplot(111)
integral=[]
error=[]
error_m=[]
real_value=0.8820813907624217
for item in n:
    inte=[]
    inte=[integral_ss(a,b,f,item) for i in range(0,10)]
    std=np.std(inte) #calculate the standard deviation
    inte=np.mean(inte) #integral solution for n
    print(inte)
    print(std)
    #integral.append(inte)
    #error.append(std)
    #error_m.append(abs(inte-real_value)) #the differenece between real value and our algorithm
    #ax.plot(item,std,'ro') #plot std vs n 
    #ax.set_xlabel('N')
    #ax.set_ylabel('std')
'''
creating the data frame:
'''
#columns=['n','I','delta I','delta I_m']
#n=[i for i in n]
#df = pd.DataFrame(list(zip(n[1:],integral,error,error_m)), columns =columns)
#print(df)
#df.to_excel('ss.xlsx')
'''
end data frame
'''

'''
plot of integral soulution vs n
'''
#plt.plot(n[1:],integral,color='y') #integral solution vs n plot
#plt.plot(n,[0.8820813907624217]*np.shape(n)[0])#true value of the integral using mathematica
#plt.xlabel('n')
#plt.ylabel('integral')
'''
histogram of integral solution for a specific n :
'''
#ax.hist(inte,bins=100) #histogram of integral solution for a specific n
#plt.xlabel('integral solution')
#plt.show()