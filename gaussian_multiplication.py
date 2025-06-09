import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from probability_representations import Guassian

a_mean, a_stdev = 8, 1
# a_x = np.linspace(a_mean - 4*a_stdev, a_mean + 4*a_stdev, 1000)
a_x = np.linspace(2.5, 20, 1000)
a_pdf = norm.pdf(a_x, a_mean, a_stdev)
a = Guassian(a_mean, a_stdev)

b_mean, b_stdev = 12, 2
# b_x = np.linspace(b_mean - 4*b_stdev, b_mean + 4*b_stdev, 1000)
b_x = np.linspace(2.5, 20, 1000)
b_pdf = norm.pdf(b_x, b_mean, b_stdev)
b = Guassian(b_mean, b_stdev)

dx = .1

a_ = a.bins(dx)
b_ = b.bins(dx)

# c_add = {key: a_.get(key, 0.) + b_.get(key, 0.) for key in set(a_) | set(b_)}
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.bar(c_add.keys(), c_add.values(), dx)
# ax.plot(a_x, a_pdf, c='red', linewidth=1.)
# ax.plot(b_x, b_pdf, c='red', linewidth=1.)
# ax.plot(a_x, a_pdf + b_pdf, c='red', linewidth=3.)

c_muliply = {key: 28 * a_.get(key, 0.) * b_.get(key, 0.) for key in set(a_) | set(b_)}
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(c_muliply.keys(), c_muliply.values(), dx)
ax.plot(a_x, a_pdf, c='red', linewidth=1.)
ax.plot(b_x, b_pdf, c='red', linewidth=1.)
# ax.plot(a_x, a_pdf * b_pdf, c='red', linewidth=2.)

product_mean = (a.mean * b.stdev**2 + b.mean * a.stdev**2) / (a.stdev**2 + b.stdev**2)
product_stdev = np.sqrt((a.stdev**2 * b.stdev**2) / (a.stdev**2 + b.stdev**2))
product_pdf = norm.pdf(a_x, product_mean, product_stdev)
ax.plot(a_x, product_pdf, c='red', linewidth=2.)

plt.show()