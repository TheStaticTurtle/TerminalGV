#import logging
#logging.basicConfig(level=logging.DEBUG)

import socketio, sys
import ui, time

sio = socketio.Client()
ui = ui.UI()

ui.print()

class PepitaNamespace(socketio.ClientNamespace):
	def on_connect(self):
		pass

	def on_disconnect(self):
		pass

	def on_gps(self, data):
		ui.gps = data
		ui.print()

	def on_connected_devices(self, data):
		ui.network["connected_devices"] = data
		ui.print()

	def on_internet_link_quality(self, data):
		ui.network["internet_link_quality"] = data
		ui.print()

	def on_trainDetails(self, data):
		ui.stops = data["stops"]
		ui.terminusDate = data["stops"][-1]["realDate"]
		ui.print()

sio.register_namespace(PepitaNamespace('/router/api/pepita'))

@sio.on('connect')
def connect():
	print("I'm connected!")

while True:
	sio.connect('https://wifi.sncf/')
	sio.wait()

