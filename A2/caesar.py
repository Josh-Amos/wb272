def cipher(w,n):
    """Encodes each letter of the input text by n positions to the right"""
    
    text = []
    cipher = []
    ci = ""  
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i  in range(len(w)):
        text.append(w[i])
  
    for i in range(len(text)):
        cipher.append(((ord(text[i]) - ord("A")) + n) % 26)
        cipher[i] = alpha[cipher[i]]
        ci += cipher[i]
              
    return ci
