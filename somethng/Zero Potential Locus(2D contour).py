'''Qn
Consider two point charges, q1 = +1 C located at position (0, 0) and q2 = -2 C located at (3, 0), in the xy-plane.
The electric potential V at any point P(x, y) in space due to a charge q is given by:

    V = (k * q) / r

where k is Coulomb’s constant and r is the distance from the point charge to P(x, y).

Tasks:
1. Write a function to compute the electric potential V at any point P(x, y) due to a point charge q located
at (x0, y0).

2. Calculate and plot the electric potential due to both charges at points in a grid across the xy-plane.
Use a suitable range for x and y (e.g., from -5 to 5) with sufficient resolution.

3. Identify and plot the locus of points where the net electric potential V_net due to both charges is zero.
This locus represents the curve along which the potential is zero.
'''

import numpy as np
import matplotlib.pyplot as plt

#Define charges and their postions
q1 = 1
q2 = -2
x1,y1 = 0,0 #Position of q1
x2,y2 = 3,0 #Position of q2

#Defining function of potential
def potential(q,x,y,x0,y0):
    k = 9e9
    r = np.sqrt((x-x0)**2 + (y-y0)**2 + 1e-9) #The extra number added is to avoid zero division error
    return k*q/r

#Creating 2D grid
X = np.linspace(-5,5,50)
Y = np.linspace(-5,5,50)
x,y = np.meshgrid(X,Y)

V1 = potential(q1,x,y,x1,y1)
V2 = potential(q2,x,y,x2,y2)
Vnet = V1 + V2

#Plotting the charges and potential contours
plt.contourf(x, y, Vnet, levels=200)
plt.colorbar(label='Potential $V$')
plt.scatter([x1,x2],[y1,y2],s=10,color=['blue','red'])

#Plotting zero potential locus
zeroline = plt.contour(x, y, Vnet, levels=[0], colors='maroon', linestyles='--', linewidths=2)

#Now creating some fake ones to put in the legend(They won't appear in plot because they have no coordinates)
q1proxy = plt.Line2D([],[],color='blue', marker='o',linestyle='None', markersize=10, label=f'q1= {q1} C')
q2proxy = plt.Line2D([],[],color='red', marker='o',linestyle='None', markersize=10, label=f'q2= {q2}C' )
zero_line_proxy = plt.Line2D([], [], color='maroon', linestyle='--', linewidth=2, label='Zero Potential Locus')

plt.legend(handles=[q1proxy,q2proxy,zero_line_proxy])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Potential Due to Two Charges')
plt.gca().set_aspect('equal',adjustable='box')
plt.grid(True)

plt.show()