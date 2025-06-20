import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from time import time


# 1D Guassian Function
class Guassian():

    def __init__(self, mean, stdev, num_points=1000000):
        self.mean = mean
        self.stdev = stdev
        self.num_points = num_points
        self.points = self.generate_points()

    def generate_points(self):
        points = np.random.normal(loc=self.mean, scale=self.stdev, size=self.num_points)
        return points

    def round_em_up(self, dx):
        x = np.copy(self.points)
        return np.round(x / dx) * dx

    def bins(self, dx):
        c = Counter(self.round_em_up(dx))
        for key in c.keys():
            c[key] = float(c[key] / (self.num_points * dx))
        return c

    def scatter(self, using_bins=False, dx=None, plot_show=True):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        if using_bins:
            if dx == None:
                dx = .1
            ax.scatter(self.round_em_up(dx), np.zeros(len(self.points)), marker='.', alpha=.05)
        else:
            ax.scatter(self.points, np.zeros(len(self.points)), marker='.', alpha=.05)
        if plot_show:
            plt.show()

    def bar(self, using_bins=False, dx=None):
        pass


# Donut Probability
class Donut():

    def __init__(self, radius_mean, radius_stdev, x_center=0., y_center=0., num_points=100000):
        self.radius_mean = radius_mean
        self.radius_stdev = radius_stdev
        self.x_center = x_center
        self.y_center = y_center
        self.num_points = num_points
        self.x, self.y = self.generate_points()

    # Used to create the random points used in calculation
    def generate_points(self):
        thetas = np.random.uniform(0, 2*np.pi, self.num_points)
        radii = np.random.normal(loc=self.radius_mean, scale=self.radius_stdev, size=self.num_points)
        x = self.x_center + radii * np.cos(thetas)
        y = self.y_center + radii * np.sin(thetas)
        return x, y

    def scatter_donut(self):
        plt.scatter(self.x, self.y, alpha=.1, marker='.')
        plt.axis('equal')
        plt.grid(True)
        plt.show()

    def round_em_up(self, x, dx):
        x = np.copy(x)
        return np.round(x / dx) * dx

    def bins(self, dx, dy):
        t0 = time()
        points = np.column_stack((self.round_em_up(self.x, dx), self.round_em_up(self.y, dy)))
        print(" ", time() - t0)
        t0 = time()
        # TODO: DO THIS FASTER
        points_tuples = [tuple(p) for p in points.tolist()]
        print(" ", time() - t0)
        t0 = time()
        # TODO: DO THIS FASTER
        c = Counter(points_tuples)
        print(" ", time() - t0)
        for key in c.keys():
            c[key] = float(c[key] / (self.num_points * dx * dy))
        return c


# Used to combine and manipulate multiple donut probability representations
class MultiDonut():

    # donuts must be an array of above Donut class
    def __init__(self, donuts=[], dx=.5, dy=.5):
        if not isinstance(donuts, list):
            print("DONUTS MUST BE A LIST OF Donut INSTANCES")
            return
        self.dx = dx
        self.dy = dy
        # self.donuts = []
        self.donuts_discrete = []
        for d in donuts:
            self.add_donut(d)
        self.counts = self.multiply_probs()

    # def recalculate(self):
    #     self.multiply_probs()

    def add_donut(self, donut, recalculate=False):
        if not isinstance(donut, Donut):
            print("THIS MONSTROCITY IS OF AN INCORRECT DATA TYPE")
            return
        t0 = time()
        self.donuts_discrete.append(donut.bins(self.dx, self.dy))
        print(time() - t0)
        if recalculate:
            self.multiply_probs()

    def multiply_probs(self):
        d = {key: self.donuts_discrete[0].get(key, 0.) * self.donuts_discrete[1].get(key, 0.) for key in set(self.donuts_discrete[0]) | set(self.donuts_discrete[1])}
        for ii in range(2, len(self.donuts_discrete)):
            d = {key: d.get(key, 0.) * self.donuts_discrete[ii].get(key, 0.) for key in set(d) | set(self.donuts_discrete[ii])}
        d = normalize_dict(d)
        return d

    def add_probs(self):
        d = {key: self.donuts_discrete[0].get(key, 0.) + self.donuts_discrete[1].get(key, 0.) for key in set(self.donuts_discrete[0]) | set(self.donuts_discrete[1])}
        for ii in range(2, len(self.donuts_discrete)):
            d = {key: d.get(key, 0.) + self.donuts_discrete[ii].get(key, 0.) for key in set(d) | set(self.donuts_discrete[ii])}
        d = normalize_dict(d)
        return d

    def make_points_for_plotting(self):
        self.x_vals = [point[0] for point in self.counts.keys()]
        self.y_vals = [point[1] for point in self.counts.keys()]
        self.z_vals = np.array(list(self.counts.values()))
        peak_index = np.argmax(self.z_vals)
        self.x_max, self.y_max, self.z_max = self.x_vals[peak_index], self.y_vals[peak_index], self.z_vals[peak_index]

    # TODO: MAKE THIS BETTER
    def get_max_loc(self):
        self.make_points_for_plotting()
        return self.x_max, self.y_max, self.z_max

    # Shortcut way to visualize the combined probabilities
    def plot(self, show_peak=True):
        # Get max peak
        x_max, y_max, z_max = self.get_max_loc()

        # Make the figure
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.bar3d(self.x_vals, self.y_vals, [0]*len(self.z_vals), dx=self.dx, dy=self.dy, dz=self.z_vals)

        # Plot the peak as a red dot
        if show_peak:
            ax.scatter(x_max, y_max, z_max, color='r', s=100)

        plt.show()



def normalize_dict(d, norm_val=1):
    total = 0.
    for key in d.keys():
        total += d[key]
    for key in d.keys():
        d[key] = norm_val * d[key] / total
    return d
