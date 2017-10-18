#!/usr/bin/env python3.6


import sys
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    last = int(sys.argv[1]) if len(sys.argv) == 2 else 50

    network = pd.read_csv("metrics.csv")

    last = min(last, len(network))

    network = network.tail(last)
    network['time_raw'] = network.apply(lambda row: datetime.strptime(row.time, "%Y-%m-%d %H:%M:%S"), axis=1)
    status_table = network.status.value_counts()
    offline_idx = (network.status == "offline")
    offline_count = sum(offline_idx)
    network = network.drop(network[offline_idx].index)

    print("Summary statistics for the last {} observations\n".format(last, offline_count))
    print("Since {}".format(network.time.iloc[0], network.time.iloc[-1]))
    print("Until {}\n".format(network.time.iloc[-1]))
    print("Online {}".format(last - offline_count))
    print("Offline {} (ignored)\n".format(offline_count))
    print(network[['time_raw', 'ping', 'upload', 'download']].describe())


if __name__ == '__main__':
    main()
