# ==================================================================================================
# file :        api/status.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Flask blueprint to provide the API to get the devices status
# ==================================================================================================
# STD
import time

# devices/switch.py
from flask import Blueprint, request, current_app, jsonify  # type: ignore

# Files
from libs.database import (
    get_all_device_status,
    update_device_bool,
    update_device_status,
)

# Create the Blueprint
api_status_bp = Blueprint("api", __name__, template_folder="templates")


# API to fetc the status of the devices
@api_status_bp.route("/status")
def api_status():
    # First, fetch the known devices on the database and actual time
    devices = get_all_device_status()
    act = time.time()

    # Fill an output dict with the keys :
    out = dict()
    THRESHOLD = 15
    for device in devices:
        # Get device status
        diff = act - device[1]
        status = diff < THRESHOLD

        # Update on the output dict, and then database
        out[device[0]] = (diff, status)
        update_device_bool(device[0], status)

    # Get the differents devices status
    return out


# API to update a device with any possible device
@api_status_bp.route("/presence/<string:device>")
def api_presence(device: str):
    update_device_status(device, True)
    return "OK"
