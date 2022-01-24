'''
Koch snowflake
EX-2
Fall 2021
Ali Setareh Kokab
'''
import matplotlib.pyplot as plt
import numpy as np
import math
import time
def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    """
    angle=np.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    
    return qx,qy

def fractal(start,end,order):
    
    l=end-start
    x=(start[0],end[0])
    y=(start[1],end[1]) 

    if order>0: 
       fractal(start,end-2/3*l,order-1)
       fractal(start+2/3*l,end,order-1)
       fractal(start+l/3,rotate(start+l/3,end-l/3,60),order-1)
       fractal(rotate(end-l/3,start+l/3,300),end-l/3,order-1)
    else:
        plt.plot(x,y,color="black")

start_point=np.asarray((1,3))
end_point=np.asarray((10,3))
order=5

for i in range(0,order+1):
    
    plt.cla()
    fractal(start_point,end_point,i)
    plt.title("Koch Snowflake\n order:%i"%i)
    plt.pause(1)
plt.show()
