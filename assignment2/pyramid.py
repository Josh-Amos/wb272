def volume(A,h,d):
    volume = (A * h) / 3
    answer = '{0:.{prec}f}'.format(volume, prec = d)
    return answer
