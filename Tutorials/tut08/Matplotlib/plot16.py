import numpy as np
import matplotlib.pyplot as plt

def plot16():
    #samples1 = np.array([1, 1, 1, 3, 2,  5, 1, 10, 10, 0])
    #samples2 = np.array([6, 6, 6, 1, 2, 3, 9, 12])
    samples1 = []
    for i in range(50):
        samples1.append(np.random.randint(1, 11))
    samples2 = []
    for i in range(30):
        samples2.append(np.random.randint(1, 11))


    N = 10
    hist1 = [0] * N
    hist2 = [0] * N

    # create two histograms
    for v in samples1:
        if 1 <= v <= 10:
            hist1[v-1] += 1
    for v in samples2:
        if 1 <= v <= 10:
            hist2[v-1] += 1

    # display the bar graph
    width = 1.0
    plt.bar(np.arange(0, N), hist1, width/2., color="orange")
    plt.bar(np.arange(0, N) + 0.5, hist2, width/2., color="lightblue")
    plt.xlabel("Bins")
    plt.ylabel("Frequency counts")
    plt.xticks(np.arange(1, N+1))
    plt.show()

if __name__ == "__main__":
    plot16()
