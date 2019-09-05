def elapsed_minutes(time1,time2):
	hoursToMin = ( int(time2[:2]) - int(time1[:2]) )* 60
	minutes = hoursToMin + (int(time2[2:]) - int(time1[2:]))
	return minutes
