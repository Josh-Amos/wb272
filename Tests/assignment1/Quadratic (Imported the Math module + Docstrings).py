import math

def qsolve(a,b,c):
	"""Returns the roots of the quadratic equation"""
	delta = math.sqrt(b**2 - (4 * a * c))
	n1 = -b + delta
	n2 = -b - delta
	den = 2 * a
	return n1/den, n2/den
