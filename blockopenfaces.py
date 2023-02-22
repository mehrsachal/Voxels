import numpy as np

def get_voxel_faces(voxels):
    """
    Returns a dictionary containing the faces of each voxel.

    Parameters:
    voxels (np.ndarray): numpy array of shape (n, 6) representing the voxels

    Returns:
    dict: a dictionary where the keys are the indices of the voxels and the
    values are lists of tuples representing the faces of the voxel, where
    each tuple contains the x, y, z coordinates of the face and the normal vector
    of the face (in the form of a tuple of three integers, where each integer
    represents the direction of the normal vector in the x, y, and z directions).
    """

    voxel_faces = {}

    for i, voxel in enumerate(voxels):
        x, y, z, size_x, size_y, size_z = voxel
        faces = []

        # Front face
        faces.append(((x, y, z), (0, 0, 1)))
        faces.append(((x + size_x, y, z), (0, 0, 1)))
        faces.append(((x + size_x, y + size_y, z), (0, 0, 1)))
        faces.append(((x, y + size_y, z), (0, 0, 1)))

        # Back face
        faces.append(((x, y, z + size_z), (0, 0, -1)))
        faces.append(((x + size_x, y, z + size_z), (0, 0, -1)))
        faces.append(((x + size_x, y + size_y, z + size_z), (0, 0, -1)))
        faces.append(((x, y + size_y, z + size_z), (0, 0, -1)))

        # Top face
        faces.append(((x, y + size_y, z), (0, 1, 0)))
        faces.append(((x + size_x, y + size_y, z), (0, 1, 0)))
        faces.append(((x + size_x, y + size_y, z + size_z), (0, 1, 0)))
        faces.append(((x, y + size_y, z + size_z), (0, 1, 0)))

        # Bottom face
        faces.append(((x, y, z), (0, -1, 0)))
        faces.append(((x + size_x, y, z), (0, -1, 0)))
        faces.append(((x + size_x, y, z + size_z), (0, -1, 0)))
        faces.append(((x, y, z + size_z), (0, -1, 0)))

        # Left face
        faces.append(((x, y, z), (-1, 0, 0)))
        faces.append(((x, y, z + size_z), (-1, 0, 0)))
        faces.append(((x, y + size_y, z + size_z), (-1, 0, 0)))
        faces.append(((x, y + size_y, z), (-1, 0, 0)))

                # Right face
        faces.append(((x + size_x, y, z), (1, 0, 0)))
        faces.append(((x + size_x, y, z + size_z), (1, 0, 0)))
        faces.append(((x + size_x, y + size_y, z + size_z), (1, 0, 0)))
        faces.append(((x + size_x, y + size_y, z), (1, 0, 0)))

        voxel_faces[i] = faces

    return voxel_faces

def count_shared_faces(faces, voxel_array):
    """
    Counts the number of shared faces between neighboring voxels.

    Parameters:
    faces (dict): a dictionary where the keys are the indices of the voxels
    and the values are lists of tuples representing the faces of the corresponding voxel.
    voxel_array (np.ndarray): numpy array of shape (n, 6) representing the voxels

    Returns:
    dict: a dictionary where the keys are tuples representing pairs of neighboring
    voxels, and the values are integers representing the number of shared faces
    between the two voxels.
    """

    shared_faces = {}

    for i, voxel_faces_i in faces.items():
        x_i, y_i, z_i, size_x_i, size_y_i, size_z_i = voxel_array[i]
        for j in range(i+1, len(faces)):
            voxel_faces_j = faces[j]
            x_j, y_j, z_j, size_x_j, size_y_j, size_z_j = voxel_array[j]
            shared = 0
            for face_i in voxel_faces_i:
                for face_j in voxel_faces_j:
                    if face_i == face_j:
                        # Check if the faces are adjacent
                        x_diff = x_i - x_j
                        y_diff = y_i - y_j
                        z_diff = z_i - z_j
                        if abs(x_diff) == size_x_i and abs(y_diff) < size_y_i and abs(z_diff) < size_z_i:
                            shared += 1
                        elif abs(y_diff) == size_y_i and abs(x_diff) < size_x_i and abs(z_diff) < size_z_i:
                            shared += 1
                        elif abs(z_diff) == size_z_i and abs(x_diff) < size_x_i and abs(y_diff) < size_y_i:
                            shared += 1
            if shared > 0:
                shared_faces[(i, j)] = shared

    return shared_faces
