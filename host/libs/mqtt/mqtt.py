# ==================================================================================================
# file :        libs/mqtt/mqtt.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Provide an MQTT abstraction layer class to make easier to handle this protocol.
# ==================================================================================================
## Imports
# Standard
import fnmatch

# Modules
import paho.mqtt.client as paho  # type: ignore


# --------------------------------------------------------------------------------------------------
# Class
# --------------------------------------------------------------------------------------------------
class MQTTClient:
    """
    Handler class to make interractions with the broker a bit easier !
    """

    def __init__(
        self,
        broker="test.mosquitto.org",
        port=1883,
        username="",
        password="",
        topics=None,
    ):
        # Store parameters (except password and username)
        self.broker = broker
        self.port = port
        self.client = paho.Client()

        # Set user and passwords
        self.client.username_pw_set(username, password)

        # Define callback functions
        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message
        self.client.on_disconnect = self.__on_disconnect

        # Set a list of topics to subscribe to
        self.topics = topics if topics is not None else []

        # A dictionary to store topic-specific callback functions
        self.callbacks = {}
        self.gcallbacks = {}

        return

    # ----------------------------------------------------------------------------------------------
    # Functions
    # ----------------------------------------------------------------------------------------------

    def start(self) -> None:
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"Could not connect to MQTT Broker: {e}")

    def stop(self) -> None:
        self.client.loop_stop()
        self.client.disconnect()
        return

    def publish(self, topic, payload) -> None:
        self.client.publish(topic, payload)
        return

    def publish_retain(self, topic, payload) -> None:
        self.client.publish(topic, payload, 2, True)
        return

    def add_subscription(self, topic, callback=None) -> None:
        self.client.subscribe(topic)
        self.topics.append(topic)
        if callback:
            if "#" in topic:
                self.gcallbacks[topic.replace("#", "*")] = callback
            else:
                self.callbacks[topic] = callback

        return

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)
        if topic in self.topics:
            self.topics.remove(topic)
        if topic in self.callbacks:
            del self.callbacks[topic]

        return

    # ----------------------------------------------------------------------------------------------
    # Private functions
    # ----------------------------------------------------------------------------------------------

    def __on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            for topic in self.topics:
                client.subscribe(topic)
        else:
            print(f"Failed to connect, return code {rc}")

    def __on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()

        # Check if a specific callback is registered for this topic
        if topic in self.callbacks:
            self.callbacks[topic](topic, payload, client, userdata)

        # Then, check for more generic callbacks, using the fnmatch module
        for gcall in self.gcallbacks:
            if fnmatch.fnmatch(topic, gcall):
                self.gcallbacks[gcall](topic, payload, client, userdata)

        return

    def __on_disconnect(self, client, userdata, rc) -> None:
        if rc != 0:
            print(f"Unexpected disconnection from MQTT Broker, return code {rc}")
        return
