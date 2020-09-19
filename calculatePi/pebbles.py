"""pebbles.py

    functions used to approximate pi with the Montecarlo method.

    Circumference center is at (0,0) and has a radius of 1. The square has a side of 2 and also centered in (0,0)
"""

import random
# import math
# from matplotlib import pyplot as plt
# import numpy as np

def pointIsInside(x,y):
    """pointIsInside

    Arguments:
    x,y -- x and y coordinates of the point.

    returns true if it is inside of the Circumference.
    """
    return x**2 + y**2 <= 1.

class MontecarloApprox:
    """MontecarloApprox class

    Description: class that implements an approximation to the number
    pi using the Montecarlo method.

    Attributes of the instances:
    - self.points -- a list of the pebbles positions. Each point is a tuple in the
        (x_coordinate,y_coordinate) format
    - self.pi_values -- a list containing the value of pi after every pebble thrown
    - self.points_inside -- the number of pebbles inside of the circumference
    - self.points_total -- the total number of pebbles
    """
    def __init__(self):
        self.points = []
        self.pi_values = []
        self.points_inside = 0
        self.points_total = 0

    def __str__(self):
        return '{:.8f}'.format(self.returnBestPiValue())

    def returnBestPiValue(self):
        if self.pi_values:
            return self.pi_values[-1]
        else:
            return 0.

    def updatePi(self):
        self.pi_values.append(4 * self.points_inside / self.points_total)

    def addNewPoint(self,n=1):
        """addNewPoint

        Description: adds n points to the board.

        Arguments:
        n -- number of new pebbles (defaults to 1)
        """
        for i in range(n):
            x = 2*random.random() - 1.
            y = 2*random.random() - 1.
            self.points.append( (x,y) )
            self.points_total += 1
            if pointIsInside(x, y):
                self.points_inside += 1
        self.updatePi()
