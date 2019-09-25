def exponential(x):
	
	fixed = x
	k = 2
	j = 1
	s0 = 1
	sn = 1 + x

	while not(sn == s0): 
		x = x * fixed

		for i in range(1, k + 1):
			j = j * i


		s0 = sn
		sn = sn + (x / j)
		k = k + 1
		j = 1
	
	return sn
