import numpy as np
import matplotlib.pyplot as plt

def plot09():
    t = np.arange(0, 200, 1)
    N = len(t)
    y = np.random.rand(N)
    x = np.arange(1, N+1)
    labels = ["data" + str(k) for k in range(1, N + 1)]
    samples = [''] * N
    for i in range(0, N, N // 5):
        samples[i] = labels[i]
    width = 1
    plt.fill_between(x, 1, y, color='b')
    plt.ylabel("Intensity")
    plt.xticks(x + width / 2, samples)
    plt.show()

if __name__ == "__main__":
    plot09()
