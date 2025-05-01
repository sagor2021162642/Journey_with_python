import numpy as np
import matplotlib.pyplot as plt

diamond_x = [0, 1, 0, -1, 0]
diamond_y = [1, 0, -1, 0, 1]

plt.figure(figsize=(5, 5))
plt.plot(diamond_x, diamond_y, 'b-', linewidth=2)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()