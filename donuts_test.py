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

md = MultiDonut([1., a, b, c], dx, dy)
md.plot()
