import blockvis
import newapp
import nfinder
import numpy as np

#File Initialization
file_name = 'blocks.xlsx'
coordinates, sizes = newapp.excel_to_arrays(file_name)
path=[]


while len(coordinates)>0:
    mask = np.ones(len(coordinates), dtype=bool)



    #blockvis.blockvis(coordinates, sizes)
    neighbors = nfinder.count_neighbors(coordinates, sizes)

    #identifies double benchers
    for i in range(len(coordinates)):
        for j in range(len(neighbors[i])):
            voxelid = neighbors[i][j]
            val = coordinates[voxelid] +(0,0,sizes[voxelid,2])
            
            for c in range(len(coordinates)):
                if (coordinates[c] == val).all():
                    mask[i] = False

    #identifies self benchers
    for i in range(len(coordinates)):
        val = coordinates[i] +(0,0,sizes[i,2])
        for c in range(len(coordinates)):
            if (val == coordinates[c]).all():
                mask[i] = False

    coordinates = coordinates[mask]
    sizes = sizes[mask]
    openf = []
    open_faces = nfinder.open_faces(coordinates, sizes)
    for i in range(len(coordinates)):
        openf.append(5-len(open_faces[i]))

    # DATA CLEANED & UPDATED TO SHOW ONLY MINEABLE BLOCKS.
    mask = np.ones(len(openf), dtype=bool)

    max_value = np.max(openf)
    max_indices = np.where(openf == max_value)[0]
    random_index = np.random.choice(max_indices)
    mask[random_index] = False

    path.append(coordinates[random_index])

print(path)