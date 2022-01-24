'''
Sierpiński triangle-Stochastic Algorithm
EX-2
Fall 2021
Ali Setareh Kokab
'''
import matplotlib.pyplot as plt
import numpy as np
import random

def draw_triangle(a,b,c,color):
  coord = [a,b,c]
  coord.append(coord[0]) #repeat the first point to create a 'closed loop'
  xs, ys = zip(*coord) #create lists of x and y values
  #plt.figure()
  #plt.plot(xs,ys,color="black") 
  plt.fill(xs,ys,color=color)

def fractal(a,b,c,order):
  d1=b-a
  d2=c-a
  d3=b-c
  n=random.randint(1,3)
  if order>0:
      if n==1:
        fractal(a,b-d1/2,c-d2/2,order-1)
      elif n==2:  
        fractal(a+d1/2,b,c+d3/2,order-1)
      elif n==3:  
        fractal(a+d2/2,b-d3/2,c,order-1)
  else:
       draw_triangle(a,b,c,"white")

coord = [[1,1], [3,5], [5,1]]
coord=np.array(coord)
order=7
itterations=3000
draw_triangle(coord[0],coord[1],coord[2],"black")
for i in range (itterations+1):
    fractal(coord[0],coord[1],coord[2],order)
    plt.title("Stochastic Sierpiński triangle order %s for %s itterations \n Level:%i"%(order,itterations,i))
    plt.pause(0.05)
plt.show()