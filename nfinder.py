def count_neighbors(coords, sizes):
    num_voxels = len(coords)
    neighbors = [[] for i in range(num_voxels)]
    for i in range(num_voxels):
        for j in range(num_voxels):
            if i == j:
                continue
            is_neighbor = True
            for k in range(3):
                if abs(coords[i][k] - coords[j][k]) > sizes[i][k] + 1 or abs(coords[i][k] - coords[j][k]) > sizes[j][k] + 1:
                    is_neighbor = False
                    break
            if is_neighbor:
                val = coords[i] -(0,0,sizes[i,2])
                
                if (val == coords[j]).all():
                    continue
                else:
                    neighbors[i].append(j)
    return neighbors



def open_faces(coords, sizes):
    num_voxels = len(coords)
    neighbors = [[] for i in range(num_voxels)]
    for i in range(num_voxels):
        for j in range(num_voxels):
            if i == j:
                continue
            is_neighbor = True
            for k in range(3):
                if k == 2 and coords[i][2] + sizes[i][2] == coords[j][2]:
                    is_neighbor = False
                    break
                elif abs(coords[i][k] - coords[j][k]) > sizes[i][k] + 1 or abs(coords[i][k] - coords[j][k]) > sizes[j][k] + 1:
                    is_neighbor = False
                    break
            if is_neighbor:
                neighbors[i].append(j)
    return neighbors

