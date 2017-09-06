# File : GetVehicleId.py
# Main Program to Fetch the Vehicle Id using the function call ReadVin and Posts the VIN as a IoMessage
# Author: Sooraj Bopanna

import ReadVIN
import PostVIN
import time

def GetVehicleId():
		VIN = ReadVIN.VIN()
		print "VIN = ",VIN
		response=PostVIN.Post(VIN)
def destroy():
        pass

if __name__=='__main__':
        try:
		while True:
	                GetVehicleId()
        except KeyboardInterrupt():
                destroy()

