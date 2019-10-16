import numpy as np
import matplotlib.pyplot as plt

def plot06():
    x1 = [1,  2,  5, 10, 15]
    y1 = [1.5 * x**2 for x in x1]
    x2 = np.arange(5, 30)
    y2 = [0.3 * x**2 for x in x2]
    plt.plot(x1, y1, "rs--", x2, y2,":b^")
    plt.show()

if __name__ == "__main__":
    plot06()
