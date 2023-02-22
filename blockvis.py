import numpy as np
import pyvista as pv



def blockvis(coordinates, sizes):
    # Create a PyVista plotter
    plotter = pv.Plotter()

    # Loop over all voxels
    for i in range(len(coordinates)):
        # Get the coordinates and sizes of the current voxel
        x, y, z = coordinates[i]
        sx, sy, sz = sizes[i]

        # Create a box for the current voxel
        box = pv.Box(bounds=(x, x+sx, y, y+sy, z, z+sz))

        # Add the box to the plotter
        plotter.add_mesh(box, color='red', opacity=1)

    # Show the plotter
    plotter.show()

def voxelvis(coordinates, sizes,colors):
    # Create a PyVista plotter
    plotter = pv.Plotter()

    # Loop over all voxels
    for i in range(len(coordinates)):
        # Get the coordinates and sizes of the current voxel
        x, y, z = coordinates[i]
        sx, sy, sz = sizes[i]

        # Create a box for the current voxel
        box = pv.Box(bounds=(x, x+sx, y, y+sy, z, z+sz))

        # Add the box to the plotter
        plotter.add_mesh(box, color=colors[i], opacity=1)

    # Show the plotter
    plotter.show()

import random

def generate_color():
    # Generate a random color using pyVista's Color() function
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return pv.Color([r, g, b])

def generate_color_list(n):
    # Generate a list of unique colors
    colors = []
    for i in range(n):
        if i % 10 == 0:
            # Generate a new color after every 10 values
            color = generate_color()
            while color in colors:
                # Make sure the new color is unique
                color = generate_color()
            colors.append(color)
        else:
            # Reuse the previous color
            colors.append(colors[-1])
    return colors