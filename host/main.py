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

# Modules
from flask import Flask, render_template  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Files
from devices import switch_bp, player_bp, speaker_bp, temperature_bp
from api import api_status_bp
from libs.mqtt import MQTTClient

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
# Flask web server init
# -------------------------------------------------------------------------------------------------

# Openning app
app = Flask(__name__)

# Including blueprints
app.register_blueprint(switch_bp, url_prefix="/devices")
app.register_blueprint(player_bp, url_prefix="/devices")
app.register_blueprint(temperature_bp, url_prefix="/devices")
app.register_blueprint(speaker_bp, url_prefix="/devices")
app.register_blueprint(api_status_bp, url_prefix="/api")

# -------------------------------------------------------------------------------------------------
# MQTT init
# -------------------------------------------------------------------------------------------------
app.config["mqtt_client"] = MQTTClient(
    broker=MQTT_BROKER,
    port=1883,
    username=MQTT_USER,
    password=MQTT_PASS,
)
app.config["mqtt_client"].start()


# First functions
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


# Make sure to teardown mqtt client when flask shutdown.
@app.teardown_appcontext
def teardown_mqtt_client(exception):
    app.config["mqtt_client"].stop()


# Launching the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
