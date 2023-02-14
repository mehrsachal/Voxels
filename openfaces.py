import numpy as np

def find_open_faces(voxels):
    """
    Finds the open faces in a plot of voxels.

    Parameters:
    voxels (numpy array): A 3D array of shape (n, m, o) containing binary values
    representing whether a voxel is present or not.

    Returns:
    open_faces (list of tuples): A list of tuples representing the open faces in
    the plot of voxels. Each tuple contains the x, y, and z coordinates of the
    voxel face.
    """
    open_faces = []

    # Pad the voxels with zeros so that we can easily detect the boundary voxels
    voxels_padded = np.pad(voxels, ((1, 1), (1, 1), (1, 1)), mode='constant')

    # Iterate over the boundary voxels
    for i in range(1, voxels_padded.shape[0] - 1):
        for j in range(1, voxels_padded.shape[1] - 1):
            for k in range(1, voxels_padded.shape[2] - 1):
                # Check if the current voxel is present
                if voxels_padded[i, j, k] == 1:
                    # Check if any of the neighbouring voxels are not present
                    if voxels_padded[i-1, j, k] == 0:
                        open_faces.append((i-1, j-1, k-1))
                    if voxels_padded[i+1, j, k] == 0:
                        open_faces.append((i, j-1, k-1))
                    if voxels_padded[i, j-1, k] == 0:
                        open_faces.append((i-1, j-1, k-1))
                    if voxels_padded[i, j+1, k] == 0:
                        open_faces.append((i-1, j, k-1))
                    if voxels_padded[i, j, k-1] == 0:
                        open_faces.append((i-1, j-1, k-1))
                    if voxels_padded[i, j, k+1] == 0:
                        open_faces.append((i-1, j-1, k))

    return open_faces
