def parallelogram(s):
	w = ""
	v = ""
	for i in range(0, len(s)):
		w = w + s[i]
		v = "{:>{l}}".format(w, l=len(s))
		if (w == s):
			print(w)
			for j in range(1, len(s)):
				w = s[j:]
				print(w)
			break;
		else:
			print(v)


def parallelogram_2(L):
	L = L.upper()
	s = 2 * -len(L) + 1
	span = len(L)
	k = " "
	for i in range(1,2 * len(L)):
		print("{0:>{a}}".format(L[s:i], a=span))
		L += k
