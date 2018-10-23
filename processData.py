def plot_data(data):
    import matplotlib.pyplot as plt
    import numpy as np

    t = data["time"]
    v = data["voltage"]

    plt.plot(t, v)
    plt.show()


