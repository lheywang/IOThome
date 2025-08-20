// Header
#include "mqtt.h"

// Files
#include "mqtt_private.h"

// Arduino library
#include <WiFi.h>
#include <Arduino.h>
#include <PubSubClient.h>

static WiFiClient espClient;
PubSubClient mqttClient(espClient);

void callback(char *topic, byte *payload, unsigned int length)
{
    Serial.printf("Topic : %s - %s", topic, (char *)payload);
    return;
}

int mqtt::Connect()
{
    String clientId = "ESP32Client-" + String(random(0xffff), HEX);

    mqttClient.setServer(mqtt_broker, mqtt_port);
    mqttClient.setCallback(callback);

    Serial.print("Attempting MQTT connection...");

    // Attempt to connect with credentials and a unique client ID
    if (mqttClient.connect(clientId.c_str(), mqtt_user, mqtt_password))
    {
        Serial.println("connected!");
        // Subscribe to a topic after a successful connection
        mqttClient.subscribe("test/switch");
        return 0; // Success
    }
    else
    {
        // Connection failed, print the error code for debugging
        int errorCode = mqttClient.state();
        Serial.print("failed, rc=");
        Serial.print(errorCode);
        Serial.println(" retrying in 5 seconds");

        // Return the error code
        return errorCode;
    }
}

int mqtt::Disconnect()
{
}
