import sys

def sqrt(a):
	x0 = a
	e = 10e-15
	xn = (x0 + a/x0) / 2

	while abs(xn - x0) >= 10e-15:
		x0 = xn
		xn = (x0 + a/x0) / 2
	
	print(xn)
	return xn

if __name__ == "__main__":
	sqrt(float(sys.argv[1]))
