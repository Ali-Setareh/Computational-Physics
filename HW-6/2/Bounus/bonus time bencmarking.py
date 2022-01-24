import timeit

# code snippet to be executed only once  
mysetup = "import numpy as np"
            
  
# code snippet whose execution time is to be measured 
mycode = '''  
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

def g(x):
    if (x>0 and x<2):
        return (1/np.log(3))*(1/(x+1))
    else:
        return 0

f=lambda x:np.exp(-x**2) #function which we want to integrate
b=2 #upper limit
a=0 #lower limit
n=[100]

for item in n:
    inte=integral_is(a,b,f,g,item)
'''
t=(timeit.timeit(setup = mysetup,stmt = mycode,number = 10000))/10000
# timeit statement  
print('t:%.6f'%t)