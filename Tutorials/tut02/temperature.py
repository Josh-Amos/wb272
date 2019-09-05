def f2c(temp,precision):
	celcius = (temp - 32) * 5/9
	answer = '{0:.{prec}f}'.format(celcius,prec = precision)
	return answer	
			
