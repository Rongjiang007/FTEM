import matplotlib.pyplot as plt
import numpy as np
from math import *

'''
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e

# build up the numpy logo
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True
facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
filled = np.ones(n_voxels.shape)




# upscale the above voxel image, leaving gaps
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)

print(filled_2)


# Shrink the gaps
x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
x[0::2, :, :] += 0.05
y[:, 0::2, :] += 0.05
z[:, :, 0::2] += 0.05
x[1::2, :, :] += 0.95
y[:, 1::2, :] += 0.95
z[:, :, 1::2] += 0.95

ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
#ax.set_aspect('equal')

plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_cube(x1=0,y1=0,z1=0,a=1,b=1,c=1):   
    phi = np.arange(1,10,2)*np.pi/4
    Phi, Theta = np.meshgrid(phi, phi)

    x = np.cos(Phi)*np.sin(Theta)
    y = np.sin(Phi)*np.sin(Theta)
    z = np.cos(Theta)/np.sqrt(2)
    return x*a+x1,y*b+y1,z*c+z1

def getcoord2m(R,coordr):
    #np.random.seed(IC)
    theta=90.0/180.0*np.pi
    fai=10/180.0*np.pi
    
    x_tar=R*cos(fai)*cos(theta)+coordr[0]
    y_tar=R*cos(fai)*sin(theta)+coordr[1]
    z_tar=R*sin(fai)+coordr[2]
    
    return [x_tar,y_tar,z_tar]



coordr=[-1,0,-35+2]
R=15
coord_tar=getcoord2m(R,coordr)
print(coord_tar)


plt.rcParams.update({'font.size': 16})
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

x,y,z=-20,0,-33
a,b,c = 40,10,10
x,y,z = get_cube(x,y,z,a,b,c)
#ax.plot_surface(x, y, z,alpha=0.25,color='gray')
ax.plot_surface(x, y, z,alpha=0.5,cmap='gray')

'''
x,y,z=-7.5,0,-17.5
#x,y,z=0,0,0
a,b,c = 10,20,15
x,y,z = get_cube(x,y,z,a,b,c)
ax.plot_surface(x, y, z,color='peru')



x,y,z=17.5,0,0
#x,y,z=0,0,0
a,b,c = 15,20,20
x,y,z = get_cube(x,y,z,a,b,c)
ax.plot_surface(x, y, z,color='peru')



x,y,z=-17.5,15,0
#x,y,z=0,0,0
a,b,c = 15,10,20
x,y,z = get_cube(x,y,z,a,b,c)
ax.plot_surface(x, y, z,color='peru')

'''

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 6 * np.outer(np.cos(u), np.sin(v))
y = 6 * np.outer(np.sin(u), np.sin(v))
z = 6 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x+coord_tar[0]+2, y+coord_tar[1], z+coord_tar[2],color='peru')

#plt.xlabel('X (m)',fontsize=20)
#plt.ylabel('Y (m)',fontsize=20)
#plt.zlabel('Z (m)',fontsize=20)
#plt.grid(b=None)
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)
ax.set_zlim(-60,0)
#ax.view_init(0,0)
plt.savefig('3d.jpg',dpi=300)
plt.show()
