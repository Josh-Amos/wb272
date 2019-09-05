def end_time():

    prompt1 = input("Start time: ")
    prompt2 = int(input("Duration: "))
    StartTime = ((int(prompt1) // 100 ) * 60 ) + (int(prompt1) % 100)
    
    Duration = StartTime + prompt2
    
    #To help with the running over
    Duration = Duration % 1440
    Hour = Duration // 60
    Minutes = Duration - (60 * Hour)
    
    Min = "{:0<2}".format(str(Minutes))
    Hr = "{:0>2}".format(str(Hour))
    EndTime = Hr + Min
    
    return EndTime
