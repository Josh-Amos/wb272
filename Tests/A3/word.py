def diamond(s):
	mid = ''
	index = 0
	v = ''
	midp = ''
	i = 1
	k = 1
	L = []

	if len(s) % 2 == 0:
		index = len(s) // 2
		mid = s[index- 1: index + 1]	
		midp = '{0:^{length}}'.format(mid, length=len(s))
		print(midp)
		while 2*i < len(s):
			v = s[index - 2*i] + mid + s[index + i]
			v = '{0:^{length}}'.format(v, length=len(s))
			print(v)
			i += 1
		while 2*i < len(s):
			v = s[index -2*i] + mid + s[index + 2*i]
			v = '{0:^{length}}'.format(v, length=len(s))
			if (v == s):
				i -= 1
			else:
				print(v)
				i -= 1
		print(midp)
	else:
		index = len(s) // 2
		mid = s[index] 
		mid = '{0:^{length}}'.format(mid, length=len(s))
		print(mid)
		while 2*i < len(s):
			v = s[index - i: index + 2*i]
			v = '{0:^{length}}'.format(v, length=len(s))
			print(v)
			i += 1
		while 2*i > len(s):
			v = s[index - i: index + 2*i]
			v = '{0:^{length}}'.format(v, length=len(s))
			if (v == s):
				i -= 1
			else:
				print(v)
				i -= 1
		print(mid)
