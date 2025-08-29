#include "http.h"

// Other headers
#include "wifi.h"

// Arduino libs
#include <HTTPClient.h>
#include <WiFi.h>

static WiFiClient client;

static String url = "http://172.16.17.37:5000/api/presence/switch";

int http::AssertPresence()
{
    HTTPClient _http;
    if (wifi::CheckStatus(false) != 0)
    {
        return -1;
    }
    // Begin the HTTP request
    _http.begin(client, url);

    // Send the GET request
    int httpCode = _http.GET();

    // httpCode will be negative on error
    if (httpCode > 0)
    {
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);

        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY)
        {
            String payload = _http.getString();
            Serial.println(payload);
        }
    }
    else
    {
        Serial.printf("[HTTP] GET... failed, error: %s\n", _http.errorToString(httpCode).c_str());
    }

    _http.end();

    return 0;
}