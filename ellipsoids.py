import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # Registers the 3D projection in Matplotlib 3.1.

theta = np.linspace(0, np.pi, 41)
phi = np.linspace(0, 2 * np.pi, 81)
Phi, Theta = np.meshgrid(phi, theta)

U = np.sin(Theta) * np.sin(Phi)
V = np.sin(Theta) * np.cos(Phi)
W = np.cos(Theta)

np.testing.assert_allclose(U**2 + V**2 + W**2, 1, atol=1e-12)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(U, V, W, alpha=0.65)
ax.set(xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1))
plt.show()

semi_a = 3
semi_b = 2
semi_c = 1

U *= semi_a
V *= semi_b
W *= semi_c

A = np.array([0., 0., 0.])
B = np.array([4., 4., 2.])

d = A + B / 2.0
a = np.linalg.norm(d)
e_x = d/a
print(e_x)
print(d)
