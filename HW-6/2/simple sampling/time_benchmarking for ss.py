import timeit

# code snippet to be executed only once  
mysetup = "import numpy as np"
            
  
# code snippet whose execution time is to be measured 
mycode = '''  
def integral_ss(a,b,f,n):
    ran=np.random.uniform(a,b,n)
    mean=np.mean(list(map(f,ran)))
    return (b-a)*mean
f=lambda x:np.exp(-x**2) #function which we want to integrate
b=2 #upper limit
a=0 #lower limit
n=[1000] 
for item in n:
    inte=integral_ss(a,b,f,item)
'''
t=(timeit.timeit(setup = mysetup,stmt = mycode,number = 10000))/10000
# timeit statement  
print('t:%.6f'%t)