from vpython import *
import random
import numpy as np

# Set up the display
scene = canvas(title="Schrödinger's Wave Equation: Electron around a Nucleus",
               width=800, height=600, center=vector(0, 0, 0), background=color.black)

# Nucleus (at the origin)
nucleus = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.red)


# Probability function for the electron wavefunction (Gaussian approximation)
def electron_probability(r):
    # Gaussian distribution for simplicity (not a real hydrogen atom wavefunction)
    sigma = 0.8
    return np.exp(-r ** 2 / (2 * sigma ** 2))


# Create particles to represent the electron cloud
num_particles = 80
particles = []

for i in range(num_particles):
    # Generate random spherical coordinates for the electron's position
    r = random.uniform(0, 3)  # Radial distance (adjust for visualization)
    theta = random.uniform(0, 2 * np.pi)  # Azimuthal angle
    phi = random.uniform(0, np.pi)  # Polar angle

    # Convert spherical coordinates to Cartesian coordinates
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    # Calculate probability and randomly decide to place a particle
    probability = electron_probability(r)

    if random.uniform(0, 1) < probability:
        particle = sphere(pos=vector(x, y, z), radius=0.05, color=color.blue, opacity=0.5)
        particles.append(particle)

# Add motion to the particles to simulate the electron cloud's "motion"
while True:
    rate(50)
    for particle in particles:
        # Random small movement for each particle (like diffusion)
        particle.pos.x += random.uniform(-0.05, 0.05)
        particle.pos.y += random.uniform(-0.05, 0.05)
        particle.pos.z += random.uniform(-0.05, 0.05)