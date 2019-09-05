metals = [['beryllium',4,9.012],['magnesium',12,24.305],['calcium',20,40.078],['strontium',38,87.62],['barium',56,137.327],['radium',88,226]]
j = 0
for i in range(len(metals)):
		print("{0:<9}: {1:>2} {2:>7.3f}".format(metals[i][j],metals[i][j+1],metals[i][j+2]))
		j = 0
data = []

for i in range(len(metals)):
	for j in range(len(metals[0])):
		data.append(metals[i][j])

print(data)
