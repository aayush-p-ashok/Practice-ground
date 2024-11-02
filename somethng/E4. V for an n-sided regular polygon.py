'''
Consider an n-sided regular polygon with charges of equal magnitude at vertices
1. Create a program that computes the position of each charge in the x-y plane.
2. Plot the electric potential due to collection of these charges.
'''
import numpy as np
import matplotlib.pyplot as plt

ex = 'y'
while ex=='y':
    q = float(input('Charge, q = '))

    # Considering the centre of the polygon to be the origin, take as input, the length of one side of the square
    s = float(input('Enter the length of a side of the polygon(in metre): '))
    n = int(input('Enter the no: of sides of the polygon: '))
    theta0 = np.pi/n
    # We find the average distance to each vertex, R = s/(2sin(theta0)
    R = s/(2 * np.sin(theta0))

    # Defining function of potential
    def potential(q, x, y, x0, y0):
        k = 9e9
        r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2 + 1e-9)  # The extra number added is to avoid zero division error
        return k * q / r

    # Creating 2D grid
    X = np.linspace(-5, 5, 500)
    Y = np.linspace(-5, 5, 500)
    x, y = np.meshgrid(X, Y)

    Xm = np.zeros(n)
    Ym = np.zeros(n)
    Vnet = 0

    for m in range(n):
        theta = 2 * m * theta0
        Xm[m] = R * np.cos(theta)
        Ym[m] = R * np.sin(theta)

    for m in range(n):
        Vnet += potential(q,x,y,Xm[m],Ym[m])

    epsilon = 1e-7  # small number to prevent log(0)
    Vplot = np.sign(Vnet) * np.log10(np.abs(Vnet) + epsilon)

    # Plot 3D
    plt.rcParams['figure.figsize'] = [15, 12]  # Increased figure size
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Plot the surface with colormap 'viridis'
    surf = ax.plot_surface(x, y, Vplot, cmap='magma', edgecolor='none',
                           antialiased=True,  # Smooth edges
                           rcount=100,  # Resampling for smoother look
                           ccount=100,  # Resampling for smoother look
                           alpha=0.9)

    # Add a zero potential contour
    zero_levels = ax.contour(x, y, Vplot, levels=[0],
                             colors='green', linewidths=2,
                             zdir='z', offset=Vnet.min())  # Projection of zero potential line onto x-y plane

    # Plot the actual 3D contour where potential is zero
    ax.contour3D(x, y, Vplot, levels=[0],
                 colors='#00FFFF', linewidths=2)

    # Add a color bar with adjusted position
    cbar = fig.colorbar(surf, ax=ax, shrink=0.7, aspect=10, pad=0.1, label=r'$\log(V)$')

    # Set labels with adjusted padding
    ax.set_xlabel('x', labelpad=10)
    ax.set_ylabel('y', labelpad=10)
    ax.set_zlabel(r'$\log(V)$', labelpad=10)
    ax.set_title('3D Potential Due to Two Charges', pad=20, y=1.05)

    # Adjust the viewing angle and distance
    ax.view_init(elev=45, azim=45)  # Adjust viewing angle(polar and azimuthal angles)
    ax.dist = 8  # Adjust camera distance (lower number = closer)

    # Make axis limits slightly larger than data range
    ax.set_box_aspect([1, 1, 0.8])  # Adjust the box aspect ratio

    # Optional: If you want to adjust axis limits
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    # ax.set_zlim(Vnet.min(), Vnet.max())

    plt.show()
    print('Do you want to redo?')
    ex = input('Enter y to redo and x to exit: ')

