import math

def mercator(ilon,lat,lon):
	x = math.radians(lon) - math.radians(ilon)
	val = (1 + math.sin(lat)) / (1 - math.sin(lat))
	y = 0.5 * math.log(val)
	
	return (x,y)
