# ==================================================================================================
# file :        api/status.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Flask blueprint to provide the API to get the devices status
# ==================================================================================================

# devices/switch.py
from flask import Blueprint, request, current_app, jsonify  # type: ignore

# Create the Blueprint
api_status_bp = Blueprint("api", __name__, template_folder="templates")


@api_status_bp.route("/status")
def apo_status():
    # Get the differents devices status
    mqtt_client = current_app.config["mqtt_client"]
    devices = mqtt_client.presence_handler.get_active_devices()

    # Ensure all devices are presents
    names = ["temperature", "player", "speaker", "switch"]
    for name in names:
        if not name in devices:
            devices[name] = (-1, False)

    return jsonify(devices)
