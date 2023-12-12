import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
import time

#this is the file we import for curvature calculation in our scene setup notebook

class Curvature:
    """
    Class for computing curvature of ordered list of points on a plane
    """
    def __init__(self, line):

        self.line = np.array(line)
        self.curvature = None

    @staticmethod
    def _get_twice_triangle_area(a, b, c):

        if np.all(a == b) or np.all(b == c) or np.all(c == a):
            exit('CURVATURE:\nAt least two points are at the same position')

        twice_triangle_area = (b[0] - a[0])*(c[1] - a[1]) - (b[1]-a[1]) * (c[0]-a[0])

        if twice_triangle_area == 0:
            warnings.warn('Collinear consecutive points found: '
                          '\na: {}\t b: {}\t c: {}'.format(a, b, c))

        return twice_triangle_area

    def _get_menger_curvature(self, a, b, c):

        menger_curvature = (2 * self._get_twice_triangle_area(a, b, c) /
                            (np.linalg.norm(a - b) * np.linalg.norm(b - c) * np.linalg.norm(c - a)))
        return -menger_curvature

    def calculate_curvature(self, gap=0):

        self.curvature = np.zeros(len(self.line) - 2)
        for local_, point in enumerate(range(len(self.curvature)-gap*2)):
            triplet = self.line[point:point+3+gap*2:gap+1, :]
            self.curvature[local_] = self._get_menger_curvature(*triplet)
        return self.curvature


