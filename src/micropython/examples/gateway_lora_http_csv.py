# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@terkin.org>
from uterkin.lopy_lora_server import server
from uterkin.telemetry import CSVTelemetryNode

class LoRaHttpCsvGateway:

    def __init__(self):

        # Create a "Node API" telemetry client object
        self.telemetry = CSVTelemetryNode(
            "http://swarm.hiveeyes.org/api-notls",
            {
                "realm":    "hiveeyes",
                "network":  "testdrive",
                "gateway":  "area-42",

                # Node ID is obtained from call to ``.transmit``
                "node":     None,
            }
        )

        self.lora_server = server(callback=self.forward_lora_to_backend)

    # Forward data
    def forward_lora_to_backend(self, lora_message):
        """
        lora_message.control
        lora_message.deviceID
        lora_message.Seq
        lora_message.indicator1
        lora_message.indicator2
        lora_message.stype
        lora_message.svalue
        lora_message.check
        """
        outcome = self.telemetry.transmit(lora_message.svalue, node=str(lora_message.deviceID))
        return outcome

    # Run LoRa receiver server
    def run(self):
        while True:
            success = self.lora_server.update()
            print('success:', success)


if __name__ == '__main__':
    gateway = LoRaHttpCsvGateway()
    gateway.run()

