import numpy as np
import matplotlib.pyplot as plt

def plot10():
    t = np.arange(0, 200, 1)
    N = len(t)
    y1 = np.random.rand(N)
    delta = np.random.rand(N)
    y2 = y1 + delta / 2
    x = np.arange(1, N + 1)
    plt.fill_between(x, 0, y1, color="m")
    plt.fill_between(x, y1, y2, color="y")
    plt.axis([0, N, 0, max(y2)])
    plt.show()

if __name__ == "__main__":
    plot10()
