# ==================================================================================================
# file :        libs/mqtt/callbacks/logs/logs.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Provide callback functions for the presences parser
# ==================================================================================================


class logs_handler:
    def __init__(self):
        self.presences = {}
        return

    def parse_payload(self, topic, payload, client, userdata):
        print(topic)
        print(payload)
        print(client)
        print(userdata)
        return
