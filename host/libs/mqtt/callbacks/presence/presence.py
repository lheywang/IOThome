# ==================================================================================================
# file :        libs/mqtt/callbacks/presence/presence.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Provide callback functions for the presences parser
# ==================================================================================================
# STD imports
import time
import threading
import os
from flask import current_app  # type: ignore


class presence_handler:
    def __init__(self):
        self.devices = dict()

        # Ensure all devices are presents
        names = ["temperature", "player", "speaker", "switch"]
        for name in names:
            self.devices[name] = (-1, False)
        print(self.devices)

        return

    def parse_payload(self, topic, payload, client, userdata):

        # First, fetch the device name (with topic)
        device = str(topic).replace("presence/", "")
        time.time()

        # Update the internal variable
        self.devices[device] = tuple((time.time(), -1))

        # Compare them to a threshold
        THRESHOLD = 10
        current_app.config["status"] = dict()

        for dev in self.devices:
            if self.devices[dev][0] > 0:
                tmp = time.time() - self.devices[dev][0]
                current_app.config["status"][dev] = (tmp, (tmp < THRESHOLD))
            else:
                current_app.config["status"][dev] = (-1, False)

        print(f" GETTER 2: {current_app.config["status"]}")

        return
