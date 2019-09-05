
def answer():
	"""QUESTION 4(a)"""
	metals = [["beryllium",4,9.012],["magnesium",12,24.305],["calcium",20,40.078],["strontium",38,87.620],["barium",56,137.327],["radium",88,226.000]]
	
	for i in metals:
		a = "{0:<9}: {2:>2} {3:>7,.3f}".format(i[0],":",i[1],i[2])
		print(a)
		
	data = []	
	
	for i in metals:
		for j in range(len(metals[0])):
			data.append(i[j])
			
	print(data)

