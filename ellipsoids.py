import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # Registers tDjo lb.e ic i)
phi = np.linspace(0, 2 * np.pi, 81)
theta = np.linspace(0, np.pi, 41)
Phi, Theta = np.meshgrid(phi, theta)

U = np.sin(Theta) * np.sin(Phi)
V = np.sin(Theta) * np.cos(Phi)
W = np.cos(Theta)

np.testing.assert_allclose(U**2 + V**2 + W**2, 1, atol=1e-12)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(U, V, W, alpha=0.65)
ax.set(xlim=(-5, 5), ylim=(-5, 5), zlim=(-5, 5))
#plt.show()

semi_a = 3
semi_b = 2
semi_c = 1

U *= semi_a
V *= semi_b
W *= semi_c

A = np.array([1., 0., 0.])
B = np.array([4., 4., 2.])

d = (A + B) / 2.0
a = np.linalg.norm(B-A) / 2
e_x = (B-A)/np.linalg.norm(B-A)

np.testing.assert_allclose(d - a * e_x, A, atol=1e-12)
np.testing.assert_allclose(d + a * e_x, B, atol=1e-12)

# e_x is now the vector pointing from A to B (line segment)
# e_x does not necessarily start at the origin.
# e_x is the unit vector for the X axis of the ellipsoid
# I'd make y the rotation of e_x along the XY axis by 90 degrees.

# construct a rotation matrix
R = np.array([
    [np.cos(np.pi/2), -np.sin(np.pi/2), 0],
    [np.sin(np.pi/2), np.cos(np.pi/2), 0],
    [0, 0, 1]])

e_x_shadow = e_x.copy()
e_x_shadow[2] = 0.0

e_y = R @ e_x_shadow
e_y = e_y / np.linalg.norm(e_y)
e_z = np.cross(e_x, e_y)

np.testing.assert_allclose(np.dot(e_x, e_y), 0.0, atol=1e-12)

ax.plot(
    [A[0], B[0]],
    [A[1], B[1]],
    [A[2], B[2]],
    color = 'red',
    linewidth=2
)

plt.show()
