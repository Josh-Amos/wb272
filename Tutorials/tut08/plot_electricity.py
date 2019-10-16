import sys
import numpy as np
import matplotlib.pyplot as plt

def plot():

	data = [("BFM",61,91),("CTN",87,94),("DBN",74,90),("ELN",47,81),
			("GER",75,82),("JHB",85,91),("PEZ",71,90),("PTA",77,89) ]
	N = len(data)
	axes = plt.gca()
	axes.set_ylim([0,100])
	x = np.arange(1, N + 1)
	y1 = [num for (s, num, z) in data]
	y2 = [z for (s, num, z) in data]
	labels = [s for (s, num, z) in data]
	width = 1
	plt.bar(x, y1, 0.25, color="orange")
	plt.bar(x + 0.25, y2, 0.25, color="blue")
	plt.ylabel("Electricity")
	plt.xticks(x + 0.125, labels)
	plt.show()

if __name__ == "__main__":
	plot()
