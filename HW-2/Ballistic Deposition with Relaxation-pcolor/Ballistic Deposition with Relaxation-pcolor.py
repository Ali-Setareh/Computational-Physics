'''
Ballistic Deposition with Relaxation
EX-2
Fall 2021
Ali Setareh Kokab
'''
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c
import statistics

'''
funcetions:
'''
def graphic(layer_length,number_of_particles):

    Z=np.zeros([number_of_particles,layer_length],dtype=float) #matix in which we save position of on/off pixels
    height=[0]*layer_length # A list which contains height of each box 
    
    change_color=[1,2] #to change color for every 2000 particles
    X=np.repeat([np.arange(layer_length+1)],np.shape(Z)[0]+1,0) # X cooridiante for pcolormesh grid
    Y=np.transpose(np.repeat([np.arange(np.shape(Z)[0]+1)],layer_length+1,0)) # Y cooridiante for pcolormesh grid
    color_control=0 
    cMap = c.ListedColormap(['w','r','b']) #colors that we use in pcolormesh
    temp=0
    coloro_sampling=10*layer_length
   
    for i in range(0,number_of_particles):
        n=random.randint(0,layer_length-1) # A random number
        if height[n-1]<=height[(n+1)%layer_length] and height[n-1]<height[n]:
            height[n-1]+=1
            Z[height[n-1],n-1]=change_color[color_control]
               
        elif height[(n+1)%layer_length]<=height[n-1] and height[(n+1)%layer_length]<height[n]:
            #min_height=random.choice([n-1,(n+1)%layer_length])
            height[(n+1)%layer_length]+=1
            Z[height[(n+1)%layer_length],(n+1)%layer_length]=change_color[color_control]
                
        else:
            #min_height=height.index(min(height[n-1],height[(n+1)%layer_length]))
            height[n]+=1
            Z[height[n],n]=change_color[color_control]
        temp+=1
        if temp==coloro_sampling: #change color:
            color_control+=1
            color_control=color_control%2
            temp=0
    Z=Z[~np.all(Z == 0, axis=1)]
    X=np.repeat([np.arange(layer_length+1)],np.shape(Z)[0]+1,0)
    Y=np.transpose(np.repeat([np.arange(np.shape(Z)[0]+1)],layer_length+1,0))
    plt.pcolormesh(X,Y,Z,cmap=cMap)
    plt.title('Ballistic Decomposition with Relaxations for %i particles and a layer with length %i\n color has been changed every %i particles'%(number_of_particles,layer_length,coloro_sampling))
    plt.xlabel('position of cells')
    plt.ylabel('height of cells')
    plt.show()


def analytical(layer_length,number_of_particles,number_of_ensembles): 
    mean_height=[]
    std=[]
    for e in range(number_of_ensembles):
        height=[0]*layer_length
        index=[]
        sampling_time=8
        for i in range(0,number_of_particles):
            n=random.randint(0,layer_length-1)         
            if height[n-1]<=height[(n+1)%layer_length] and height[n-1]<height[n]:
                height[n-1]+=1
               
            elif height[(n+1)%layer_length]<=height[n-1] and height[(n+1)%layer_length]<height[n]:
                height[(n+1)%layer_length]+=1
                
            else:
                height[n]+=1
                
            if i==sampling_time:
                mean_height.append(np.mean(height))
                std.append(np.std(height))
                index.append(sampling_time)
                sampling_time*=2 #to plot mean height change this to sampling_time+=3000
        print("ensemble:%i"%e)
    mean_height=np.asarray(mean_height)
    mean_height=np.reshape(mean_height,(number_of_ensembles,len(index)))
    
    std=np.asarray(std)
    std=np.reshape(std,(number_of_ensembles,len(index)))

    return index,mean_height ,std
'''
main body:
'''
'''
1.Graphic Part:
'''
layer_length=200
number_of_particles=2**17
#graphic(layer_length,number_of_particles) #graphic output!!!!!!!!!!!!!!!!!!!

beta=[]
for i in range(0,1): #this loop is for averaging over betas so change the range to average beta over your disered number of times
    '''
    2.Analytical Part:
    '''
    
    layer_length=200
    number_of_ensembles=10
    fig,ax=plt.subplots()
    index,height,std=analytical(layer_length,number_of_particles,number_of_ensembles)
    mean_height=np.mean(height,axis=0) #calculate mean height
    mean_height_error=np.std(height,axis=0) #mean height error
    mean_std=np.mean(std,axis=0) #calculate mean standard deviation
    std_error=np.std(std,axis=0) #error of standard deviations over ensembles

    '''
    plot mean height
    '''
    fig2,ax2=plt.subplots()
    ax2.errorbar(index,mean_height,yerr=mean_height_error,ecolor='g',fmt='ro',markersize=2,capsize=2)
    ax2.plot(index,mean_height)
    plt.xlabel("time (number of particels)")
    plt.ylabel("mean height")
    plt.title("mean height versus time for Ballistic Deposition with Relaxation\n the length of the layer is %i and each point has been averaged over %i enseble"%(layer_length,number_of_ensembles))
    coeffs2 = np.polyfit(index,mean_height,deg=1)
    plt.show()
    '''
    take the log of variables:
    '''
    index_log=np.log10(index)
    std_log=np.log10(mean_std)
    '''
    fit line for linear section before saturation:
    '''
    partition_time={25:6,50:8,100:11,200:15,400:18,800:20}
    partition=partition_time[layer_length]

    fit_line_index=index[:partition]

    fit_line_index_log=index_log[:partition]
    fit_line_std_log=std_log[:partition]
    fit_line_std=mean_std[:partition]

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
    
    plt.title("Ballistic Deposition with Relaxation\nlog-log plot of roughness versus time for a layer with length %i\n each point has been averaged over %i ensembles"%(layer_length,number_of_ensembles))
    plt.xlabel("log(t)")
    plt.ylabel("log(w)")
    #print(poly,'\n')
    beta.append(poly[1])
#print(beta)
print('beta:%f'%statistics.mean(beta))
print('beta std:%f'%statistics.stdev(beta))
plt.show()
