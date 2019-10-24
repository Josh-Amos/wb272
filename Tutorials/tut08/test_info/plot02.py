import sys
import numpy as np
import matplotlib.pyplot as plt

def plot(marks_txt):
	
	N = 10
	hist = [0] * N
	marks = []
	mod = 0
	f = open(marks_txt, "r")

	for line in f:
		line = line.replace("\n", "")
		marks = line.split(",")
		mod = int(marks[1]) // N
		if 1 <= mod <= 10:
			hist[mod - 1] += 1
	
	num_bins = 10
	n, bins, patches = plt.hist(hist, num_bins, normed=1,
	facecolor="lightblue", alpha = 0.51)
	#width = 1.0
	#x = np.arange(1, N+1)
	#plt.bar(np.arange(0, N), hist, width, color="lightblue")
	#plt.xlabel("Bins")
	#plt.ylabel("Frequency counts")
	#plt.xticks(np.arange(1, N +1))
	plt.show()
	f.close()

if __name__ == "__main__":
	plot(sys.argv[1])
