// #include "websocket.h"

// #include "websocket_private.h"

// #include <WebSockets2_Generic.h>
// #include <Arduino.h>
// #include <WiFi.h>

// static WiFiClient espClient;
// static WebSocketsClient webSocketClient;

// int websocket::init()
// {
//     webSocketClient.begin(server_IP, server_port, "/");
//     webSocketClient.setReconnectInterval(5000); // Attempt to reconnect every 5 seconds
//     webSocketClient.onEvent(websocket::handler);
// }

// void websocket::handler(WStype_t type, uint8_t *payload, size_t length)
// {
//     switch (type)
//     {
//     case WStype_DISCONNECTED:
//         Serial.println("[WebSocket] Disconnected!");
//         break;
//     case WStype_CONNECTED:
//         Serial.printf("[WebSocket] Connected to url: %s\n", payload);
//         // Send a message to the server upon connection
//         webSocketClient.sendTXT("Hello from ESP32!");
//         break;
//     case WStype_TEXT:
//         Serial.printf("[WebSocket] Message received: %s\n", payload);
//         break;
//     case WStype_BIN:
//         Serial.println("[WebSocket] Binary data received.");
//         Serial.println((char *)payload);
//         break;
//     case WStype_PING:
//         Serial.println("[WebSocket] Ping received.");
//         break;
//     case WStype_PONG:
//         Serial.println("[WebSocket] Pong received.");
//         break;
//     default:
//         Serial.printf("[WebSocket] Unhandled event type: %d\n", type);
//         break;
//     }
// }

// void websocket::update()
// {
//     webSocketClient.loop();
// }