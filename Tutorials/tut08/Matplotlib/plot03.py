import numpy as np
import matplotlib.pyplot as plt

def plot03():
    x = [1, 2, 3, 4, 6, 5, 7]
    y = [1, 2, 4, 3, 6, 5, 7]
    plt.plot(x, y, ":gs")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.show()

if __name__ == "__main__":
    plot03()
