from PXSensors import PXSensor
import evdev
import os

os.system('./scripts/enableSensors.sh')

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	if device.name == 'fxas2100x':
		gyro = PXSensor(device)
	elif device.name == 'fxos8700':
		accel = PXSensor(device)

import time

while True:
	while accel.read() is False:
		continue

	print(accel.values['x'])