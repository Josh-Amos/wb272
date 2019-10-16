import numpy as np
import matplotlib.pyplot as plt

def plot12():
    data = [("data1", 34), ("data2", 22), ("data3", 11),
            ("data4", 28), ("data5", 57), ("data6", 39),
            ("data7", 23), ("data8", 98)]
    N = len(data)
    x = np.arange(1, N+1)
    y = [num for (s, num) in data]
    labels = [s for (s, num) in data]
    width = 1
    plt.bar(x, y, width, color="y")
    plt.ylabel("Intensity")
    plt.xticks(x + width / 2, labels)
    plt.show()

if __name__ == "__main__":
    plot12()
