import tkinter as tk
import subprocess
import os

# Define the list of Python files
python_files = ['electron_cloud_sim.py', 'electron_movement_3D_sim.py', 'probab_density_sim.py', 'tunnel_effect_sim.py',
                'vpython_electron_around_nucleus.py']


# Function to run a Python file in a new window
def run_file(fileName):
    # Open the file in a new terminal window
    # 'python' can be replaced with 'python3' depending on your system
    subprocess.Popen(['python', fileName])


# Create the main tkinter window
root = tk.Tk()
root.title("Quantum Mechanics Simulations")

# Create a button for each file
for file_name in python_files:
    if os.path.exists(file_name):
        btn = tk.Button(root, text=f"Run {file_name}", command=lambda f=file_name: run_file(f))
        btn.pack(pady=5)

# Run the tkinter main loop
root.mainloop()
