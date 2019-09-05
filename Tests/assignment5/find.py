def find_min(L,i):
	"""A function that returns the index of the min value in list"""
	Min = L[i]
	index = i
	
	for j in range(i + 1, len(L)):
		if L[j] < Min:
			Min = L[j]
			index = j

	return index
			
