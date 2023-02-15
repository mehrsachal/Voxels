import numpy as np

def list_voxel_faces(voxel_array):
    """
    Given an array of voxels, return a list of all the faces of the voxels
    and a dictionary that maps each voxel to the number of open faces,
    excluding the bottom face of voxels in the bottom.
    The voxel_array should have shape (n, 6) where n is the number of voxels
    and 6 represents the x, y, z coordinates and size of each voxel.
    """
    voxel_set = set(tuple(v) for v in voxel_array)
    faces = []
    open_face_count = {}
    for voxel in voxel_set:
        x, y, z, s, d, f = voxel
        open_faces = 0
        for i in range(-s, s+1):
            if (x+i, y, z) not in voxel_set:
                faces.append([(x+i, y, z), (x+i, y+d, z), (x+i, y+d, z+f), (x+i, y, z+f)])
                open_faces += 1
        for j in range(-d, d+1):
            if (x, y+j, z) not in voxel_set:
                faces.append([(x, y+j, z), (x+s, y+j, z), (x+s, y+j, z+f), (x, y+j, z+f)])
                open_faces += 1
        for k in range(-f, f+1):
            if (x, y, z+k) not in voxel_set and z+k >= 0:
                faces.append([(x, y, z+k), (x+s, y, z+k), (x+s, y+d, z+k), (x, y+d, z+k)])
                open_faces += 1
        open_face_count[voxel] = open_faces
    return faces, open_face_count
