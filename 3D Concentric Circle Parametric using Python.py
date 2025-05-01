import matplotlib.pyplot as plt

import numpy as np

num_circles=10

radius_step=0.5

z_step=1


t=np.linspace(0,2*np.pi,100)

fig=plt.figure(figsize=(6,6))

ax=fig.add_subplot(111,projection='3d')

for i in range(num_circles):

    r=(i+1)*radius_step

    z_layer=i*z_step

    x=r*np.cos(t)

    y=r*np.sin(t)

    z=np.full_like(t,z_layer)

    ax.plot(x,y,z,label=f'Circle {i+1}')

ax.set_title('3D Concetric Circle')

ax.set_xlabel('X axis')

ax.set_ylabel('Y axis')

ax.set_zlabel('Z axis')

ax.set_box_aspect([1,1,2])

plt.tight_layout()

plt.show()