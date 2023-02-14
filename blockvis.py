import openpyxl
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_blocks():
    # Load the block data from the Excel file
    wb = openpyxl.load_workbook('blocks.xlsx')
    ws = wb.active
    block_data = []
    for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True)):
        block_data.append(row[1:7])
    block_data = np.array(block_data)

    # Set the dimensions of the voxel grid
    x_min, y_min, z_min = block_data[:, :3].min(axis=0)
    x_max, y_max, z_max = block_data[:, :3].max(axis=0)
    size_x, size_y, size_z = block_data[:, 3:].max(axis=0)
    n, m, o = (x_max - x_min + size_x), (y_max - y_min + size_y), (z_max - z_min + size_z)

    # Create a 3D plot of the block data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(block_data.shape[0]):
        x, y, z, size_x, size_y, size_z = block_data[i,:]
        vertices = np.array([
            [x, y, z],
            [x+size_x, y, z],
            [x+size_x, y+size_y, z],
            [x, y+size_y, z],
            [x, y, z+size_z],
            [x+size_x, y, z+size_z],
            [x+size_x, y+size_y, z+size_z],
            [x, y+size_y, z+size_z],
        ])
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[3], vertices[0], vertices[4], vertices[7]],
            [vertices[4], vertices[5], vertices[6], vertices[7]]
        ]
        poly = Poly3DCollection(faces, alpha=1, facecolor='blue', edgecolor='black')
        ax.add_collection3d(poly)

    # Set the plot limits and labels
    ax.set_xlim([x_min, x_max + size_x])
    ax.set_ylim([y_min, y_max + size_y])
    ax.set_zlim([z_min, z_max + size_z])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    # Show the plot
    plt.show()
    return block_data
