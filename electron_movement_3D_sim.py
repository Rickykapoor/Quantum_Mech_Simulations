import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

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


# Step 2: Function to simulate the movement of an electron in a 3D orbital
def simulate_electron_movement():
    # Define spherical coordinates
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 50)

    # Create meshgrid for spherical coordinates
    theta, phi = np.meshgrid(theta, phi)

    # Assume constant radius for simplicity (in Bohr radii)
    r = 1

    # Convert spherical coordinates to Cartesian
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z


# Step 3: Animation function for electron movement
def animate(i, ax, x, y, z):
    """Update the electron's position for animation."""
    ax.clear()

    # Change electron's position slightly to simulate movement
    new_x = x * np.cos(i * 0.1)
    new_y = y * np.sin(i * 0.1)

    # Plot the electron movement with updated positions
    ax.plot_surface(new_x, new_y, z, color='b', alpha=0.6, rstride=5, cstride=5)
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Electron Movement in Atomic Orbital")


# Step 4: Main function to handle user input and display the simulation
def main():
    # User input for atom
    atom = input("Enter the name of the atom or ion (e.g., H, He+, Li2+): ").strip()

    if is_bohr_atom(atom):
        print(f"{atom} is a Bohr atom. Simulating electron movement...")

        # Set up the figure for 3D plot
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Generate the electron's movement
        x, y, z = simulate_electron_movement()

        # Create the animation
        ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(ax, x, y, z), interval=100)

        # Show the animation
        plt.show()

    else:
        print(f"{atom} is not a Bohr atom. No simulation available.")


# Run the main function
if __name__ == "__main__":
    main()