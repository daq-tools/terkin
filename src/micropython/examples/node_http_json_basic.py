# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@terkin.org>
"""
Synopsis::

    # Install "uterkin" library
    micropython -m upip install micropython-uterkin

    # Run example program
    micropython examples/node_http_json_basic.py

"""
from uterkin.telemetry import TelemetryNode

if __name__ == '__main__':

    # Create a "Node API" telemetry client object
    telemetry = TelemetryNode('http://localhost:9999/api')

    # Setup telemetry object
    telemetry.setup()

    # Transmit data
    data = {"temperature": 42.84, "humidity": 83};
    print(telemetry.transmit(data))

