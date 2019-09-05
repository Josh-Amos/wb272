def time_sum(time1,time2):
    """Calculates the sum of two times"""
    
    t1 = "{:0>4}".format(time1)
    t2 = "{:0>4}".format(time2)
    Hrs = int(t1[:2]) + int(t2[:2])
    Min = (int(t1[2:]) + int(t2[2:]))
    floor = Min // 60
    
    Uphrs = Hrs + floor
    UpMin = Min - (floor * 60)
    
    Hrt = "{:0>2}".format(Uphrs)
    Mint = "{:0>2}".format(UpMin)
    time = Hrt + Mint
   
    return time
