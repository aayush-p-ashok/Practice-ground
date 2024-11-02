'''
Make an Interactive Electric Potential Plot of two charges q1 and q2
'''
#To run this, open jupyter lab from command terminal or use google collab
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive,FloatSlider,IntSlider
from IPython.display import display

def potential_plot(elev,azim,q1,q2,x1,y1,x2,y2):
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
    Vnet = V1 + V2

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
    # Calculating z-cordinate for zero potential
    zero_levels = ax.contour(x, y, Vnet, levels=[0],
                             colors='green', linewidths=2,
                             zdir='z', offset=Vnet.min())

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
    ax.view_init(elev=elev, azim=azim)  # Adjust viewing angle(polar and azimuthal angles)
    ax.dist = 8  # Adjust camera distance (lower number = closer)

    # Make axis limits slightly larger than data range
    ax.set_box_aspect([1, 1, 0.8])  # Adjust the box aspect ratio

    # Optional: If you want to adjust axis limits
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    # ax.set_zlim(Vnet.min(), Vnet.max())

    plt.show()

# Create interactive sliders
interactive_plot = interactive(potential_plot,
                             elev=IntSlider(min=-90, max=90, step=5, value=25),
                             azim=IntSlider(min=0, max=360, step=5, value=45),
                             q1=FloatSlider(min=-5, max=5, step=0.1, value=1, description='q1'),
                             q2=FloatSlider(min=-5, max=5, step=0.1, value=-2, description='q2'),
                             x1=FloatSlider(min=-5, max=5, step=0.1, value=0, description='x1'),
                             y1=FloatSlider(min=-5, max=5, step=0.1, value=0, description='y1'),
                             x2=FloatSlider(min=-5, max=5, step=0.1, value=3, description='x2'),
                             y2=FloatSlider(min=-5, max=5, step=0.1, value=0, description='y2'))
display(interactive_plot)