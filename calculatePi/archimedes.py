import math
delta_0 = math.sqrt(2.)
first_points = [(0.,1.),(1.,0.),(0.,-1.),(-1.,0.)]

def returnNewDelta(delta_old):
    return math.sqrt( 2. * (1. - math.sqrt(1. - 0.25 * delta_old**2) ) )

def returnDeltasUpToN(n):
    deltas = [delta_0]
    while n:
        deltas.append( returnNewDelta(deltas[-1]) )
        n -= 1
    return deltas

def returnPiUpToN(n):
    return [2**(N+1)*delta for N,delta in enumerate(returnDeltasUpToN(n))]

def returnNewPoints(old_points):
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

def returnPointsUptToN(n):
    points = [first_points]
    while n:
        points.append( returnNewPoints(points[-1]) )
        n -= 1
    return points
