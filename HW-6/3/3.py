
from math import pi
import numpy as np
def random_generator(R,n): #produce 3 sets of random numbers (x,y,z) in a sphere with radius R
    x=np.random.uniform(-R,R,n) #first we produce random numbers within a cube
    y=np.random.uniform(-R,R,n)
    z=np.random.uniform(-R,R,n)
    x_copy=[]
    y_copy=[]
    z_copy=[]
    for i in range(n): #then we pick those which dropped inside the sphere
        if x[i]**2+y[i]**2+z[i]**2<=R**2:
            x_copy.append(x[i])
            y_copy.append(y[i])
            z_copy.append(z[i])
    return x_copy,y_copy,z_copy
def CM(X,Y,Z,P,R,n):
    x,y,z=random_generator(1,n)
    total_mass=(4/3)*pi*(R**3)*np.mean([P(x[i],y[i],z[i],R) for i in range(len(x))])
    x_cm=(4/3)*pi*(R**3)*np.mean([X(x[i],y[i],z[i],R) for i in range(len(x))])/total_mass
    y_cm=(4/3)*pi*(R**3)*np.mean([Y(x[i],y[i],z[i],R) for i in range(len(x))])/total_mass
    z_cm=(4/3)*pi*(R**3)*np.mean([Z(x[i],y[i],z[i],R) for i in range(len(x))])/total_mass
    return x_cm,y_cm,z_cm

P=lambda x,y,z,R:z+3*R #density function
X=lambda x,y,z,R:x*(z+3*R) #x component
Y=lambda x,y,z,R:y*(z+3*R) #y component
Z=lambda x,y,z,R:z*(z+3*R) #z component

R=1
N=1
n=2*10**7                                                                                                                                   
mean_x=0
mean_y=0
mean_z=0
for j in range(N):
    x,y,z=CM(X,Y,Z,P,R,n)
    mean_x+=x
    mean_y+=y
    mean_z+=z
x_cm=mean_x/N
y_cm=mean_y/N
z_cm=mean_z/N
print('x:',x_cm,'\n','y:',y_cm,'\n','z:',z_cm)