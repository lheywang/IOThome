# ==================================================================================================
# file :        devices/speaker.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Flask blueprint to provide the speaker functions calls
# ==================================================================================================

# devices/switch.py
from flask import Blueprint, render_template, request  # type: ignore

# Create the Blueprint
speaker_bp = Blueprint("speaker", __name__, template_folder="templates")


@speaker_bp.route("/speaker.html")
def switch_page():
    return render_template("devices/speaker.html")


@speaker_bp.route("/speaker/command", methods=["POST"])
def handle_switch_command():
    # Get data from the POST request
    print(request)
