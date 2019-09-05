
def isbn13_to_10(is13):
    
    is9 = is13[3:12]
    digits = ["0","1","2","3","4","5","6","7","8","9","10"]
    index  = ["0","1","2","3","4","5","6","7","8","9","X"]
    num = [] 
    solved = []
    mod = []
    
    for i in range(len(is9)):
        num.append(int(is9[i]))
   
    for i in range(2,len(num) + 2):
        num[-i + 1] = num[-i + 1] * i
    
    checksum = sum(num)
        
    for i in range(len(digits)):
        solved.append(checksum + int(digits[i]))
    
    for i in range(len(solved)):
        mod.append(solved[i] % 11)
        
    check = mod.index(0)
    check = index[check]
    
    is10 = is9 + check
        
    return is10
       
    
    
