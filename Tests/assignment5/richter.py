def category(mag):
	"""A function that returns the category of the earthquake related to the magnitude"""
	magn = "{0:.1f}".format(mag)
	f = float(magn)
	
	if f < 3.0:
		return "micro"
	if 3.0 <= f <= 3.9:
		return "minor"
	if 4.0 <= f <= 4.9:
		return "light"
	if 5.0 <= f <= 5.9:
		return "moderate"
	if 6.0 <= f <= 6.9:
		return "strong"
	if 7.0 <= f <= 7.9:
		return "major"
	if f >= 8.0:
		return "great"
