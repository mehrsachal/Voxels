import pyramidgen
import visualiser
import blockvis
import optblockvis
import openfaces

pyramidgen.genpyr(2)
pr=visualiser.plot_voxel()
pt = openfaces.list_voxel_faces(pr)
print(len(pt))

#blockvis.plot_blocks()
#optblockvis.plot_blocks()