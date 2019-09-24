import numpy as np
import numpy.linalg as la

def invertible(A, B):
	""""Checks whether array A or B is invertible"""
	detA = la.det(A)
	detB = la.det(B)
	
	if (detA == 0):
		if (detB == 0):
			print("None are invertible")
		else:
			return B
	else:
		if (detB == 0):
			return A
		else:
			print("Both are invertible")

def sol_matrix(D, b):
	x = la.solve(D, b)
	return x

def matrix_multipl(A, n):
	x = la.matrix_power(A, n)
	return x
