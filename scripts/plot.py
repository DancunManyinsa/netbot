#!/usr/bin/env python3.6


import os
import sys
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def csv_path():
    return os.path.join(os.path.dirname(__file__), os.path.pardir, "data", "metrics.csv")

def main():
    last = int(sys.argv[1]) if len(sys.argv) == 2 else 50

    metrics_csv = os.path.join(os.path.dirname(__file__), )
    network = pd.read_csv(csv_path())

    last = min(last, len(network))

    network = network.tail(last)
    network['time_raw'] = network.apply(lambda row: datetime.strptime(row.time, "%Y-%m-%d %H:%M:%S"), axis=1)
    network = network.drop(network[network.status == "offline"].index)

    fig, axes = plt.subplots(3, 1, sharex=True)
    fig.subplots_adjust(hspace=0.1)

    fig.suptitle("Ping, upload and download for the last {} observations".format(last))

    for i, (metric, unit) in enumerate(zip(['ping', 'upload', 'download'], ['ms', 'Mbps', 'Mbps'])):
        metric_mean = np.mean(network[metric])

        axes[i].plot(network['time_raw'], network[metric], label="{} ({})".format(metric, unit))
        axes[i].axhline(y=metric_mean, color='r', linestyle='-', label="mean: {:.2f}".format(metric_mean))
        axes[i].legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, frameon=True)
        axes[i].set(ylabel=metric)

    axes[i].set_xlabel("Time")

    plt.show()


if __name__ == '__main__':
    main()
