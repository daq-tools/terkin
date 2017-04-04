###################
micropython-uterkin
###################



************
Introduction
************
A convenient data acquisition and telemetry client framework for MicroPython.

It handles simple scenarios as well as more advanced ones using the
same API interfaces, just add a little more sugar.

It supports the transports:

- HTTP
- MQTT

as well as the serialization formats:

- x-www-form-urlencoded
- JSON
- CSV



********
Synopsis
********
.. highlights:: python
::

    from uterkin.telemetry import TelemetryNode

    # Setup
    telemetry = TelemetryNode('http://localhost:9999/api')
    telemetry.setup()

    # Transmit
    data = {"temperature": 42.84, "humidity": 83};
    telemetry.transmit(data)


The library is agnostic of the physical transport, so using MQTT is just about::

    telemetry = TelemetryNode('mqtt://localhost/hello/42')



*******
Hacking
*******
This is about running the examples inside the working tree, i.e. development mode.

Synopsis::

    # Go to directory
    cd terkin/src/micropython

    # Announce path to micropython binary
    export PATH=$PATH:~/dev/foss/fetched/micropython/unix

    # Run example
    micropython -c 'import sys; sys.path.insert(0, ".")' examples/node_http_json_wan.py



*************
Build package
*************
::

    python3 setup.py sdist



*******
License
*******
The MIT License (MIT)

Copyright (c) 2017 The Terkin Contributors


Terkin for MicroPython is licensed using the same license as the MicroPython libraries ported from Core Python,
see https://github.com/micropython/micropython-lib/blob/master/LICENSE.

