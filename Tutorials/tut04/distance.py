import math


def closest(points):
	"""Returns the the point closests to origin, its index in the list and the distance in the form of a tuple"""
	
	distance = []
	
	for i in range(len(points)):
		for j in range(1,len(points[0])):
			distance.append(math.sqrt(pow(points[i][j-1],2) + pow(points[i][j],2)))
			
	d = min(distance)
	i = distance.index(d)
	p = points[i]

	return (p,i,d)
