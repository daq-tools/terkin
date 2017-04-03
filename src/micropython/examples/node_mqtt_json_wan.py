# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@terkin.org>
"""
Synopsis::

    # Install "uterkin" library
    micropython -m upip install micropython-uterkin

    # Run MQTT subscriber
    mosquitto_sub -h swarm.hiveeyes.org -t 'hiveeyes/testdrive/#' -v

    # Run example program
    micropython examples/node_mqtt_json_wan.py

"""
from uterkin.telemetry import TelemetryNode, TelemetryTopologies

# Create a "Node API" telemetry client object
telemetry = TelemetryNode(
    #"https://swarm.hiveeyes.org/api",
    #"http://swarm.hiveeyes.org/api-notls",
    "mqtt://swarm.hiveeyes.org",
    address = {
        "realm":    "hiveeyes",
        "network":  "testdrive",
        "gateway":  "area-42",
        "node":     "node-1",
    },
    topology = TelemetryTopologies.KotoriWanTopology
)

# Setup telemetry object
telemetry.setup()

# Transmit data
data = {"temperature": 42.84, "humidity": 83};
print(telemetry.transmit(data))
