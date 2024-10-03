import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

# Constants
hbar = 1.0  # Reduced Planck's constant (in arbitrary units)
m = 1.0     # Mass (in arbitrary units)
L = 10.0    # Length of the system (arbitrary units)
N = 1000    # Number of points in space
a = L / N   # Discretization step

# Potential barrier
V0 = 5.0    # Barrier height
x = np.linspace(0, L, N)
V = np.zeros_like(x)
V[int(0.4*N):int(0.6*N)] = V0  # Set the potential barrier in the middle

# Hamiltonian matrix in finite difference form
diag = np.ones(N) * (2.0 * hbar**2 / (m * a**2)) + V
off_diag = np.ones(N-1) * (-hbar**2 / (m * a**2))

# Solving for eigenvalues and eigenvectors (numerically solves the Schrödinger equation)
eigenvalues, eigenvectors = eigh_tridiagonal(diag, off_diag)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, eigenvectors[:, 0]**2, label="Ground State Probability")
plt.plot(x, eigenvectors[:, 1]**2, label="1st Excited State Probability")
plt.plot(x, V/V0, label="Potential Barrier", linestyle='--')
plt.xlabel('Position (arbitrary units)')
plt.ylabel('Probability Density')
plt.legend()
plt.title("Quantum Tunneling through a Potential Barrier")
plt.show()