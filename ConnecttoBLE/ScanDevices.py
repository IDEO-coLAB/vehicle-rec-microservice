
# File : ScanDevices.py  
# Program uses the BLE microservice to scan the BLE devices and returns the Mac Address of the specified BLE Device
# Author: Sooraj Bopanna

#!usr/bin/env python
#!/bin/bash

import os
import json
import urllib2
import socket
import ReadOBDSensorName

def setup():
	global BLEDeviceName,DeviceFound
	BLEDeviceName=ReadOBDSensorName.fileread()
	print "BLEDevice = ",BLEDeviceName
	

def ScanBLEDevices():
	setup()
	macaddr=""
	print "BLE Devince In ScanBLEDevices :%s",BLEDeviceName
	Resp = urllib2.urlopen('http://localhost:10500/devices')
	Resp_obj = json.load(Resp)
	#print " Resp_obj = %s " %Resp_obj

	#print "Length of String =%d" %len(Resp_obj)	

	
	macaddr="Device Not Found"
		
	for i in Resp_obj:
		json_dmps=json.dumps(i)
		

		for key, di in json.loads(json_dmps).iteritems():
			
			if key=="local_name": 
				
				if di==BLEDeviceName:
					print "BLEDevice JSON String = %s",json_dmps
					
					json_MacAddr=json_dmps
					
					for k, v in json.loads(json_MacAddr).iteritems():
						if k=="mac_address":
							macaddr=v
							print "MacAddr Found for BLEDevice ",macaddr

	
	return macaddr

def loop():
		 print "In Main Loop :"
		 MAC=ScanBLEDevices()
		 print " MAC Address in Main Loop is ",MAC 

def destroy():
	pass

if __name__=='__main__':
	try:
		#setup()
		loop()
	except KeyboardInterrupt():
		destroy()

