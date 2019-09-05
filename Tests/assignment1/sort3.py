def sort3(a,b,c):
    # Sorts 3 digits in ascending order
    Min = min(min(a,b),c)
    Max = max(max(a,b),c)
    z = max(a,min(b,c))
    x = max(b,min(a,c))
    Mid = min(z,x)
    
    return Min,Mid,Max
