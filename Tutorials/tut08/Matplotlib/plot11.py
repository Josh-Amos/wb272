import numpy as np
import matplotlib.pyplot as plt

def plot11():
    y = [3, 10, 7,5, -3, 4.5, 6, 8]
    N = len(y)
    x = range(N)
    width = 1 / 1.5
    plt.bar(x, y, width, color="g")
    plt.show()

if __name__ == "__main__":
    plot11()
