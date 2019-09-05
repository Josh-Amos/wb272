def stdev(L):

	mean = 0
	square = 0;

	for i in L:
		mean = mean + i
		square = square + pow(i, 2)
	
	mean = mean / len(L)
	var = (square/len(L)) - pow(mean, 2)
	std = pow(var, 0.5)
	
	return std
