def volume(A,h,d):
	"""Solves the volume of a pyramid to some precision point"""
	volume = (A * h) / 3
	answer = '{0:.{prec}f}'.format(volume, prec = d)
	return answer
