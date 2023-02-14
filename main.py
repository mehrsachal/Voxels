import pyramidgen
import visualiser
import blockvis
import listopenfaces
import doublebench

pyramidgen.genpyr(2)
voxel_array=visualiser.plot_voxel()
print(voxel_array)

faces, open_face_count =listopenfaces.list_voxel_faces(voxel_array)
print(len(faces))
print("Open face count:", open_face_count)

n_on_top=doublebench.get_voxels_with_neighbor_on_top(voxel_array)
print("Voxels with neighbor on top:")
print(n_on_top)