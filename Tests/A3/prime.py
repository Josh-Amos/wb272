def prime_factorise(n):
	
	L = []
	K = []
	i = 2
	p1 = 0
	n1 = 0
	k = 0
	lowest = 0

	while i < n:
		if (n % i == 0):
			k = n
			p1 = i
			n1 = 1
			while (k % i == 0):
				n1 += 1
				k = k / i

			L.append((p1, n1 - 1))
		n1 = 0
		i += 1
	
	lowest = L[0][0]
	for item in L:
		if (item[0] == lowest or not(item[0] % lowest == 0)):
			K.append(item)

	return K
