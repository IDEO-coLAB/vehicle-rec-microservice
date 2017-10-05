# File : OpenSerialPort.py
# Sub Program used to establish a serial port for RF Communication
# Author: Sooraj Bopanna

import os
import serial

def Open():
	ser = serial.Serial('/dev/rfcomm0',38400,timeout=1)
	return ser

