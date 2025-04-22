import numpy as np

import matplotlib.pyplot as plt

num_stars = 30  

x_vals = np.random.uniform(0, 10, num_stars)

y_vals = np.random.uniform(0, 10, num_stars)

sizes = np.random.randint(20, 100, num_stars)

num_connections = 10

connections = np.random.choice(num_stars, (num_connections, 2), replace=False)

fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')

ax.set_facecolor("black")

ax.scatter(x_vals, y_vals, s=sizes, color='white', alpha=0.8)

for start, end in connections:

    ax.plot([x_vals[start], x_vals[end]], [y_vals[start], y_vals[end]], 

            color='white', linestyle='-', linewidth=0.8, alpha=0.6)

ax.set_xticks([])

ax.set_yticks([])

ax.set_frame_on(False)

plt.title("Star Constellation Pattern", fontsize=14, fontweight="bold", color="white")

plt.show()