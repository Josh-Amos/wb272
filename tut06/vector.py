def print_as_vector(L):
	
	vector = ""

	for i in range(len(L)):
		
		if (i == 0):
			vector = "<{}, ".format(L[0])

		elif (i == len(L) - 1):
			vector = vector + "{}>".format(L[len(L) - 1])

		else:
			vector = vector + "{}, ".format(L[i])
	
	print(vector)
