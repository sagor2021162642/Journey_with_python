import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(10000)
y=np.random.randn(10000)

plt.hexbin(x,y,gridsize=30,cmap='Blues',edgecolor='gray')
plt.colorbar(label='Count in bin')
plt.title('Honeycomb pattern plot')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()