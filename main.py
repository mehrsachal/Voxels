import pyramidgen
import visualiser
import blockvis
import optblockvis
import openfaces

pyramidgen.genpyr(3)
pr=visualiser.plot_voxel()
pt = openfaces.find_open_faces(pr)
print(pt)
#blockvis.plot_blocks()
#optblockvis.plot_blocks()