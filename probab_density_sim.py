import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from scipy.constants import pi


# Step 1: Define the Radial Wave function for the 2p Orbital of Lithium
def R_2p(r, Z=3):
    a0 = 1  # In atomic units
    return (1 / (4 * np.sqrt(6))) * (r / a0) * np.exp(-Z * r / (2 * a0))  # Z=3 for lithium


# Step 2: Define the Angular part of the 2p_z Orbital (Spherical Harmonics)
def Y_10(theta):
    return np.cos(theta) / np.sqrt(4 * pi)


# Step 3: Calculate the total wave function for the 2p_z orbital
def psi_2p_z(r, theta, Z=3):
    return (R_2p(r, Z) * Y_10(theta)) ** 2


# Step 4: Generate a grid of points in spherical coordinates
r = np.linspace(0, 20, 200)  # Radial distance from nucleus (in Bohr radii)
theta = np.linspace(0, pi, 200)  # Polar angle
R, Theta = np.meshgrid(r, theta)  # Create a grid of r and theta values

# Step 5: Compute the probability density |psi|^2
prob_density = psi_2p_z(R, Theta)

# Step 6: Convert spherical to Cartesian coordinates for plotting
X = R * np.sin(Theta)  # x = r*sin(theta)
Y = R * np.cos(Theta)  # y = r*cos(theta)

# Step 7: Set up the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Initial plot setup
surf = ax.plot_surface(X, Y, prob_density, cmap='inferno', edgecolor='none')

# Customize the plot (titles and labels)
ax.set_title(r'Probability Density of Electron in $2p_z$ Orbital of Lithium')
ax.set_xlabel(r'$x$ (Bohr radii)')
ax.set_ylabel(r'$y$ (Bohr radii)')
ax.set_zlabel(r'$|psi|^2$')
fig.colorbar(surf, ax=ax, label='Probability Density')  # Add a color bar


# Step 8: Animation function
def animate(i):
    """Update the plot for each frame."""
    ax.clear()  # Clear the previous frame
    # Recompute the probability density (changing phase over time for animation)
    prob_density_time = psi_2p_z(R, Theta) * (np.sin(i * 0.1) + 1.5)  # Varying function over time
    # Update surface plot with a new color map (change color gradually with time)
    surf = ax.plot_surface(X, Y, prob_density_time, cmap=plt.cm.plasma, edgecolor='none')

    # Customize the plot for each frame
    ax.set_title(f"Probability Density of Electron in $2p_z$ Orbital (Frame {i})")
    ax.set_xlabel(r'$x$ (Bohr radii)')
    ax.set_ylabel(r'$y$ (Bohr radii)')
    ax.set_zlabel(r'$|psi|^2$')

    return surf,


# Step 9: Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=False)

# Step 10: Show the animated plot
plt.show()