import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 6, 500)
y1 = np.sin(x1)

x2 = np.random.rand(10) * 6
y2 = np.cos(x2)

plt.style.use("scifig")
plt.xlabel("x label")
plt.ylabel("y label")

plt.plot(x1, y1, "k-", label="sin(x)")
plt.plot(x2, y2, "bo", label="cos(x)")

plt.legend()
plt.tight_layout()

plt.savefig("scifig_example.png", dpi=300)
