# **MQTT**

All of the project is based on an MQTT backhaul, which ensure the communication between devices without using
any static IPs !

The broker use multiples topics, which are :

IOTHome : Root topic
├── data : Data topic. Each device has it's subtopic, with an RX channel (where the server send commands), and the tx channel (where the server receive commands / returns)
│ ├── player
│ │ ├── rx
│ │ └── tx
│ ├── speaker
│ │ ├── rx
│ │ └── tx
│ ├── switch
│ │ ├── rx
│ │ └── tx
│ └── temperature
│ ├── rx
│ └── tx
├── logs : Logs topic, devices are writtings their debugs output here
│ ├── player
│ ├── speaker
│ ├── switch
│ └── temperature
└── presence : Presence topic. Devices ping here regularly to show they're on the network.
├── player
├── speaker
├── switch
└── temperature
