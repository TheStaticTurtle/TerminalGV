import dateutil.parser
import sys
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Europe/Paris')

ts = 34

class UI:
	def __init__(self):
		self.gps = {"success":True,"fix":0,"timestamp":0, "latitude":0,"longitude":0,"altitude":0,"speed":0,"heading":0}
		self.network = {"internet_link_quality": {"quality":0}, "connected_devices": {"devices":0}}
		self.terminusDate = '2000-01-01T00:00:00.000000Z'
		self.stops = []

	def _clear_terminal(self):
		print("\033[2J")
		print("\033[0;0f")

	def _print_train(self):
		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;252;65;3m")
		sys.stdout.write("                                   __   __\n")
		sys.stdout.write("                                                 /'   `\\\n")
		sys.stdout.write("                                                Y.     .Y\n")
		sys.stdout.write("                                      _______    \\`. .'/\n")
		sys.stdout.write("                       ,-------------'=======\"--\"\"\"\"-\"\"\"\"---.\n")
		sys.stdout.write("                 __,=+'-------------------------------------|p\n")
		sys.stdout.write("              .-/__|_]_]  :\"/:\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"|'\n")
		sys.stdout.write("           ,-'__________[];/_;_____________________T G V____|\n")
		sys.stdout.write("         ,\".../_|___________________________________________|\n")
		sys.stdout.write("        (_>        ,-------.                     ,-------.  |\n")
		sys.stdout.write("         `-._____.'(_)`='(_)\\_7___7___7___7__7_.'(_)`='(_)\\_/ hjw\n")
		sys.stdout.write("\033[000m")
		sys.stdout.flush()

	def _hummanize_date(self, isostring):
		date = dateutil.parser.isoparse(isostring)
		date = date.astimezone(to_zone)
		return date.strftime("%Y/%m/%d %H:%M")

	def print(self):
		self._clear_terminal()
		self._print_train()


		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;245;179;66m")
		sys.stdout.write("\n" + '='*ts +" Line " + '='*(ts-1)+"\n")
		sys.stdout.write("\033[000m")

		sys.stdout.write("Stops:\n")
		if len(self.stops) == 0:
			print("   Loading....")
		for stop in self.stops:
			print(f" - {stop['label']:40s} Arrival time: {self._hummanize_date(stop['realDate'])}")

		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;194;245;66m")
		sys.stdout.write("\n" + '='*ts +" GPS " + '='*ts+"\n")
		sys.stdout.write("\033[000m")
		print(f"Latitude:  {self.gps['latitude']:.6f} °")
		print(f"Longitude: {self.gps['longitude']:.6f} °")
		print(f"Altitude:  {self.gps['altitude']:.2f} m")
		print(f"Speed:     {self.gps['speed']*3.6:.2f} km/h")
		print(f"Heading:   {self.gps['heading']:.2f} °")


		sys.stdout.write("\033[001m")
		sys.stdout.write("\x1b[38;2;66;245;99m")
		sys.stdout.write("\n" + '='*(ts-2) +" Network " + '='*(ts-2)+"\n")
		sys.stdout.write("\033[000m")
		print(f"Connected users: {'👤'*(self.network['connected_devices']['devices']//4)} ({self.network['connected_devices']['devices']})")
		print(f"Link quality:    {'⭐'*self.network['internet_link_quality']['quality']}")
