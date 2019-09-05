
def is_valid_usnum(num):
	s = str(num)
	l = []
	
	for i in range(len(s)):
		l.append(int(s[i]))
	
	for i in range(1,len(l) + 1):
		l[-i] = i * l[-i]
	
	checksum = sum(l) % 11
	
	return checksum == 0

def is_valid_usnum2(num):
	a = []
	
	for i in range(len(num)):
		a.append(num[i])
	
	for i in range(1,len(a) + 1):
		a[-i] = i * int(a[-i])
	
	checksum = sum(a) % 11
	
	return checksum == 0

def control(a):
	char = ['0','1','2','3','4','5','6','7','8','9']
	s = str(a)
	num = []
	mod = []
	
	for i in range(len(s)):
		num.append(int(s[i]))

	for i in range(1, len(num) + 1):
		num[-i] = (i + 1) * num[-i]
	
	total = sum(num)
	
	for i in range(len(char)):
		mod.append((total + int(char[i])) % 11)
	
	control = char[mod.index(0)]
	stdnum = s + control
	
	return stdnum,control
