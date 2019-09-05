def get_change(Due,Payed):
    change = Payed - Due
    R5 = change // 5
    change = change - (5 * R5)
    R2 = change // 2
    change = change - (2 * R2)
    R1 = change // 1
    return R5,R2,R1
    
     
