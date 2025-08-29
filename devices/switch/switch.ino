// Custom made C++ code
#include "src/wifi.h"
#include "src/gpio.h"
#include "src/http.h"
// #include "src/websocket.h"

// Arduino libs
#include <HTTPClient.h>
#include <WiFi.h>

WiFiServer server(1234);

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

/*
 * DEPENDENCIES
 * - HTTPClient
 * - WebSockets2_Generic
 *
 */

void setup()
{
    // Initialize the serial communication
    Serial.begin(115200);

    // Initialize the GPIOs
    gpio::Init();

    // Connect to the wifi network
    wifi::Connect();

    server.begin();
    Serial.println("Server started!");
}

void loop()
{
    WiFiClient client = server.available();

  if (client) {
    // A new client has connected.
    Serial.println("New client connected!");
    
    // Process a single command from the client
    String command = client.readStringUntil('\n');
    command.trim();
    
    Serial.print("Received command: ");
    Serial.println(command);

    if (command == "status") {
      client.println("Status: OK");
    } else if (command == "toggle_switch") {
      client.println("Toggling switch...");
    } else {
      client.println("Unknown command");
    }

    // Immediately stop the client after processing the command.
    client.stop();
    Serial.println("Client disconnected.");
  }

    // Set presence every 10 seconds
    static unsigned long lastSend = 0;
    if (millis() - lastSend > 10000)
    {
        http::AssertPresence();
        lastSend = millis();
    }
}
