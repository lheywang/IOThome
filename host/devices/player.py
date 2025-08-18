# ==================================================================================================
# file :        devices/player.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Flask blueprint to provide the player functions calls
# ==================================================================================================

# devices/switch.py
from flask import Blueprint, render_template, request  # type: ignore

# Create the Blueprint
player_bp = Blueprint("player", __name__, template_folder="templates")


@player_bp.route("/player.html")
def switch_page():
    return render_template("devices/player.html")


@player_bp.route("/player/command", methods=["POST"])
def handle_switch_command():
    # Get data from the POST request
    print(request)
