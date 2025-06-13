import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from probability_representations import Donut, MultiDonut

n = 1000000

a = Donut(15., 2.6, -10, -15, num_points=n)
b = Donut(12, 2.5, 10, 3, num_points=n)
c = Donut(10, 2.6, -3, 5, num_points=n)

# dx = .1
# dy = .1
# dx = .25
# dy = .25
dx = .5
dy = .5
# dx = 1.
# dy = 1.

md = MultiDonut([a, b, c], dx, dy)
x_vals, y_vals, z_vals = md.get_points_for_plotting()

peak_index = np.argmax(z_vals)
x_max, y_max, z_max = x_vals[peak_index], y_vals[peak_index], z_vals[peak_index]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(x_vals, y_vals, [0]*len(z_vals), dx=dx, dy=dy, dz=z_vals)

ax.scatter(x_max, y_max, z_max, color='r', s=100)
plt.show()
