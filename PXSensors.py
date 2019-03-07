import evdev
from evdev import categorize, InputDevice, AbsEvent, InputEvent
from select import select

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

class PXSensor():
	def __init__(self,device):
		self.device=device
		self.values = {'x':[],'y':[],'z':[]}
		return

	def read(self):
		
		try:
			events = [event for event in self.device.read()]
			abs_events = [event for event in events if isinstance(categorize(event),AbsEvent)]

			self.values['x'] = [(event.timestamp(),event.value) \
									for event in abs_events if event.code==0]
			self.values['y'] = [(event.timestamp(),event.value) \
									for event in abs_events if event.code==1]
			self.values['z'] = [(event.timestamp(),event.value) \
									for event in abs_events if event.code==2]
			return True
		except:
			return False


