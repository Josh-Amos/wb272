import math

def merc(a0,la,li):
	"""Converts latitude and longitude of a point into a tuple"""	
	x = math.radians(li) - math.radians(a0)
	y = 0.5 * math.log((1 + math.sin(math.radians(la)))/(1 - math.sin(math.radians(la))))
	return (x,y)
