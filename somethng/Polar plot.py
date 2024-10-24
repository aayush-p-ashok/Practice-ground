#install the libraries
import numpy as np
import matplotlib.pyplot as plt

#Practice Problem: 2

theta = np.linspace(0,2*np.pi,1000)
r = 1 + np.sin(5*theta)*3/4
x = r * np.cos(theta)
y = r * np.sin(theta)
#Calculate area
A = 1/2 * sum(r**2) * (theta[1] - theta[0])
print(f'Area of the flower: {A:.4}')
#Calculate arclength
L = sum(np.sqrt(r**2 + (np.gradient(r,theta))**2)) * (theta[1] - theta[0])
print(f'Perimeter of the petals: {L:.5}')

# Add darker X and Y axes
plt.axhline(0, color='black', linewidth=1)  # X-axis
plt.axvline(0, color='black', linewidth=1)  # Y-axis

plt.plot(x,y, color='red', linewidth=1.5, linestyle='-')
plt.ylabel("y")
plt.xlabel("x")
plt.gca().set_aspect('equal', adjustable='box')
plt.title(r'Polar Plot of $r(\theta) = 1 + \frac{3}{4} \sin(3\theta)$')
plt.grid(True)
plt.show()

# Create a polar plot(Suggested by Chatgpt)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, color='blue', linewidth=2)# Plot the curve in polar coordinates
ax.set_title(r'Polar Plot of $r(\theta) = 1 + \frac{3}{4} \sin(3\theta)$', va='bottom')
ax.tick_params(axis='both', which='both', labelsize=6)  # Adjust 'labelsize' to make text smaller
ax.grid(True)
plt.show()