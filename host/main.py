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

# Modules
from flask import Flask, render_template  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Files
from devices import switch_bp, player_bp, speaker_bp, temperature_bp
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
# MQTT init
# -------------------------------------------------------------------------------------------------
mqtt_client = MQTTClient(
    broker=MQTT_BROKER,
    port=1883,
    username=MQTT_USER,
    password=MQTT_PASS,
)
mqtt_client.start()


def test_callback(topic, payload, client, userdata):
    print(f"{topic} : {payload}")
    return


mqtt_client.add_subscription("presence/#", test_callback)
mqtt_client.publish_retain("presence/server", "Up !")


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


# First functions
@app.route("/")
@app.route("/index.html")
def hello_world():
    return render_template("index.html")


# Launching the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
