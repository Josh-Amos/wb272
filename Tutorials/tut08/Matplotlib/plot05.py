import numpy as np
import matplotlib.pyplot as plt

def plot05():
    t = np.arange(1, 10, 0.01)
    print(len(t))
    plt.plot(t, t**2, "r-", t, 3*(t**2), "b-")
    plt.show()

if __name__ == "__main__":
    plot05()
