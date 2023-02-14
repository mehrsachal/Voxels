import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import openfaces
# Define a 3D NumPy array of voxel positions to represent 5 voxels in the same plane
voxels = np.array([[[1, 0], [0, 1]], [[0, 0], [1, 0]]])



faces = openfaces.get_voxel_faces(voxels)

# Plot the voxel faces using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for face in faces:
    x = [face[0][0], face[1][0], face[2][0], face[3][0], face[0][0]]
    y = [face[0][1], face[1][1], face[2][1], face[3][1], face[0][1]]
    z = [face[0][2], face[1][2], face[2][2], face[3][2], face[0][2]]
    verts = [list(zip(x, y, z))]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='blue', edgecolors='black'))

ax.set_xlim3d(0, 2)
ax.set_ylim3d(0, 2)
ax.set_zlim3d(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
print(len(faces))
plt.show()

