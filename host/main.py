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
import os
import time
from multiprocessing import Manager

# Modules
from flask import Flask, render_template, send_from_directory  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Files
from devices import switch_bp, player_bp, speaker_bp, temperature_bp
from api import api_status_bp
from libs.mqtt import MQTTClient
from libs.database import setup_db

# -------------------------------------------------------------------------------------------------
# LOAD .env config file
# -------------------------------------------------------------------------------------------------
# Read file
load_dotenv()

# Fetch variables
MQTT_BROKER = str(os.getenv("MQTT_BROKER"))
MQTT_USER = str(os.getenv("MQTT_USER"))
MQTT_PASS = str(os.getenv("MQTT_PASS"))

# -------------------------------------------------------------------------------------------------
# Database access
# -------------------------------------------------------------------------------------------------
# Set-up
setup_db()

# -------------------------------------------------------------------------------------------------
# Flask web server init
# -------------------------------------------------------------------------------------------------

# Openning app
app = Flask("IOTHome")

# Including blueprints
app.register_blueprint(switch_bp, url_prefix="/devices")
app.register_blueprint(player_bp, url_prefix="/devices")
app.register_blueprint(temperature_bp, url_prefix="/devices")
app.register_blueprint(speaker_bp, url_prefix="/devices")
app.register_blueprint(api_status_bp, url_prefix="/api")

# Setting up shared memory locations
app.config["status"] = dict()

# -------------------------------------------------------------------------------------------------
# MQTT init
# -------------------------------------------------------------------------------------------------
mqtt_client = MQTTClient(
    broker=MQTT_BROKER,
    port=1883,
    username=MQTT_USER,
    password=MQTT_PASS,
)
mqtt_client.start()


# Routes to the index.html land page
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


# Redirect the /favicon.icon to the custom defined icon we want
@app.route("/favicon.ico")
def favicon():
    # Return the favicon.ico file from the static directory
    return send_from_directory(os.path.join(app.root_path, "static/img"), "icon.png")


# Make sure to teardown mqtt client when flask shutdown.
@app.teardown_appcontext
def teardown_mqtt_client(exception):
    mqtt_client.stop()


# Launching the app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
    )
