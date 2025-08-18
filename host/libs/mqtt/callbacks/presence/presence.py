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


class presence_handler:
    def __init__(self):
        self.presences = {}
        return

    def parse_payload(self, topic, payload, client, userdata):

        # First, fetch the device name (with topic)
        dev = str(topic).replace("presence/", "")

        # Add / Update the timestamp of the device.
        self.presences[dev] = time.time()

        print(self.presences)

        return

    def get_device_deltas(self) -> dict:
        # Function init
        act = time.time()
        retdict = {}

        # Get the deltas betweens each devices
        for dev in self.presences:
            retdict[dev] = int(act - self.presences[dev])

        return retdict

    def get_active_devices(self) -> dict:
        # Get the deltas between the devices
        device_delta = self.get_device_deltas()

        print(device_delta)

        # Compare them to a threshold
        THRESHOLD = 10

        for dev in device_delta:
            device_delta[dev] = (device_delta[dev], (device_delta[dev] < THRESHOLD))

        return device_delta
