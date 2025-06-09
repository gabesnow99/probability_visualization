import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from probability_representations import Donut

n = 1000000

a = Donut(15., 2.6, -10, -15, num_points=n)
b = Donut(12, 2.5, 10, 3, num_points=n)
c = Donut(10, 2.6, -3, 5, num_points=n)

def round_em_up(x, dx=None):
    x = np.copy(x)
    if dx == None:
        span = max(x) - min(x)
        dx = span / 100
    return np.round(x / dx) * dx

def donut_bar3d(x, y, dx, dy, ax):

    points = np.column_stack((round_em_up(x, dx), round_em_up(y, dy)))
    points_tuples = [tuple(p) for p in points.tolist()]
    counts = Counter(points_tuples)

    x_vals = [point[0] for point in counts.keys()]
    y_vals = [point[1] for point in counts.keys()]
    z_vals = np.array(list(counts.values())) / n

    ax.bar3d(x_vals, y_vals, [0]*len(z_vals), dx=dx, dy=dy, dz=z_vals)

    peak_index = np.argmax(z_vals)
    return x_vals[peak_index], y_vals[peak_index], z_vals[peak_index]


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# dx = .1
# dy = .1
# dx = .25
# dy = .25
# dx = .5
# dy = .5
dx = 1.
dy = 1.

x_ = np.concatenate((a.x, b.x, c.x))
y_ = np.concatenate((a.y, b.y, c.y))

x_max, y_max, z_max = donut_bar3d(x_, y_, dx, dy, ax)
ax.scatter(x_max, y_max, z_max, color='r', s=100)

plt.show()
