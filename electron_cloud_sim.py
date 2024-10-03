import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# List of Bohr atoms (hydrogen-like atoms)
bohr_atoms = {
    "H": 1,  # Hydrogen
    "He+": 1,  # Helium ion with one electron
    "Li2+": 1,  # Lithium ion with one electron
    "Be3+": 1,  # Beryllium ion with one electron
    "C5+": 1  # Carbon ion with one electron
}


# Step 1: Check if the atom is a Bohr atom
def is_bohr_atom(atom):
    """Check if the given atom is a Bohr atom."""
    return atom in bohr_atoms


# Step 2: Function to simulate the electron cloud for a Bohr atom
def generate_electron_cloud(n_points=10000):
    """Generate a 3D electron cloud distribution."""
    # Randomly sample points in spherical coordinates
    r = np.random.exponential(scale=1.0, size=n_points)  # Radial distance (exponential distribution)
    theta = np.random.uniform(0, 2 * np.pi, n_points)  # Azimuthal angle (0 to 2pi)
    phi = np.random.uniform(0, np.pi, n_points)  # Polar angle (0 to pi)

    # Convert spherical to Cartesian coordinates for plotting
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z


# Step 3: Plot the electron cloud
def plot_electron_cloud(x, y, z):
    """Plot the electron cloud as a 3D scatter plot."""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot points using scatter with transparency to simulate cloud effect
    ax.scatter(x, y, z,  cmap='plasma', alpha=0.1, s=1)

    # Set axis limits and labels
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X (Bohr radii)')
    ax.set_ylabel('Y (Bohr radii)')
    ax.set_zlabel('Z (Bohr radii)')
    ax.set_title("Electron Cloud Simulation")

    plt.show()


# Step 4: Main function to handle user input and display the simulation
def main():
    # User input for atom
    atom = input("Enter the name of the atom or ion (e.g., H, He+, Li2+): ").strip()

    if is_bohr_atom(atom):
        print(f"{atom} is a Bohr atom. Simulating electron cloud...")

        # Generate the electron cloud
        x, y, z = generate_electron_cloud()

        # Plot the electron cloud
        plot_electron_cloud(x, y, z)

    else:
        print(f"{atom} is not a Bohr atom. No simulation available.")


# Run the main function
if __name__ == "__main__":
    main()