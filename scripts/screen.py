#!/usr/bin/env python3.6


import curses
import os
import time
import sys
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def csv_path():
    return os.path.join(os.path.dirname(__file__), os.path.pardir, "data", "metrics.csv")


def summary(window):
    while True:
        last = int(sys.argv[1]) if len(sys.argv) == 2 else 50

        network = pd.read_csv(csv_path())

        last = min(last, len(network))

        network = network.tail(last)
        network['time_raw'] = network.apply(lambda row: datetime.strptime(row.time, "%Y-%m-%d %H:%M:%S"), axis=1)
        status_table = network.status.value_counts()
        offline_idx = (network.status == "offline")
        offline_count = sum(offline_idx)
        network = network.drop(network[offline_idx].index)
        last_metric = network.tail(1).values[0]
        last_str = "{} - ping: {:.2f} ms, upload: {:.2f} Mbps, download: {:.2f} Mbps"\
                    .format(last_metric[0], last_metric[1], last_metric[2], last_metric[3])

        window.addstr(0, 0, "Summary statistics for the last {} observations".format(last))
        window.addstr(2, 0, "Since {}".format(network.time.iloc[0], network.time.iloc[-1]))
        window.addstr(3, 0, "Until {}".format(network.time.iloc[-1]))
        window.addstr(5, 0, "Online {}".format(last - offline_count))
        window.addstr(6, 0, "Offline {} (ignored)".format(offline_count))
        window.addstr(8, 0, "Last {}".format(last_str))
        window.addstr(10, 0, str(network[['time_raw', 'ping', 'upload', 'download']].describe()))

        window.refresh()


def main():
    curses.wrapper(summary)


if __name__ == '__main__':
    main()
