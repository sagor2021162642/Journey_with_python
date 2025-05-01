import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,400)
y1=np.sin(2np.pix)
y2=np.sin(2np.pix+np.pi2)

plt.figure(figsize=(8,5))
plt.plot(x,y1,label=Wave 1(sin),color='royalblue',linewidth=2)
plt.plot(x, y2, label=Wave 2 (sin + π2), color=crimson, linestyle=--, linewidth=2)

plt.title(Wave pattern plot,fontsize=14,fontweight=bold)
plt.xlabel(X-axis)
plt.ylabel(Y-axis)
plt.grid(True,linestyle='--',alpha=0.6)
plt.show()