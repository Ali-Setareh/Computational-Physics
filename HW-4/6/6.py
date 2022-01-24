import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import colors as c
l=200
h=[0]*l
particle_number=1000
coin=[-2,-1,1,2]
p=0
mesh=np.zeros((particle_number+8,l))
mesh[0,:]=1
change_color=[1,2] #to change color for every 2000 particles
color_control=0
cMap = c.ListedColormap(['w','r','b']) #colors that we use in pcolormesh
temp=0
coloro_sampling=l
X=np.repeat([np.arange(l+1)],np.shape(mesh)[0]+1,0) # X cooridiante for pcolormesh grid
Y=np.transpose(np.repeat([np.arange(np.shape(mesh)[0]+1)],l+1,0)) # Y cooridiante for pcolormesh grid
while p<particle_number:
    #mesh = np.vstack ((mesh,np.zeros(l)))
    current_x=random.randint(0,l-1)
    lower_bound=max(h)+3
    upper_bound=lower_bound+4
    current_y=lower_bound
    while current_y<=upper_bound:

        flip=random.choice(coin)
        if flip==-1 or flip==1:
            current_x=int((current_x+flip)%l)
        else:
            current_y=int(current_y+flip/2)
            
        if mesh[current_y,current_x-1]+mesh[current_y,int((current_x+1)%l)]+mesh[current_y-1,current_x]+mesh[current_y+1,current_x]>=1:
            if current_y>h[current_x]:
                h[current_x]=current_y
            mesh[current_y,current_x]=change_color[color_control] 
            p+=1
            temp+=1
            if temp==coloro_sampling: #change color:
                color_control+=1
                color_control=color_control%2
                temp=0
            break
    
#print(mesh)
mesh=mesh[~np.all(mesh == 0, axis=1)]
X=np.repeat([np.arange(l+1)],np.shape(mesh)[0]+1,0) # X cooridiante for pcolormesh grid
Y=np.transpose(np.repeat([np.arange(np.shape(mesh)[0]+1)],l+1,0)) # Y cooridiante for pcolormesh grid
#mesh=mesh[~np.all(mesh == 0, axis=1)]
plt.pcolormesh(X,Y,mesh,cmap=cMap)
plt.show()