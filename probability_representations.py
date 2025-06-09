import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


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

class Donut():

    def __init__(self, radius_mean, radius_stdev, x_center=0., y_center=0., num_points=100000):
        self.radius_mean = radius_mean
        self.radius_stdev = radius_stdev
        self.x_center = x_center
        self.y_center = y_center
        self.num_points = num_points
        self.x, self.y = self.generate_points()

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
