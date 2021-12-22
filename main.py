#import logging
#logging.basicConfig(level=logging.DEBUG)

import socketio, sys

sio = socketio.Client()

class PepitaNamespace(socketio.ClientNamespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_gps(self, data):
        print(data)

    def on_connected_devices(self, data):
        print(data)

    def on_internet_link_quality(self, data):
        print(data)

    def on_trainDetails(self, data):
        print(data["stops"][-1]["realDate"])

sio.register_namespace(PepitaNamespace('/router/api/pepita'))

@sio.on('connect')
def connect():
    print("I'm connected!")

sio.connect('https://wifi.sncf/')
sio.wait()
