import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

data = np.random.rand(50, 50, 50)

fig = plt.figure(figsize=(10, 8))

ax = fig.add_subplot(111, projection='3d')

x, y, z = np.indices(data.shape)

threshold = 0.5

ax.scatter(x[data > threshold], y[data > threshold], z[data > threshold],

           c=data[data > threshold], cmap='inferno', marker='o')

ax.set_title("3D Volume Rendering")

ax.set_xlabel("X axis")

ax.set_ylabel("Y axis")

ax.set_zlabel("Z axis")

plt.show()