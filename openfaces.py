import numpy as np

def list_voxel_faces(voxel_array):
    """
    Given an array of voxels, return a list of all the faces of the voxels.
    The voxel_array should have shape (n, 3) where n is the number of voxels
    and 3 represents the x, y, and z coordinates for each voxel.
    """
    voxel_set = set(tuple(v) for v in voxel_array)
    faces = []
    for voxel in voxel_set:
        x, y, z = voxel
        if (x-1, y, z) not in voxel_set:
            faces.append([(x, y, z), (x, y+1, z), (x, y+1, z+1), (x, y, z+1)])
        if (x+1, y, z) not in voxel_set:
            faces.append([(x+1, y, z), (x+1, y+1, z), (x+1, y+1, z+1), (x+1, y, z+1)])
        if (x, y-1, z) not in voxel_set:
            faces.append([(x, y, z), (x+1, y, z), (x+1, y, z+1), (x, y, z+1)])
        if (x, y+1, z) not in voxel_set:
            faces.append([(x, y+1, z), (x+1, y+1, z), (x+1, y+1, z+1), (x, y+1, z+1)])
        if (x, y, z-1) not in voxel_set:
            faces.append([(x, y, z), (x+1, y, z), (x+1, y+1, z), (x, y+1, z)])
        if (x, y, z+1) not in voxel_set:
            faces.append([(x, y, z+1), (x+1, y, z+1), (x+1, y+1, z+1), (x, y+1, z+1)])
    return faces


