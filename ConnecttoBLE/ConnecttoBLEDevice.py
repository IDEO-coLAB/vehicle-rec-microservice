import serial
import ScanDevices
import os
import time

def Connect():
	print "In Connect"	
	#os.system('ls -l')
	status ="Failed"
	scan =ScanDevices.ScanBLEDevices()

	if(scan != "Device Not Found"):
		print "MAC Address in Connect : %s",scan
	
	#clear any open rfcomm connections
		os.system('sudo killall rfcomm')
		rfcommstr='sudo rfcomm connect /dev/rfcomm0 '+scan+' 1 &'

		print "RFComm String = %s",rfcommstr

		os.system(rfcommstr)
		#sleep(30) #Wait for connection to establish successfully	

		rfconnection = os.system('sudo ls -l /dev/rf* | grep rfcomm0')

		if (rfconnection != ''):
			print "RFComm Connection established"
		
			status="Success"

	else:
		print "Device Not Found"
		status="Failed"

	#sudo rfcomm connect /dev/rfcomm0 F6:A3:41:05:18:D9 1
	
	return status

def Destroy():
	pass

def loop():
	#print "In Loop Calling Connect from ConnecttoBLEDevice"
	connStatus=Connect()
	print "Status for BLEDevice Connection :",connStatus

if __name__=='__main__':
	try:
		loop()
	except KeyboardInterrupt:
		Destroy()
	#finally:
		#print "In Finally block for Connect to BLE Device"
		#os.system('sudo killall rfcomm')	
	



