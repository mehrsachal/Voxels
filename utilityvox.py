import numpy as np
new_arr=np.array([])
def remove_voxel(voxel_array, n_on_top):
    for v in range(len(voxel_array)):
        t= str(voxel_array[v])
        for r in range(len(n_on_top)):
            tp = str(n_on_top[r])
            if t == tp:
                new_arr = np.delete(voxel_array, (v, r), axis=0)

        
    
    
    return new_arr