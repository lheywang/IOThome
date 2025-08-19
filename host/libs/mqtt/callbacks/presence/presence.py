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

# Files
from libs.database import update_device_status


class presence_handler:
    def __init__(self):
        return

    def parse_payload(self, topic, payload, client, userdata):

        # First, fetch the device name (with topic)
        device = str(topic).replace("presence/", "")

        update_device_status(device, True)

        return
