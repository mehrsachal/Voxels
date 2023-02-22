import pyramidgen
import visualiser
import blockvis
import listopenfaces
import doublebench
import utilityvox
import numpy as np
import blockopenfaces

# pyramidgen.genpyr(2)
# voxel_array=visualiser.plot_voxel()
# faces, openfacecount = listopenfaces.list_voxel_faces(voxel_array)
# print (len(faces))

voxel_array=blockvis.plot_blocks()

faces = blockopenfaces.get_voxel_faces(voxel_array)

# Count the number of shared faces between neighboring voxels
shared_faces = blockopenfaces.count_shared_faces(faces, voxel_array)

# Count the total number of faces
total_faces = sum([len(faces_i) for faces_i in faces.values()]) / 2
for shared in shared_faces.values():
    total_faces += shared

print(total_faces)