
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import random
from copy import deepcopy
from matplotlib.animation import FuncAnimation
from matplotlib import animation as anim
import matplotlib.animation as animation
from celluloid import Camera

def rule(cell,cell_length):

    cell_temp=deepcopy(cell)
    #calculate number of neighbor for each cell
    for row in range(0,cell_length):
        for culumn in range(0,cell_length):
            neighbor=0    
            #conseder all 8 cells near a cell
            for i in range(-1,2):
                for j in range(-1,2):
                    if i!=0 or j!=0: #ignore the present cell
                        row_neighbor=row+i
                        culumn_neighbor=culumn+j
                        #boundry conditions
                        if row+i==cell_length:
                            row_neighbor=0
                        if culumn+j==cell_length:
                            culumn_neighbor=0
        
                        if cell[row_neighbor][culumn_neighbor]==1:
                            neighbor+=1
            
            if neighbor==3 and cell[row][culumn]==0: #born condition
                 cell_temp[row][culumn]=1
            elif neighbor>=4 or neighbor<=1 and cell[row][culumn]==1: #death condition
                 cell_temp[row][culumn]=0
    #G = np.zeros((cell_length,cell_length,3))
    #G[cell_temp==0] = [1,1,1]
    #G[cell_temp==1] = [0,0,0]
    cell=deepcopy(cell_temp)
    return cell


#randome  initial state
#cell=np.random.randint(2,size=(cell_length,cell_length))
#given initial state for exercise 4
#glider and eater:
#initial=[(1,6),(2,5),(3,5),(3,6),(3,7),(5,3),(5,4),(6,4),(7,1),(7,2),(7,3),(8,1)]
#glider:
#initial=[(2,3),(3,1),(3,3),(4,2),(4,3)]
#beacon:
#initial=[(1,1),(1,2),(2,1),(3,4),(4,3),(4,4)]
#loaf:
initial=[(1,2),(1,3),(2,1),(2,4),(3,2),(3,4),(4,3)]

time=10
cell_length=10
cell =np.zeros((cell_length,cell_length))
#giving the initial states:
for i,j in initial:
    cell[i][j]=1



#print(cell)
arr=[]
#apllying the rule to cells:
for t in range(0,time):
    arr.append(cell)
    cell=rule(cell,cell_length)
    #print(cell,"\n",'*********')
    
##animation:

fig = plt.figure()
i=0
im = plt.imshow(arr[0], animated=True)

def updatefig(*args):
    global i
    im.set_array(arr[i])
    if (i<9):
        i += 1
    return im,
plt.title("loaf")
ani = animation.FuncAnimation(fig, updatefig, interval=1000 , blit=True)
#ani.save('loaf.gif', writer='PillowWriter')
plt.show()


