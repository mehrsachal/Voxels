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
faces, openfacecount = blockopenfaces.list_voxel_faces(voxel_array)
print (len(faces))



# nextbatch = utilityvox.remove_voxel(voxel_array, n_on_top)



        
        