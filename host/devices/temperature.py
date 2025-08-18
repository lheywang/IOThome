# ==================================================================================================
# file :        devices/temperature.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Flask blueprint to provide the temperature sensor functions calls
# ==================================================================================================


# devices/switch.py
from flask import Blueprint, render_template, request  # type: ignore

# Create the Blueprint
temperature_bp = Blueprint("temperature", __name__, template_folder="templates")


@temperature_bp.route("/temperature.html")
def switch_page():
    return render_template("devices/temperature.html")


@temperature_bp.route("/temperature/command", methods=["POST"])
def handle_switch_command():
    # Get data from the POST request
    print(request)
