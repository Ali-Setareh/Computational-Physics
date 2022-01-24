'''
Sierpiński triangle
EX-2
Fall 2021
Ali Setareh Kokab
'''
import matplotlib.pyplot as plt
import numpy as np
def draw_triangle(a,b,c): #function to draw a rectangle with 3 given points 
  coord = [a,b,c]
  coord.append(coord[0]) #repeat the first point to create a 'closed loop'
  xs, ys = zip(*coord) #create lists of x and y values
  #plt.figure()
  #plt.plot(xs,ys,color="black") 
  plt.fill(xs,ys,color="black")

def fractal(a,b,c,order):
  d1=b-a
  d2=c-a
  d3=b-c
  if order>0:
    fractal(a,b-d1/2,c-d2/2,order-1)
    fractal(a+d1/2,b,c+d3/2,order-1)
    fractal(a+d2/2,b-d3/2,c,order-1)
  else:
    draw_triangle(a,b,c)
    

coord = [[1,1], [3,5], [5,1]]
coord=np.array(coord)
order=7
for i in range (order+1):
  plt.cla()
  fractal(coord[0],coord[1],coord[2],i)
  plt.title("Sierpiński triangle\n order:%i"%i)
  plt.pause(1)
  
plt.show()