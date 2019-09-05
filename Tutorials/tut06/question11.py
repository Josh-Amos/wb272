from decimal import *
import sys

def phi_deci(d):
	#Iterations:65
	#Floating-point: 27
	n = 500
	F = [0,1]
	number = 0
	if (d < 1 or d == 1):
		print("Enter a value for d, where d > 1")
	else:
		x = 1 * pow(10,-d)
		#print(x)
		#prec = "0." + ("0" * (d - 1)) + "1"
		#p = float(prec)
		for i in range(2,n):
			a = F[i - 1] + F[i - 2]
			F.append(a)

		for i in range(2, len(F)):
			if ((i + 2) == len(F) - 1):
				a = F[i - 1] + F[i - 2]
				F.append(a)
			phi1 = Decimal(F[i + 1]) / Decimal(F[i])
			phi2 = Decimal(F[i + 2]) / Decimal(F[i + 1])
			if (abs(phi2 - phi1) <= x):
				answer = "{0:.{prec}f}".format(phi2,prec=d)
				print("*** ITERATIONS: {0} ***".format(number))
				print("Phi: {0}".format(answer))
				break;
			else:	
				answer1 = "{0:.{prec}f}".format(phi1,prec=d)
				answer2 = "{0:.{prec}f}".format(phi2,prec=d)
				number += 1
				#print("Phi1: {0}".format(answer1))
				#print("Phi2: {0}".format(answer2))
				#print("__________________________")

def phi_float(d):
	#Iterations = 38
	#floating-point = 15
	n = 500
	F = [0,1]
	number = 0
	if (d < 1 or d == 1):
		print("ERROR: Enter a value, where value > 1")
	else:
		x = 1 * pow(10,-d)
		#prec = "0." + ("0" * (d - 1)) + "1"
		#p = float(prec)
		for i in range(2,n):
			a = F[i - 1] + F[i - 2]
			F.append(a)

		for i in range(2, len(F)):
			if ((i + 2) == len(F) - 1):
				a = F[i - 1] + F[i - 2]
				F.append(a)
			phi1 = F[i + 1] / F[i]
			phi2 = F[i + 2] / F[i + 1]
			if (abs(phi2 - phi1) <= x):
				answer = "{0:.{prec}f}".format(phi2,prec=d)
				print("*** ITERATIONS: {0} ***".format(number))
				print("Phi: {0}".format(answer))
				break;
			else:	
				answer1 = "{0:.{prec}f}".format(phi1,prec=d)
				answer2 = "{0:.{prec}f}".format(phi2,prec=d)
				number += 1
				#print("Phi1: {0}".format(answer1))
				#print("Phi2: {0}".format(answer2))
				#print("__________________________")

if __name__ == "__main__":
	if (sys.argv[1] == "f"):
		phi_float(int(sys.argv[2]))
	elif (sys.argv[1] == "d"):
		phi_deci(int(sys.argv[2]))
	else:
		print("Incorrect inputs!")


