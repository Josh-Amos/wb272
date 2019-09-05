
#Solve the square root w/o Math.sqrt
def qsolve(a,b,c):
    delta = pow(b,2) - (4 * (a *c))
    sqrt = pow(delta,0.5)
    numerator1 = -(b) + sqrt
    numerator2 = -(b) - sqrt
    denominator = 2 * a
    return numerator1 / denominator , numerator2 / denominator
