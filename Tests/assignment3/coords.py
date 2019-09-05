import math

def polar_to_cartesian(r,theta,d):
    """Returns cartesian coordinates"""
    radians = math.radians(theta)
    x = r * math.cos(radians)
    y = r * math.sin(radians)
    s = "({0:.{prec}f}, {1:.{prec}f})".format(x,y,prec = d)
    return s
