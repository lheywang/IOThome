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
def api_status():
    # Get the differents devices status
    return jsonify(current_app.config["status"])
