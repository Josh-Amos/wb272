import sys

A = 9.81

def velocity(v0,t):
	"""A function that determines the velocity"""
	return v0 + (A * t)

def distance(s0,v0,t):
	"""A function that determines the distance"""
	return s0 + (v0 * t) + (0.5 * A * pow(t,2))

def velocity2(Ds,v0):
	"""A function that determines the velocity"""
	x = pow(v0,2) + (2 * A * Ds)
	return pow(x,0.5)

if __name__ == "__main__":
	v0 = int(sys.argv[1])
	t  = int(sys.argv[2])
	s0 = int(sys.argv[3])
	s1 = int(sys.argv[4])
	Ds = int(s1) - int(s0)
	print(velocity(v0,t))
	print(distance(s0,v0,t))
	print(velocity2(Ds,v0))
	
