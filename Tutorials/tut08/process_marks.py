import sys
import numpy as np
import matplotlib.pyplot as plt

N = 10
hist = [0] * N

def process(marks, s):
	Ass = Test = FM = 0.0
	test_a = []
	array = s.split(",")

	for i in range(0,len(array)):
		if array[i] == "":
			array[i] = "0"

	for i in range(1, len(marks)):
		if i < 9:
			Ass = Ass + (float(array[i]) / float(marks[i]))
		else:
			test_a.append(float(array[i]) / float(marks[i]))

	test_a.sort()
	test_a.reverse()
	test_a.pop()

	Ass = (Ass / 8) * 64
	Test = (sum(test_a)/3) * 36

	FM = Ass + Test
	FM = int(round(FM))
	if 35 <= FM <= 50:
		FM = round5(FM)
	
	hist[int(FM//(100/N))] += 1
	s = s + "," + str(FM) + "\n"
	return s


def create(in_file,out_file):
	
	f = open(out_file, "w")
	file = open(in_file, "r")
	s = ""
	marks = []

	for line in file:
		if line.startswith("S") or line.startswith(","):
			if line.startswith(","):
				marks = line.replace("\n", "").split(",")
				f.write(line.replace("\n",",100\n"))
			else:
				f.write(line.replace("\n", ",Final Mark\n"))
		else:
			s = line.replace("\n", "")
			#process converts array to a string!
			s = process(marks, s)
			f.write(s)

	f.close()

def round5(x):

	y = x % 10
	if (y < 2.5 or 5 <= y < 7.5):
		x -= x % 5
	elif 2.5 <= y < 5:
		x += 5 - (x % 5)
	elif 7.5 <= y < 10:
		x += 10 - y
	
	return int(x)

def plot():
	width = 1.0
	plt.bar(np.arange(0, N), hist, width, color ="orange")
	plt.xlabel("Bins")
	plt.ylabel("Frequency counts")
	plt.xticks(np.arange(0, N))
	plt.show()

if __name__ == "__main__":
	create(sys.argv[1], sys.argv[2])
	plot()
