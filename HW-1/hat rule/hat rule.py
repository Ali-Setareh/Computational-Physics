
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

#rules for wearing a hat
def rule (a,b): 
    if a==1 and b==1:
        return 0
    if a==1 and b==0:
        return 1
    if a==0 and b==1:
        return 1
    if a==0 and b==0:
        return 0

cell=[] 
cell_temp=[]
cell_length=101
for i in range(0,cell_length): #initial state of cells 
    if i==cell_length//2:
        cell.append(1)
    else:
        cell.append(0)

#for how many time steps the program should run
time=100
#a copy of main cell
cell_temp=list(cell) 
#matrix contains state of each cell in everye time steps
matrix_cell=np.zeros((time,cell_length)) 
for i in range(0,time):
    matrix_cell[i]=cell
    for j in range(0,len(cell)): #going through each cell and apply the rule
        if j==len(cell)-1:
            cell_temp[j]=rule(cell[j-1],cell[0])
        else:
            cell_temp[j]=rule(cell[j-1],cell[j+1])
    cell=list(cell_temp)


G = np.zeros((time,cell_length,3))
# Where we set the RGB for each pixel
G[matrix_cell==0] = [1,1,1]
G[matrix_cell==1] = [0,0,0]

plt.xlabel("cells")
plt.ylabel("time")
plt.title("hat rule for %i people"%cell_length)
plt.imshow(G,interpolation='nearest')
plt.show()
