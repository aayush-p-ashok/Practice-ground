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

#Potential function
def cont_potential(q,a,x,y,x0,y0):
    k = 9e9
    sigma = q/a
    integrand = lambda x, y: sigma/np.sqrt((x-x0)**2 + (y-y0)**2 + 1e-7 )#zero division error to be resolved
    x_range = np.sqrt(a/np.pi)
    V, _ = dblquad(integrand,-x_range,x_range,lambda y:-x_range,lambda x:-x_range)
    return k*V

X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
x,y = np.meshgrid(X,Y)

Vnet = cont_potential(q,a,x,y,x0,y0)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.plot_surface(x,y,np.log(Vnet))
ax.set_xlabel = ('x')
ax.set_ylabel = ('y')
ax.set_zlabel = (r'$\log(V)$')

plt.show()