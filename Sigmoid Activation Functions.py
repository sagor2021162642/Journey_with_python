import numpy as np
import matplotlib.pyplot as plt

# define sigmoid(x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input range
x = np.linspace(-10, 10, 500)

plt.figure(figsize=(10, 6))
plt.plot(x, sigmoid(x), "b-", label="Sigmoid", fontsize=16)
plt.xlabel("Input", fontsize=14)
plt.ylabel("Output", fontsize=14)
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.title("Activation Function", fontsize=16)
plt.tight_layout()
plt.show()