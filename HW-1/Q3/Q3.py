import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

#rule 110
def rule (a,b,c,d): # d is a list contains of rule in binary form 
    if a==1 and b==1 and c==1:
        return d[0]
    if a==1 and b==1 and c==0:
        return d[1]
    if a==1 and b==0 and c==1:
        return d[2]
    if a==1 and b==0 and c==0:
        return d[3]
    if a==0 and b==1 and c==1:
        return d[4]
    if a==0 and b==1 and c==0:
        return d[5]
    if a==0 and b==0 and c==1:
        return d[6]
    if a==0 and b==0 and c==0:
        return d[7]
def convert(string): #convert function takes a string and convert it to a list
    list1=[] 
    list1[:0]=string 
    list1 = [ int(x) for x in list1 ]
    return list1

cell=[] 
cell_temp=[]
cell_length=201
time=300 #for how many time steps the program should run
rule_110="01101110"
rule_converted=convert(rule_110)

#Matrix cell contains history of cells:
matrix_cell=np.zeros((time,cell_length))
rule_converted_temp=np.zeros((8,8),dtype=int)
temp=0
for k in range(0,8): #calculate all the possible rules by flipping a zero to one or vice versa
    rule_converted_temp[k]=rule_converted
    if rule_converted[temp]==1:
        rule_converted_temp[k][temp]=0
    else:
        rule_converted_temp[k][temp]=1
    temp+=1


#a copy of main cell
cell_temp=list(cell) 
#matrix contains state of each cell in everye time steps
matrix_cell=np.zeros((time,cell_length)) 
for k in range(0,8): #this for is a loop through all the rules
    ruule=rule_converted_temp[k]
    cell=[0]*cell_length
    cell[cell_length//2]=1
    cell_temp=list(cell)
     
    for i in range(0,time):
        matrix_cell[i]=cell
        for j in range(0,len(cell)): #going through each cell and apply the rule
            if j==len(cell)-1:
                cell_temp[j]=rule(cell[j-1],cell[j],cell[0],list(ruule))
            else:
                cell_temp[j]=rule(cell[j-1],cell[j],cell[j+1],list(ruule))
        cell=list(cell_temp)

    G = np.zeros((time,cell_length,3))
    # Where we set the RGB for each pixel
    G[matrix_cell==0] = [1,1,1]
    G[matrix_cell==1] = [0,0,0]
    res = int("".join(str(x) for x in ruule), 2) 
    plt.title('rule: %s'%res)
    plt.xlabel('cells')
    plt.ylabel('time')
    plt.imshow(G,interpolation='nearest')
    plt.show()