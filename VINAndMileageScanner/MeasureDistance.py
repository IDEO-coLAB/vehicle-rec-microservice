# File : MeasureDistance.py
# SubProgram to calculate the Total distance traveled. The main function in this subprogram is ReadDistance which is called from the main driver program
# Function Read Distance gets the duration to measure the distance for, the serial port handle and the Id of the vehicle. This function reads the speed of the vehicle
# based on the output of the ELM Command "01 0D" and reads the same as a byte stream. This byte stream is then stripped off any space characters and the 
# speed string for evaluation is constructed. If the speed measured is different from the original speed, then, the time difference is recorded and the distance for 
# that time interval is calculated until the time does not equal to the calculation duration specified. If this total time interval equals the 
# calculation duration specified, a function to post the message to the Fog is invoked by passing the VIN, Distance and the start and end times for the 
# distance measured. This sub program continues in a loop and posts the message at each time duration specified.
#
# Author: Sooraj Bopanna

import serial
import binascii
import re
import time
import datetime
import CalculateHours
import PostVINAndDistance
from datetime import timedelta


def RetrieveSpeed(SpeedStr):

	print " In RetrieveSpeed = ",SpeedStr

	print " Length of SpeedStr =",len(SpeedStr)


	joinedstr=''.join(SpeedStr)
	print "joinedstr: ",joinedstr

	print " Len of joinedstr =",len(joinedstr)

	speedtuple=joinedstr[12:14]
	print " speedtuple = ",speedtuple

	print " Len of speedtuple =",len(speedtuple)

	return speedtuple

def ReadDistance(duration,ser,VIN):
	Prevspeed=""

	initspeed="00"
	newspeed="00"
        starttime=datetime.datetime.now()
	endtime=""
	disttraveled=0
	timediff=0
	calcbegintime=starttime

	print "Duration passed to ReadDistance Method = ",duration

	while True:
	
		line =[]
		print "Writing to ELM" 
		writecallmesg=ser.write("01 0D\r") #record speed

	 	Speed=""
		
	
		C=ser.read()
		while (C <> '>'):
		 print "Char Read = ",C
		 line.append(C)
		 C=ser.read()
	

		if(C == '>'):
		 print "Char > encountered "
		 print " line = ",line
		 
		 if(len(line)==17):
		    VehicleSpeed=RetrieveSpeed(line)
		    print "Returned from Retrieve Speed function : ",VehicleSpeed
		    print "Init speed =",initspeed		    
		    if(VehicleSpeed <> initspeed):
		     
		     endtime=datetime.datetime.now()
		     timeelapsed=endtime-starttime
		     timeinHours=CalculateHours.CalcHours(str(timeelapsed))
		     
		     disttraveled+=float(int(initspeed,16))*timeinHours
		     
                     initspeed=VehicleSpeed
                     starttime=endtime
		     timediff+=timeelapsed.total_seconds()/60
		     print "time elapsed in mins in dist calc loop",timediff
                     timeelapsed=0
		     print " duration in dist calc loop",duration		
			
		if(int(timediff) == int(duration)):
		  print " In loop as timediff equals duration"	
		  timediff=0
		  distinmiles=disttraveled/1.6
		  PostVINAndDistance.Post(VIN,distinmiles,calcbegintime.strftime('%Y-%m-%dT%H:%M:%SZ'),endtime.strftime('%Y-%m-%dT%H:%M:%SZ'))
		  calcbegintime=endtime
		  distinmiles=0
		  disttraveled=0			

	
