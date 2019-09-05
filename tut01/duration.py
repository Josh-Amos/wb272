def elapsed_minutes(time1,time2):
    h1 = int(time2[0:2]) * 60
    min1 = int(time2[2:4])
    h2 = int(time1[0:2]) * 60
    min2 = int(time1[2:4])
    t1 = h1 + min1
    t2 = h2 + min2
    
    return t1 - t2
