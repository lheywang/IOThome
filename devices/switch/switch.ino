// Custom made C++ code
#include "src/wifi.h"
#include "src/gpio.h"
#include "src/http.h"

// Arduino libs
#include <HTTPClient.h>
#include <WiFi.h>

/*
 * IMPORTANT NOTICE
 * - Before compiling the tool, copy the files that end with _ex.h to their name without the _ex, and fill the fields.
 *   On a UNIX system, that may look like :
 *   - cp src/wifi_private_ex.h src/wifi_private.h
 *
 * - And then, fill the different fields (SSID and password for wifi).
 * - Failing to do so will result in a compilation error. Theses files are excluded from git (for obvious reasons), and thus DO NOT EXIST after clone.
 *   They remain included by other file, thus, the compiler will simply trigger an error.
 *
 * */

void setup()
{
    // Initialize the serial communication
    Serial.begin(115200);

    // Initialize the GPIOs
    gpio::Init();

    // Connect to the wifi network
    wifi::Connect();
}

void loop()
{
    http::AssertPresence();
    delay(1000 * 10);
}
