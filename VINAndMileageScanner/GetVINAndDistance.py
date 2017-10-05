# File : GetVINAndDistance
# Main Driver program to get the Vehicle Id and Distance Traveled. Following sub program calls are made for these specific functions
# SubProgram: GetPostInterval - This gets the interval in minutes from the microservice configuration parameters
# SubProgram: OpenSerialPort - This opens a serial port for communication with the BLEDevice
# SubProgram: ReadVIN - This is used to get the Vehicle Id
# SubProgram: MeasureDistance - This is used to calculate the distance traveled over the time period specified and publish the VIN and Distance Message
# to FogController
# Author: Sooraj Bopanna

import OpenSerialPort
import ReadVIN
import MeasureDistance
import GetPostInterval
import time

def GetVINAndDistance():
		interval=GetPostInterval.GetInterval()
		serport = OpenSerialPort.Open()
		VIN =ReadVIN.VIN(serport)
		print "VIN Retrieved in Get VIN and Distance Function = ",VIN
		Distance = MeasureDistance.ReadDistance(interval,serport,VIN)
def destroy():
        pass

if __name__=='__main__':
        try:
		while True:
	                GetVINAndDistance()
        except KeyboardInterrupt():
                destroy()

