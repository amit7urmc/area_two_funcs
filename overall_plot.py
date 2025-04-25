import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = range(1,101)
    frac = list(map(lambda x: (x-1)/(x+1),n))

    fig, ax = plt.subplots(1,1)
    ax.plot(n, frac)
    ax.set_title("the fraction area ($\Delta$) asymptotically reaches 100% for very large values of n")
    ax.set_xlabel("n")
    ax.set_ylabel("Fraction of area $\Delta$")
    plt.show()