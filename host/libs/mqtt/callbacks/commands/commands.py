# ==================================================================================================
# file :        libs/mqtt/callbacks/commands/commands.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Provide callback functions for the command parser
# ==================================================================================================


class command_handler:
    def __init__(self):
        return

    def parse_payload(self, topic, payload, client, userdata):
        print(topic)
        print(payload)
        print(client)
        print(userdata)
        return
