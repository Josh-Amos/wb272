def matrix_transpose(matrix):
	
	m = len(matrix) #ROWS
	n = len(matrix[0]) #COLS
	transpose = []
	
	for i in range(n):
		#appends all the elements of the first sublist as the first 
		#elements of the n sublists
		transpose.append([matrix[0][i]])
		for j in range(1,m):
			#Appends by indexing the next sublist ([-1])
			transpose[-1].append(matrix[j][i])
	
	return transpose
