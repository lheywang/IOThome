#include "src/wifi.h"
#include "src/mqtt.h"
#include "src/gpio.h"

/*
 * IMPORTANT NOTICE
 * - Before compiling the tool, copy the two files that end with _ex.h to their name without the _ex, and fill the fields.
 *   On a UNIX system, that may look like :
 *   - cp src/mqtt_private_ex.h src/mqtt_private.h
 *   - cp src/wifi_private_ex.h src/wifi_private.h
 *
 * - And then, fill the different fields (SSID and password for wifi, broker, user and password for MQTT).
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

  // Connect to the mqtt broker
  mqtt::Connect();
}

void loop()
{
  Serial.print(wifi::CheckStatus());
  Serial.print(" - Hello World !\n");
  sleep(1);
}
