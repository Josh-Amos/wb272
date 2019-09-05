def triangle(n):

	for i in range(1,n + 1):
		print("X" * i)


def triangle_2(n):
	
	for i in range(1, n + 1):
		char = ""
		for j in range(i):
			char = char + "X"
		print(char)

def triangle_3(n):
	
	i = 1
	j = 0
	char = ""
	
	while i < n + 1:
		while j < i:
			char = char + "X"
			j += 1

		print(char)
		i += 1
