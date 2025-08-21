// Header
#include "udp.h"

// Others file
#include "gpio.h"

// Libs
#include <WiFi.h>
#include "AsyncUDP.h"
#include <Arduino.h>

AsyncUDP udp;

void udplib::packet_handler(AsyncUDPPacket packet)
{
    uint8_t *buf = (uint8_t *)packet.data();
    buf[packet.length()] = '\0';

    if (packet.length() != 9)
    {
        Serial.printf("Invalid buffer length ! Read : %s byte", packet.length());
        return;
    }

    int payload = strtol((char *)buf, NULL, 16);
    uint8_t cmd = (payload & 0xFF000000) >> 24;
    uint8_t state = (payload & 0x00FF0000) >> 16;
    uint8_t id = (payload & 0x0000FF00) >> 8;
    uint8_t cst = (payload & 0x000000FF);

    Serial.println(cmd);
    Serial.println(state);
    Serial.println(id);
    Serial.println(cst);

    if (cst != 0xAA)
    {
        Serial.printf("Invalid buffer, did not get the last byte as 0xAA\n");
        return;
    }

    switch (cmd)
    {
    case 1: // Set outputs
        digitalWrite(SPEAKERS[id - 1], state);
        Serial.printf("Wrote output pin %d with %s", SPEAKERS[id], state);
        break;

    case 2: // Set inputs
        digitalWrite(INPUTS[id - 1], state);
        Serial.printf("Wrote output pin %d with %s", INPUTS[id], state);
        break;

    case 254: // Reset defaults
        digitalWrite(32, state);
        break;

    case 255: // Reboot device
        break;

    default:
        Serial.print("Unrecognized command");
    }

    return;
}
