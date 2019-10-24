import sys
import numpy as np
import matplotlib.pyplot as plt

def plot(marks_txt):
	
	N = 50
	hist = [0] * N

	f = open(marks_txt, "r")
	for line in f:
		line = line.replace("\n", "")
		marks = line.split(",")
		hist[int(marks[1]) // (100//N) -1] += 1
	
	labels = [i for i in range(0,101,20)]
	x = np.arange(0,N) + 1.55
	plt.bar(x, hist, 1.0, color="blue")
	plt.xlabel("marks")
	plt.ylabel("Number of students")
	plt.xticks(np.arange(0,N+1, 10), labels)
	plt.show()
	
if __name__ == "__main__":
	plot(sys.argv[1])
