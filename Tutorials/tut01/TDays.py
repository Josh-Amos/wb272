def day_of_the_week(y,m,d):
	"""A function that returns the day of the week the date falls on"""
	y0 = y - (14 - m)// 12
	x  = y0 + y0 // 4 - y0// 100 + y0// 400
	m0 = m + 12 * ((14 - m) // 12) - 2
	d0 = (d + x + (31 * m0)//12) % 7
	
	return d0
