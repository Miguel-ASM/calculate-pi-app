import math
delta_0 = math.sqrt(2.)

def newDelta(delta_old):
    return math.sqrt( 2. * (1. - math.sqrt(1. - 0.25 * delta_old**2) ) )

def calculateDeltasUpToN(n):
    deltas = [delta_0]
    while n:
        deltas.append( newDelta(deltas[-1]) )
        n -= 1
    return deltas

def calculatePiUpToN(n):
    return [2**(N+1)*delta for N,delta in enumerate(calculateDeltasUpToN(n))]
