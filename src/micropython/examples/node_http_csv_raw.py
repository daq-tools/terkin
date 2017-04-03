# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@terkin.org>
"""
Synopsis::

    # Install "uterkin" library
    micropython -m upip install micropython-uterkin

    # Run example program
    micropython examples/node_http_csv_raw.py

"""
from uterkin.telemetry import CSVTelemetryNode, TelemetryTopologies

# Create a "Node API" telemetry client object
telemetry = CSVTelemetryNode(
    #"https://swarm.hiveeyes.org/api",
    "http://swarm.hiveeyes.org/api-notls",
    #"mqtt://swarm.hiveeyes.org",
    address = {
        "realm":    "hiveeyes",
        "network":  "testdrive",
        "gateway":  "area-42",

        # Node ID is obtained from call to ``.transmit``
        "node":     None,
    },
    topology = TelemetryTopologies.KotoriWanTopology
)

# Setup telemetry object
telemetry.setup()

# Transmit header
success = telemetry.transmit('## temperature, humidity, weight', node='node-1')

# Transmit data
success = telemetry.transmit('42.42, 84.84, 35', node='node-1')
