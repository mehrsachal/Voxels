import pyramidgen
import visualiser
import blockvis
import optblockvis
import openfaces
import listopenfaces

pyramidgen.genpyr(2)
voxel_array=visualiser.plot_voxel()
# open_faces = openfaces.list_voxel_faces(voxel_array)
# print(len(open_faces))
# print(open_faces)

faces, open_face_count =listopenfaces.list_voxel_faces(voxel_array)

print("Faces:", faces)
print("Open face count:", open_face_count)


#blockvis.plot_blocks()
#optblockvis.plot_blocks()