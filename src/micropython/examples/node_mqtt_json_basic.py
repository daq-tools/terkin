# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@terkin.org>
"""
Synopsis::

    # Install "uterkin" library
    micropython -m upip install micropython-uterkin

    # Run MQTT subscriber
    mosquitto_sub -h localhost -t '#' -v

    # Run example program
    micropython examples/node_mqtt_json_basic.py

"""
from uterkin.telemetry import TelemetryNode

if __name__ == '__main__':

    # Create a "Node API" telemetry client object
    telemetry = TelemetryNode('mqtt://localhost/hello/42')

    # Setup telemetry object
    telemetry.setup()

    # Transmit data
    data = {"temperature": 42.84, "humidity": 83};
    print(telemetry.transmit(data))

