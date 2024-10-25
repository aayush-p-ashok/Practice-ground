'''Qn
Consider two point charges, q1 = +1 C located at position (0, 0) and q2 = -2 C located at (3, 0), in the xy-plane.
The electric potential V at any point P(x, y) in space due to a charge q is given by:

    V = (k * q) / r

where k is Coulomb’s constant and r is the distance from the point charge to P(x, y).

Tasks:
1. Write a function to compute the electric potential V at any point P(x, y) due to a point charge q located
at (x0, y0).

2. Create a 3D plot of the Electric Potential against x and y axes
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
# Plot the 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with colormap 'viridis'
surf = ax.plot_surface(X, Y, Vnet, cmap='viridis', edgecolor='none')

# Add a color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Potential V')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Potential V')
ax.set_title('3D Potential Due to Two Charges')


plt.show()