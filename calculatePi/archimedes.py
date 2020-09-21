"""archimedes.py

    functions used to approximate pi with the archimede method
"""

import math
from matplotlib import pyplot as plt
import numpy as np

# Avoid automatic display of the figures
plt.ioff()

#Initial values for the sides and the points
delta_0 = math.sqrt(2.)
# The format for the points is [(x_1,y_1),(x_2,y_2),....]
first_points = [(0.,1.),(1.,0.),(0.,-1.),(-1.,0.)]

# When we approximate up to order n, we have
# deltas = [delta_0,delta_1,....,delta_n]
# points = [points_0,points_1,....,points_n]

def returnNewDelta(delta_old):
    """returns the side of the new polygonal approximation.

    Arguments:
    delta_old -- the side of the previous approximation
    """
    return math.sqrt( 2. * (1. - math.sqrt(1. - 0.25 * delta_old**2) ) )

def returnDeltasUpToN(n):
    """returns the sides of the polygonal approximations up to the n approximation.

    Arguments:
    n -- the order of the approximation
    """
    deltas = [delta_0]
    while n:
        deltas.append( returnNewDelta(deltas[-1]) )
        n -= 1
    return deltas

def returnPiUpToN(n):
    """returns the approximations of pi up to the n approximation.

    Arguments:
    n -- the order of the approximation
    """
    return [2**(N+1)*delta for N,delta in enumerate(returnDeltasUpToN(n))]

def returnNewPoints(old_points):
    """returns the points of the new approximation polygon.

    Arguments:
    old_points -- points of the previous polygon approximation
    """
    new_points = []
    for point,next_point in zip(old_points,old_points[1:]+old_points[0:1]):
        # Calculate the intermediate point between point and next_point
        x_intermediate = 0.5 * (point[0]+next_point[0])
        y_intermediate = 0.5 * (point[1]+next_point[1])
        # Normalize its distance w.r. to the origin to one
        length = math.sqrt(x_intermediate**2+y_intermediate**2)
        intermediate_point = (x_intermediate/length , y_intermediate/length)
        # add the points to the new_points list
        new_points.append(point)
        new_points.append(intermediate_point)
    return new_points

def returnPointsUpToN(n):
    """returns the points of approximation polygons up to order n.

    Arguments:
    n -- the order of the approximation
    """
    points = [first_points]
    while n:
        points.append( returnNewPoints(points[-1]) )
        n -= 1
    return points


def plotTheApproximationPolygon(points):
    """plots the approximation polygons up to order n together to the circle.

    Arguments:
    points -- the list of the points for the approximation
    """

    # First the points have to be unpacked in a x and y values
    x, y = zip(*points)

    # Create a figure
    fig,ax = plt.subplots(constrained_layout=True,figsize=(8,8))

    ax.set_aspect(1.)
    ax.set_xlim(-1.1,1.1)
    ax.set_ylim(-1.1,1.1)

    rho_circle = np.linspace(0, 2 * np.pi,100)
    r_circle = np.ones(np.shape(rho_circle))

    x_circle = r_circle * np.cos(rho_circle)
    y_circle = r_circle * np.sin(rho_circle)

    ax.fill(x_circle,y_circle,fill=False,zorder=1)
    ax.fill(x, y,zorder=2)

    return fig
