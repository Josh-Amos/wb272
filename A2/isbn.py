def isbn10to13(a):
    """Converts an isbn10 number to an isbn13 number"""
    
    a = "978" + a[:len(a) - 1]
    
    print(a)
    num = []
    index  = ["0","1","2","3","4","5","6","7","8","9","X"]
    digits = [0,1,2,3,4,5,6,7,8,9,10]
    mod = []
     
    for i in range(len(a)):
        num.append(int(a[i]))
    
    for i in range(1,len(num),2):
        num[i] = 3 * num[i]
    
    checksum = sum(num)
        
    for i in range(len(digits)):
        mod.append((checksum + digits[i]) % 10)
        
    control = mod.index(0)
    control = index[control]
    
    return a + control
    
        
        
    
    
         
        
