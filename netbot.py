#!/usr/bin/env python3.6


import os
import time

import pyspeedtest as pst

from metrics import Metric, MetricWriterCSV, MetricWriterJSON


def main():
    st = pst.SpeedTest()

    csv_file = os.path.join(os.path.dirname(__file__), "data/metrics.csv")
    csv_writer = MetricWriterCSV(csv_file)

    json_file = os.path.join(os.path.dirname(__file__), "data/metrics.json")
    json_writer = MetricWriterJSON(json_file)

    while True:
        try:
            ping = st.ping()
            upload = st.upload()
            download = st.download()
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception:
            ping, upload, download = 0.0, 0.0, 0.0
            is_online = False
        else:
            is_online = True

        metric = Metric(ping, upload, download, is_online)

        csv_writer.write(metric)
        json_writer.write(metric)
        print(metric)


if __name__ == '__main__':
    main()
