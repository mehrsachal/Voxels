import numpy as np

def has_neighbor_on_top(voxel, voxel_array):
    """
    Given a voxel and an array of voxels, return True if any of the 4 neighbors
    of the voxel on the same z-axis has another voxel on top of it, and False otherwise.
    The voxel should be represented as a tuple of 3 values (x, y, z).
    The voxel_array should have shape (n, 3) where n is the number of voxels
    and 3 represents the x, y, and z coordinates for each voxel.
    """
    x, y, z = voxel
    
    neighbors = [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z),(x-1, y-1, z), (x-1, y+1, z), (x+1, y-1, z), (x+1, y+1, z)]

    for v in voxel_array:
        if voxel[0] == v[0] and voxel[1] == v[1] and voxel[2]+1 == v[2]:
            return True

    for neighbor in neighbors:
        
        for v in voxel_array:
            
            if neighbor[0] == v[0] and neighbor[1] == v[1] and neighbor[2]+1 == v[2]:
                
                return True

        
    return False




def get_voxels_with_neighbor_on_top(voxel_array):
    """
    Given an array of voxels, return a new array that contains only the voxels
    that have a neighbor with another voxel on top of it.
    The voxel_array should have shape (n, 3) where n is the number of voxels
    and 3 represents the x, y, and z coordinates for each voxel.
    """
    voxels_with_neighbor_on_top = []
    for voxel in voxel_array:
        if has_neighbor_on_top(voxel, voxel_array)==False:
            voxels_with_neighbor_on_top.append(voxel)
    return np.array(voxels_with_neighbor_on_top)
