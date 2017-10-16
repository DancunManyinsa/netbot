#!/usr/bin/env python3.6


import pyspeedtest as pst
import time
from collections import namedtuple
from datetime import datetime


class Metric:
    def __init__(self, ping, upload, download, status_ok, *,
                 unit_time='ms', unit_bandwidth='bps'):
        self.ping = ping
        self.upload = upload
        self.download = download
        self.status_ok = status_ok
        self.time = datetime.now()

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
                .format(self.time.strftime("%Y-%m-%d %H:%M:%S"), self.ping, self.upload, self.download)
        else:
            return "{} - no connection".format(self.time.strftime("%Y-%m-%d %H:%M:%S"))


def main():
    st = pst.SpeedTest()

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

        print(metric)

        time.sleep(20)


if __name__ == '__main__':
    main()
