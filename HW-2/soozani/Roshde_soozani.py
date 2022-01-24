'''
Roshd_e_Soozani
EX-2
Fall 2021
Ali Setareh Kokab
'''
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c

'''
funcetions:
'''
def graphic(layer_length,number_of_particles):

    Z=np.zeros([number_of_particles,layer_length],dtype=float) #matix in which we save position of on/off pixels
    height=[0]*layer_length # A list which contains height of each box 
    height[layer_length//2]=1
    Z[1,layer_length//2]=2
    
    change_color=[1,2] #to change color for every 2000 particles
    X=np.repeat([np.arange(layer_length+1)],np.shape(Z)[0]+1,0) # X cooridiante for pcolormesh grid
    Y=np.transpose(np.repeat([np.arange(np.shape(Z)[0]+1)],layer_length+1,0)) # Y cooridiante for pcolormesh grid
    color_control=0 
    cMap = c.ListedColormap(['w','r','b']) #colors that we use in pcolormesh
    temp=0
    coloro_sampling=10*layer_length
    
    i=0
    while i!=number_of_particles: 
        n=random.randint(0,layer_length-1) # A random number
        if height[n]!=0 or height[n-1]!=0 or height[(n+1)%layer_length]:
            i+=1
            if height[n]>=height[n-1] and height[n]>=height[(n+1)%layer_length]:    
                height[n]+=1
                Z[height[n],n]=change_color[color_control]
                

            else:
                max_height=max(height[n-1],height[(n+1)%layer_length])
                Z[max_height,n]=change_color[color_control] 
                height[n]=max_height

            temp+=1
            if temp==coloro_sampling: #change color:
                color_control+=1
                color_control=color_control%2
                temp=0
    plt.show()
    Z=Z[~np.all(Z == 0, axis=1)]
    X=np.repeat([np.arange(layer_length+1)],np.shape(Z)[0]+1,0)
    Y=np.transpose(np.repeat([np.arange(np.shape(Z)[0]+1)],layer_length+1,0))
    plt.pcolormesh(X,Y,Z,cmap=cMap)
    plt.title('Roshd_e_soozani for %i particles and a layer with length %i\n color has been changed every %i particles'%(number_of_particles,layer_length,coloro_sampling))
    plt.xlabel('position of cells')
    plt.ylabel('height of cells')
    plt.show()


def analytical(layer_length,number_of_particles,number_of_ensembles): 
    mean_height=[]
    std=[]
    coherence_time=layer_length
    coherence_distance=[]
    
    
    for e in range(number_of_ensembles):
        coherence_distance_index=[]
        height=[0]*layer_length
        index=[]
        sampling_time=8
        coherence_time_temp=0
        k=0
        for i in range(0,number_of_particles):
            n=random.randint(0,layer_length-1)         
            if height[n]>=height[n-1] or height[n]>=height[(n+1)%layer_length]:    
                height[n]+=1
        
            else:
                max_height=max(height[n-1],height[(n+1)%layer_length])
                height[n]=max_height
                
            if i==sampling_time:
                mean_height.append(np.mean(height))
                std.append(np.std(height))
                index.append(sampling_time)
                sampling_time*=2
            
            coherence_time_temp+=1
            if coherence_time_temp==coherence_time:
                k+=1
                a=[x for x in height if x!=0]
                coherence_distance.append(len(a))
                coherence_distance_index.append(k*coherence_time)
                coherence_time_temp=0

        print('ensemble:%i'%e)
    mean_height=np.asarray(mean_height)
    mean_height=np.reshape(mean_height,(number_of_ensembles,len(index)))
    
    std=np.asarray(std)
    std=np.reshape(std,(number_of_ensembles,len(index)))

    coherence_distance=np.asarray(coherence_distance)
    coherence_distance=np.reshape(coherence_distance,(number_of_ensembles,len(coherence_distance_index)))

    return index,mean_height ,std,coherence_distance_index,coherence_distance
'''
main body:
'''
'''
1.Graphic Part:
'''
layer_length=800
number_of_particles=2**17
#graphic(layer_length,number_of_particles)

'''
2.Analytical Part:
'''
#layer_length=[25,50,100,200,400,800]
layer_length=800
number_of_particles=2**19
number_of_ensembles=10
fig,ax=plt.subplots()

index,height,std,d_index,d=analytical(layer_length,number_of_particles,number_of_ensembles)
mean_height=np.mean(height,axis=0) #calculate mean height
mean_std=np.mean(std,axis=0) #calculate mean standard deviation
std_error=np.std(std,axis=0) #error of standard deviations over ensembles

'''
take the log of variables:
'''
index_log=np.log10(index)
std_log=np.log10(mean_std)
#std_error_log=np.log10(std_error)
'''
fit line to linear section:
'''
partition=14

fit_line_index=index[:partition]

fit_line_index_log=index_log[:partition]
fit_line_std_log=std_log[:partition]
##############################################################
coeffs = np.polyfit(fit_line_index_log,fit_line_std_log,deg=1)
poly = np.poly1d(coeffs)
yfit = lambda index: 10**(poly(np.log10(fit_line_index)))
#plt.loglog(index,yfit(index),color="b")
#plt.loglog(index,std,'ro')
    
ax.errorbar(index,mean_std,yerr=std_error,ecolor='g',fmt='ro',markersize=2,capsize=2)
ax.plot(fit_line_index,yfit(fit_line_index),color='b')
ax.set_yscale('log')
ax.set_xscale('log')
    
plt.title("Roshd_e_Soozani\nlog-log plot of roughness versus time standard deviation for Kenar Neshast for a layer with length %i\n each point has been averaged over %i ensembles"%(layer_length,number_of_ensembles))
plt.xlabel("time")
plt.ylabel("roughness")
print(poly,'\n')
   
mean_co_d=np.mean(d,axis=0)
co_d_error=np.std(d,axis=0)
fig2,ax2=plt.subplots()
ax2.set_xlim([0,7000])
ax2.errorbar(d_index,mean_co_d,fmt="ro",yerr=co_d_error,markersize=3,ecolor='g',capsize=3)
plt.xlabel('time')
plt.ylabel('coherence distance')
plt.title("Coherence distance for Roshd_e_Soozani for a layer with length %i each point has been averaged over %i ensembles"%(layer_length,number_of_ensembles))
plt.show()
