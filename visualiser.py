import openpyxl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



def plot_voxel():
    # Load the voxel data from the Excel file
    wb = openpyxl.load_workbook('pyramid_voxels.xlsx')
    ws = wb.active
    voxel_data = []
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0: # skip header row
            continue
        voxel_data.append(row[0:3])
    voxel_data = np.array(voxel_data)

    # Set the dimensions of the voxel grid
    n, o, _ = voxel_data.max(axis=0) + 1

    # Create a 3D plot of the voxel data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(n):
        for j in range(o):
            for k in range(o):
                if np.any(np.all(voxel_data == [i, j, k], axis=1)):
                    # Draw a cube with side length 1
                    x, y, z = j, i, k
                    face1 = [(x, y, z), (x+1, y, z), (x+1, y+1, z), (x, y+1, z)]
                    face2 = [(x, y, z), (x, y, z+1), (x, y+1, z+1), (x, y+1, z)]
                    face3 = [(x, y, z), (x, y+1, z), (x+1, y+1, z), (x+1, y, z)]
                    face4 = [(x+1, y, z), (x+1, y, z+1), (x+1, y+1, z+1), (x+1, y+1, z)]
                    face5 = [(x, y+1, z), (x, y+1, z+1), (x+1, y+1, z+1), (x+1, y+1, z)]
                    face6 = [(x, y, z+1), (x+1, y, z+1), (x+1, y+1, z+1), (x, y+1, z+1)]
                    ax.add_collection3d(Poly3DCollection([face1, face2, face3, face4, face5, face6], alpha=1, facecolor='blue'))

    # Set the plot limits and labels
    ax.set_xlim([-0.5, o-0.5])
    ax.set_ylim([-0.5, n-0.5])
    ax.set_zlim([-0.5, o-0.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.invert_yaxis()

    # Show the plot
    plt.show()

        


