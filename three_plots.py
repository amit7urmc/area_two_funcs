import matplotlib.pyplot as plt

def x_y_values(n):
    x = [x/100 for x in range(0,101)]
    y_n = list(map(lambda i: i**n, x))
    y_1_n = list(map(lambda i: i**(1.0/n), x))
    return {"x": x, "y_n": y_n, "y_1_n": y_1_n}

def plot(x_y, n, ax):
    ax.plot(x_y["x"], x_y["y_n"], c=[0,0,0], linestyle="--")
    ax.plot(x_y["x"], x_y["y_1_n"], c=[0,0,0])
    ax.set_title(f"For n={n}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend(["x^n","x^(1/n)"])
    ax.set_aspect(1.0)

if __name__ == "__main__":
    fig, ax = plt.subplots(nrows=1, ncols=3, sharey=True)

    x_y_2 = x_y_values(2)
    plot(x_y_2, 2, ax[0])

    x_y_3 = x_y_values(3)
    plot(x_y_3, 3, ax[1])

    x_y_10 = x_y_values(10)
    plot(x_y_10, 10, ax[2])

    fig.suptitle("The area made by intersection grows as n grows", y=0.85)
    plt.show()