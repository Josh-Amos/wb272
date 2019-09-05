def f2c(a,d):
	"""Convert fahrenheit to degrees Celsius to d precision"""
	temp = (a - 32) * 5/9
	s = "{:.{prec}f}".format(temp,prec = d)
	return s
