import numpy as np
import matplotlib.pyplot as plt

def plot14():
    # number of bins
    N = 10

    # the samples
    samples = np.array([1, 1, 1, 3, 2, 5, 1, 10, 10, 0])

    n, bins, patches = plt.hist(samples, N, facecolor="orange",
                                range=[0, N], density=False)
    print("n =", n)
    print("bins =", bins)
    print("patches =", patches)
    plt.xlabel("bins")
    plt.ylabel("Probability")
    plt.show()
    
if __name__ == "__main__":
    plot14()
