import numpy as np
import matplotlib.pyplot as plt

def plot04():
    data = [(1, 0), (2, 0.1), (3, 1.1), (4, 1.2), (5, 2.3),
            (6, 3.5), (7, 5.8)]
    X = [x for (x, y) in data if x > 2]
    Y = [y for (x, y) in data if x > 2]
    plt.plot(X, Y, ":rs")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.show()

if __name__ == "__main__":
    plot04()
