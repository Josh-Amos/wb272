def end_time():
	"""Returns the end time after adding the minutes to the start time"""
	
	prompt1 = input("Start time: ")
	prompt2 = int(input("Duration: "))
	StartTime = ((int(prompt1) // 100 ) * 60 ) + (int(prompt1) % 100)
	#StartTime = int(prompt[:2]) * 60 + int(prompt[2:])
    
	Duration = StartTime + prompt2
    
	#To help with the running over
	# 1440 minutes = 1440 / 60 = 24 hours
	Duration = Duration % 1440
	Hour = Duration // 60
	Minutes = Duration - (60 * Hour)
    
	#Left-alignment
	Min = "{:0<2}".format(str(Minutes))
	#Right-alignment
	Hr = "{:0>2}".format(str(Hour))
	EndTime = Hr + Min
    
	return EndTime
