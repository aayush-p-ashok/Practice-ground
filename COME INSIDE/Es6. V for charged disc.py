'''
Create a potential plot for a charged disc.
'''
#The key change is we have to find a way to plot the potential of a continous charge

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

#Define charges and their positions
q = float(input('Charge, q = '))
a = float(input('Area of the disc,a = '))
x0,y0 = 0,0


# Potential function for a single point
def single_point_potential(q, a, x, y, x0, y0):
    k = 9e9
    sigma = q / a
    epsilon = 1e-10  # Small value to avoid division by zero
    integrand = lambda x_prime, y_prime: sigma / np.sqrt((x - x_prime) ** 2 + (y - y_prime) ** 2 + epsilon)
    x_range = np.sqrt(a / np.pi)
    V, _ = dblquad(integrand, -x_range, x_range,
                   lambda x: -x_range,
                   lambda x: x_range)
    return k * V


# Potential array function
def cont_potential(q, a, x, y, x0, y0):
    V = np.zeros_like(x)  # Create output array with same shape as x
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            # Calculate potential for each point individually
            V[i, j] = single_point_potential(q, a, x[i, j], y[i, j], x0, y0)
    return V

X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
x,y = np.meshgrid(X,Y)

Vnet = cont_potential(q,a,x,y,x0,y0)

plt.rcParams['figure.figsize'] = [15, 12]  # Increased figure size
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with colormap 'viridis'
surf = ax.plot_surface(x, y, Vnet, cmap='magma', edgecolor='none', )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Potential V')
ax.set_title('3D Potential Due to Two Charges', pad=20, y=1.05)

plt.show()