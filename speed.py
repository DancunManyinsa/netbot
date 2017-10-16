#!/usr/bin/env python3.6


import pyspeedtest as pst
import os
import time
from collections import namedtuple
from datetime import datetime


METRICS = ["time", "ping", "upload", "download", "status"]


class Metric:
    def __init__(self, ping, upload, download, status_ok, *,
                 unit_time='ms', unit_bandwidth='bps'):
        self.ping = ping
        self.upload = upload
        self.download = download
        self.status_ok = status_ok
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self._convert_time_units(unit_time)
        self._convert_bandwitdh_units(unit_bandwidth)

    def _convert_time_units(self, current_unit):
        pass

    def _convert_bandwitdh_units(self, current_unit):
        if current_unit == 'bps':
            self.upload = self.upload/1.0e6
            self.download = self.download/1.0e6
        else:
            pass

    def __str__(self):
        if self.status_ok:
            return "{} - ping: {:.2f} ms, upload: {:.2f} Mbps, download: {:.2f} Mbps"\
                .format(self.time, self.ping, self.upload, self.download)
        else:
            return "{} - no connection".format(self.time)

    def __iter__(self):
        yield self.time
        yield self.ping
        yield self.upload
        yield self.download
        yield "online" if self.status_ok else "offline"


class MetricWriterCSV:
    def __init__(self, file):
        self._file = file

        if not os.path.isfile(self._file) or os.stat(self._file).st_size == 0:
            self._add_header()

    def write(self, metric):
        with open(self._file, 'a') as f:
            line = self._format(metric)
            f.write(line + '\n')

    def _add_header(self):
        with open(self._file, 'w') as f:
            header = ",".join(METRICS)
            f.write(header + '\n')

    def _format(self, metric):
        metric_str = (str(m) for m in metric)
        return ",".join(metric_str)


def main():
    st = pst.SpeedTest()

    csv_file = os.path.join(os.path.dirname(__file__), "metrics.csv")
    csv_writer = MetricWriterCSV(csv_file)

    while True:
        try:
            ping = st.ping()
            upload = st.upload()
            download = st.download()
        except Exception:
            ping, upload, download = 0.0, 0.0, 0.0
            is_online = False
        else:
            is_online = True

        metric = Metric(ping, upload, download, is_online)

        csv_writer.write(metric)
        print(metric)

        time.sleep(20)


if __name__ == '__main__':
    main()
