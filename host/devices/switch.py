# ==================================================================================================
# file :        devices/switch.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Flask blueprint to provide the audio switch functions calls
# ==================================================================================================


# devices/switch.py
from flask import Blueprint, render_template, request, jsonify  # type: ignore

# Create the Blueprint
switch_bp = Blueprint("switch", __name__, template_folder="templates")


@switch_bp.route("/switch.html")
def switch_page():
    return render_template("devices/switch.html")


@switch_bp.route("/switch/command", methods=["POST"])
def handle_switch_command():
    # Get data from the POST request
    print(request)
