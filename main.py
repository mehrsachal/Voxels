import blockvis
import newapp
import nfinder
import numpy as np

#File Initialization
file_name = 'blocks.xlsx'
coordinates, sizes = newapp.excel_to_arrays(file_name)
path=[]


while len(coordinates)>0:

    #CREATES A MASK TO REMOVE ALL BLOCKS THAT ARE NOT MINEABLE
    mask = np.ones(len(coordinates), dtype=bool)
    #IDENTIFIES NEIGHBORS
    neighbors = nfinder.count_neighbors(coordinates, sizes)
    #CHECK NEIGHBORS FOR DOUBLE BENCHERS
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

    newcoord = coordinates[mask]
    newsize = sizes[mask]

    #REMOVED!!!!!!!!!!!!!
    


    #FINDS OPEN FACES
    openf = []
    open_faces = nfinder.open_faces(newcoord, newsize)
    for i in range(len(newcoord)):
        openf.append(5-len(open_faces[i]))
    


    max_value = np.max(openf)
    max_indices = np.where(openf == max_value)[0]
    random_index = np.random.choice(max_indices)
    path.append(newcoord[random_index])
    

    for i in range(len(coordinates)):
        if (coordinates[i] == newcoord[random_index]).all():
            random_index = i
            break
    coordinates = np.delete(coordinates, random_index, 0)
    sizes = np.delete(sizes, random_index, 0)
    
    
    


cleaned_list = [tuple(x.tolist()) for x in path]

#print(cleaned_list)
coordinates, sizes = newapp.excel_to_arrays(file_name)

colors = blockvis.generate_color_list(len(cleaned_list))
blockvis.voxelvis(cleaned_list, sizes,colors)

