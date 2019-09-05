def elapsed_minutes2(a,b):
	"""A function that returns the elapsed minutes between two military times"""
	hr1 = int(a[:2]) * 60
	hr2 = int(b[:2]) * 60
	min1 = int(a[2:])
	min2 = int(b[2:])
	
	time1 = hr1 + min1
	time2 = hr2 + min2
	
	return time2 - time1   

def elapsed_minutes(a,b):
	"""A function that returns the elapsed minutes between two military times"""
	hr1 = (int(a) // 100) * 60
	hr2 = (int(b) // 100) * 60 
	min1 = int(a) % 100
	min2 = int(b) % 100
	
	time1 = hr1 + min1
	time2 = hr2 + min2
	
	return time2 - time1
