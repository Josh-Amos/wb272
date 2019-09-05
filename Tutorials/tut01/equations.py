import math

def velocity(v0,t):
    return v0 + (9.81 * t)
    
def distance(s0,v0,t):
    return s0 + (v0 * t) + (0.5 * 9.81 * (t * t))

def velocity2(v0,deltaS):
    v0 = v0 * v0
    v = v0 + (2 * 9.81 * deltaS)
    return math.sqrt(v)

    
