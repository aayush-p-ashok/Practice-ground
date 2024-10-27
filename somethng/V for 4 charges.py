'''
Consider four charges q1, q2, q3 and q4 placed at four corners of a square.
1. Find the electric potential at the centre of the square.
2. Plot the potential field against x-y plane.
'''
import numpy as np
import matplotlib.pyplot as plt

ex = 'y'
while ex=='y':
    # Define charges
    q1 = float(input('Charge of q1= '))
    q2 = float(input('Charge of q2= '))
    q3 = float(input('Charge of q3= '))
    q4 = float(input('Charge of q4= '))

    # Considering the centre of the square to be the origin, take as input, the length of one side of the square
    s = float(input('Enter the length of the square(in metre): '))

    x1, y1 = s / 2, s / 2  # Position of q1
    x2, y2 = -s / 2, s / 2  # Position of q2
    x3, y3 = -s / 2, -s / 2  # Position of q3
    x4, y4 = s / 2, -s / 2  # Position of q3


    # Defining function of potential
    def potential(q, x, y, x0, y0):
        k = 9e9
        r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2 + 1e-9)  # The extra number added is to avoid zero division error
        return k * q / r


    # Creating 2D grid
    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(X, Y)

    V1 = potential(q1, x, y, x1, y1)
    V2 = potential(q2, x, y, x2, y2)
    V3 = potential(q3, x, y, x3, y3)
    V4 = potential(q4, x, y, x4, y4)
    Vnet = V1 + V2 + V3 + V4

    # Plot 3D
    plt.rcParams['figure.figsize'] = [15, 12]  # Increased figure size
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Plot the surface with colormap 'viridis'
    surf = ax.plot_surface(x, y, Vnet, cmap='magma', edgecolor='none',
                           antialiased=True,  # Smooth edges
                           rcount=100,  # Resampling for smoother look
                           ccount=100,  # Resampling for smoother look
                           alpha=0.9)

    # Add a zero potential contour
    zero_levels = ax.contour(x, y, Vnet, levels=[0],
                             colors='green', linewidths=2,
                             zdir='z', offset=Vnet.min())  # Projection of zero potential line onto x-y plane

    # Plot the actual 3D contour where potential is zero
    ax.contour3D(x, y, Vnet, levels=[0],
                 colors='#00FFFF', linewidths=2)

    # Add a color bar with adjusted position
    cbar = fig.colorbar(surf, ax=ax, shrink=0.7, aspect=10, pad=0.1, label='Potential V')

    # Set labels with adjusted padding
    ax.set_xlabel('x', labelpad=10)
    ax.set_ylabel('y', labelpad=10)
    ax.set_zlabel('Potential V', labelpad=10)
    ax.set_title('3D Potential Due to Two Charges', pad=20, y=1.05)

    # Adjust the viewing angle and distance
    ax.view_init(elev=0, azim=90)  # Adjust viewing angle(polar and azimuthal angles)
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

