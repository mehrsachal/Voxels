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
        plotter.add_mesh(box, color='red', opacity=0.5)

    # Show the plotter
    plotter.show()

