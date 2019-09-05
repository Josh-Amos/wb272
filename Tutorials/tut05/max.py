def find_max(L,i):
    Max = L[i]
    for item in L[i:]:
        if item > Max:
            Max = item
    
    return Max
