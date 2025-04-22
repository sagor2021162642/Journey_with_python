import numpy as np
import matplotlib.pyplot as plt
a=5
k=7
theta=np.linspace(0,2*np.pi,1000)
r=a*np.cos(k*theta)
x=r*np.cos(theta)
y=r*np.sin(theta)
plt.figure(figsize=(6,6),facecolor="black")
plt.plot(x,y,color='magenta',linewidth=2)
plt.axis('off')
plt.title(f"Rose curve pattern(k={k})",color="white",fontsize=14)
plt.show()