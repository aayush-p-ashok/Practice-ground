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
X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
x,y = np.meshgrid(X,Y)

V1 = potential(q1,x,y,x1,y1)
V2 = potential(q2,x,y,x2,y2)
Vnet = V1 + V2

#Plot 3D
plt.rcParams['figure.figsize'] = [15, 12]  # Increased figure size
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Plot the surface with colormap 'viridis'
surf = ax.plot_surface(x, y, Vnet, cmap='viridis', edgecolor='none',
                       antialiased=True,  # Smooth edges
                      rcount=100,        # Resampling for smoother look
                      ccount=100,        # Resampling for smoother look
                      alpha=0.9)

# Add a color bar with adjusted position
cbar = fig.colorbar(surf, ax=ax, shrink=0.7, aspect=10, pad=0.1, label='Potential V')

# Set labels with adjusted padding
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('Potential V', labelpad=10)
ax.set_title('3D Potential Due to Two Charges', pad=20, y=1.05)

# Adjust the viewing angle and distance
ax.view_init(elev=25, azim=45)  # Adjust viewing angle
ax.dist = 8  # Adjust camera distance (lower number = closer)

# Make axis limits slightly larger than data range
ax.set_box_aspect([1,1,0.8])  # Adjust the box aspect ratio

# Optional: If you want to adjust axis limits
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
#ax.set_zlim(Vnet.min(), Vnet.max())


plt.show()