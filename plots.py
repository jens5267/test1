import numpy as np
import matplotlib.pyplot as plt


def step_demo(x_range=14):
    x = np.arange(x_range)
    y = np.sin(x / 2)

    plt.step(x, y + 2, where='pre', label='pre (default)')
    plt.plot(x, y + 2, 'o--', color='grey', alpha=0.3)

    plt.step(x, y + 1, where='mid', label='mid')
    plt.plot(x, y + 1, 'o--', color='grey', alpha=0.3)

    plt.step(x, y, where='post', label='post')
    plt.plot(x, y, 'o--', color='grey', alpha=0.3)

    # instead of using "where" you can use "drawstyle":
    # where='pre': drawstyle='steps', where='mid': drawstyle='steps-mid', where='post': drawstyle='steps-post'

    plt.grid(axis='x', color='0.95')
    plt.legend(title='Parameter where:')
    plt.title('plt.step(where=...)')
    plt.show()


def histogram(wind_speeds, samples=437, bin_size=1):
    """
    Plots a histogram of wind speed measurements
    Args:
        wind_speeds (list): wind measurements
        samples (int): number of measurements
        bin_size (int): size of the bins. 1 by default
    """
    # np.random.seed(19680801)
    # example data
    # mu = np.mean(windspeeds)
    mu = 12  # mean of distribution
    # sigma = np.std(x)
    sigma = 4  # standard deviation of distribution
    # x = wind_speeds
    x = mu + sigma * np.random.randn(samples)

    num_bins = 20

    fig, ax = plt.subplots()

    # the histogram of the data
    ax.hist(x, num_bins, density=True, edgecolor="black")
    bins = list(range(0, int(max(x)), bin_size))
    # add a 'best fit' line
    y = [((1 / (np.sqrt(2 * np.pi) * sigma)) *
        np.exp(-0.5 * (1 / sigma * (bin - mu))**2)) for bin in bins]
    ax.plot(bins, y, '--')
    ax.set_xlabel('Wind speed [m/s]')
    ax.set_ylabel('Probability density')
    ax.set_title(f'Histogram of wind speeds: $\mu={mu:.2f}$, $\sigma={sigma:.2f}$')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()

# histogram(wind_speeds=[1])

def sin_waves(x):
    y_values = np.sin(x)
    legend = 'sin(x)'
    # sin_waves = plt.plot(x,y)
    return y_values, legend

    # return sin_waves, legend

def cos_waves(x):
    y_values = np.cos(x)
    legend = 'cos(x)'
    return y_values, legend
    # cos_waves = plt.plot(x,y)

    # return cos_waves, legend


def plot_diagrams(start_value, end_value, steps):
    x = np.arange(start_value, end_value * np.pi, steps)
    legend = []
    for func in [sin_waves, cos_waves]:
        values, description = func(x)
        plt.plot(x, values)
        legend.append(description)
    tick_pos = [np.pi*i for i in list(range(round(max(x)/np.pi)))]
    tick_labels = [f'{i}$\pi$' for i,j in enumerate(tick_pos)]

    plt.xticks(tick_pos, tick_labels)
    plt.legend(legend)

    plt.show()
# plot_diagrams(0, 4, 0.1)


# n = 256
# X = np.linspace(-np.pi, np.pi, n, endpoint=True)
# Y = np.sin(2 * X)

# plt.axes([0.025, 0.025, 0.95, 0.95])

# plt.plot(X, Y + 1, color='blue', alpha=1.00)
# plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

# plt.plot(X, Y - 1, color='blue', alpha=1.00)
# plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
# plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)

# plt.xlim(-np.pi, np.pi)
# plt.xticks(())
# plt.ylim(-2.5, 2.5)
# plt.yticks(())

# plt.show()