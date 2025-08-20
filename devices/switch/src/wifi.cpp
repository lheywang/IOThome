// Header
#include "wifi.h"

// Arduino library
#include <WiFi.h>
#include <Arduino.h>

// Private libs
#include "wifi_private.h"
#include "mqtt.h"

// Functions
int wifi::Connect()
{
    WiFi.mode(WIFI_STA);
    WiFi.begin(wifi_ssid, wifi_password);
    Serial.println("\nConnecting");

    int count = 0;
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(100);
        count++;
        if (count > 200)
        {
            return -1; // Error while connecting to wifi
        }
    }

    Serial.println("\nConnected to the WiFi network");
    Serial.print("Local ESP32 IP: ");
    Serial.println(WiFi.localIP());

    return 0;
}

int wifi::Disconnect()
{
    WiFi.disconnect();

    int count = 0;
    while (wifi::CheckStatus() == 0)
    {
        delay(100);
        count++;
        if (count > 200)
        {
            return -1; // Error while connecting to wifi
        }
    }

    return 0;
}

int wifi::CheckStatus()
{
    switch (WiFi.status())
    {
    case WL_NO_SHIELD:
        Serial.print("No Wi-Fi shield is present. Please ensure Wi-Fi is available on the device, and retry\n");
        return -1;
        break;

    case WL_IDLE_STATUS: // Wait status before WL_CONNECTED of FAILED
        return -2;
        break;

    case WL_CONNECT_FAILED:
        Serial.print("Could not connect to Wi-Fi. Please ensure credentials are correct !\n");
        return -3;
        break;

    case WL_NO_SSID_AVAIL:
        Serial.print("There's no Wi-Fi network available. Ensure the device can receive Wi-Fi signal !");
        return -4;
        break;

    case WL_SCAN_COMPLETED: // Nothing to do here
        return -5;
        break;

    case WL_CONNECTION_LOST:
        Serial.print("Lost wifi connection... Retry to connect !");
        // Proper shtudown
        mqtt::Disconnect();
        wifi::Disconnect();

        wifi::Connect();
        mqtt::Connect();
        return -6;
        break;

    case WL_DISCONNECTED:
        return -7;
        break;

    case WL_CONNECTED:
        // Nothing to do, exit
        return 0;
        break;

    default:
        // Shall never get here... Anyway
        return -1024;
        break;
    }
}