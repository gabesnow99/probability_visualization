import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from probability_representations import Donut, MultiDonut

n = 1000000

# a = Donut(17., 2.6, -10, -15, num_points=n)
# b = Donut(12, 2.5, 10, 3, num_points=n)
# c = Donut(10, 2.6, -3, 5, num_points=n)

a = Donut(17., .1, -10, -15, num_points=n)
b = Donut(12, .1, 10, 3, num_points=n)
c = Donut(10, .1, -3, 5, num_points=n)

# a = Donut(11, .5, 8, 0, num_points=n)
# b = Donut(10, .5, 10, 0, num_points=n)
# c = Donut(15, .1, 0, 0)

# a = 1.
# b = 1.
# c = 1.

# dx = .1
# dy = .1
dx = .25
dy = .25
# dx = .5
# dy = .5
# dx = 1.
# dy = 1.

md = MultiDonut([a, b, c], dx, dy)
# print(md.get_max_loc())
md.plot(False)
