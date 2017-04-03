# -*- coding: utf-8 -*-
# (C) 2017 constantinos
# https://forum.pycom.io/post/4860
import gc
import time
import struct
import socket
from network import LoRa

LORA_MSG_FORMAT = "LLBBBBlB"


class incoming_message:
    def __init__(self, data):
        self.control, self.deviceID, self.Seq, self.indicator1,  self.indicator2,  self.stype,  self.svalue,  self.check = struct.unpack(LORA_MSG_FORMAT, data)
        #self.control is something added from RFM95. Just discard it. Your message starts from the 5th byte

class server:
    def __init__(self, callback=None):
        self.callback = callback
        cfg_mode = LoRa.LORA
        cfg_freq = 868000000
        cfg_bandwidth=LoRa.BW_125KHZ        # LoRa.BW_125KHZ or LoRa.BW_250KHZ
        cfg_sf = 7                          # Accepts values between 6 and 12.
        #  6 =   64  Chips/Symbol
        #  7 =  128  Chips/Symbol
        #  8 =  256  Chips/Symbol
        #  9 =  512  Chips/Symbol
        # 10 = 1024  Chips/Symbol
        # 11 = 2048  Chips/Symbol
        # 12 = 4096  Chips/Symbol

        cfg_preamble=8                      #configures the number of pre-amble symbols. The default value is 8
        cfg_coding_rate=LoRa.CODING_4_5     #LoRa.CODING_4_5, LoRa.CODING_4_6, LoRa.CODING_4_7 or LoRa.CODING_4_8
        cfg_power_mode=LoRa.ALWAYS_ON       #LoRa.ALWAYS_ON, LoRa.TX_ONLY or LoRa.SLEEP

        self.lora = LoRa(mode=cfg_mode, frequency=cfg_freq, bandwidth=cfg_bandwidth, sf=cfg_sf, preamble=cfg_preamble, coding_rate=cfg_coding_rate,  rx_iq=True, power_mode=cfg_power_mode)
        self.lora.init(mode=LoRa.LORA,
            frequency=868000000,
            tx_power=14,
            bandwidth=LoRa.BW_125KHZ,
            sf=7,
            preamble=8,
            coding_rate=LoRa.CODING_4_5,
            power_mode=LoRa.ALWAYS_ON,
            tx_iq=False,
            rx_iq=False)
        self.lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self.lora_sock.setblocking(False)
    def update(self):
        raw_data = self.lora_sock.recv(61)

        if raw_data:
            try:
                msg = incoming_message(raw_data)
                if msg.deviceID % msg.Seq == msg.check:
                    print("msg received. devid:", msg.deviceID,  " seq:", msg.Seq)
                    if self.callback:
                        return self.callback(msg)
                else:
                    print("msg check failed")
            except:
                print("msg failed to parse")
        else:
            pass

def test_server():
    srv = server()
    while True:
        srv.update()

if __name__ == '__main__':
    test_server()

