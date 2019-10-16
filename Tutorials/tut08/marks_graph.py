import sys
import numpy as np
import matplotlib.pyplot as plt

N = 10
hist = [0] * 10


def plot(input_file):

	marks = []
	mod = 0

	f = open(input_file, "r")
	for line in f:
		line = line.replace("\n", "")
		marks = line.split(" ")
		for i in range(0, len(marks)):
			mod = int(marks[i]) // N
			if 1 <= mod <= 10:
				hist[mod - 1] += 1
	
	width = 1.0
	x = np.arange(1, N + 1)
	plt.bar(np.arange(0, N), hist, width, color="orange")
	plt.xlabel("Bins")
	plt.ylabel("Frequency counts")
	plt.xticks(np.arange(1, N + 1))
	plt.show()

	f.close()





if __name__ == "__main__":
	plot(sys.argv[1])
