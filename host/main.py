# ==================================================================================================
# file :        main.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Main file for the IOTHome web server ! Provide root functions as well as include of subfiles
# ==================================================================================================
## Imports
# Default libs
import time
import os

# Modules
from flask import Flask, render_template, Response  # type: ignore

# Files
from devices import switch_bp, player_bp, speaker_bp, temperature_bp

# Openning app
app = Flask(__name__)

# Including blueprints
app.register_blueprint(switch_bp, url_prefix="/devices")
app.register_blueprint(player_bp, url_prefix="/devices")
app.register_blueprint(temperature_bp, url_prefix="/devices")
app.register_blueprint(speaker_bp, url_prefix="/devices")


# First functions
@app.route("/")
@app.route("/index.html")
def hello_world():
    return render_template("index.html")


# Launching the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
