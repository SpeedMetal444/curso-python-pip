import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"img/{name} bar.png")
    plt.close()


def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig(f"img/{name} pie_chart.png")
    plt.close()


"""def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
"""

if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 40, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
