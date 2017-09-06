import serial
import binascii
import re
import time
import datetime
import CalculateHours
import PostDistance
from datetime import timedelta

# Formula to be used to calculate the distance traveled : (Avg of Non-Zero Speed)*(Time in Mins)/60

def RetrieveSpeed(SpeedStr):
	#d=['0','9',' ','0','2','\r','0','1','4',' ','\r','0',':',' ','4','9',' ','0','2',' ','0','1',' ','3','2',' ','5','4',' ','3','3',' ','\r','1',':',' ','4','4',' ','4','6',' ','3','4',' ','4','4',' ','5','6',' ','3','5',' ','4','3',' ','\r','2',':',' ','5','7',' ','3','2',' ','3','3',' ','3','5',' ','3','8',' ','3','3',' ','3','2',' ','\r','\r','>']
	#print "Length of D: ",len(d)

	#print " d =",d

	print " In RetrieveSpeed = ",SpeedStr

	print " Length of SpeedStr =",len(SpeedStr)


	#e=''.join(d)

	joinedstr=''.join(SpeedStr)
	print "joinedstr: ",joinedstr

	print " Len of joinedstr =",len(joinedstr)

	speedtuple=joinedstr[12:14]
	print " speedtuple = ",speedtuple

	print " Len of speedtuple =",len(speedtuple)

	return speedtuple

def ReadDistance(duration):
	Prevspeed=""
	ser = serial.Serial('/dev/rfcomm0',38400,timeout=1)

	#outfile=open("VehicleSpeedandTime.odt","w")
	#writecallmesg=ser.write("01 31\r") # distance traveled since code cleared
	
	#writecallmesg=ser.write("01 0D\r") #record speed
        #print "WriteMesg = ",writecallmesg

	initspeed="00"
	newspeed="00"
        starttime=datetime.datetime.now()
	endtime=""
	disttraveled=0
	timediff=0
	calcbegintime=starttime

	print "Duration passed to ReadDistance Method = ",duration

	while True:
	#while (int(timediff) <> int(duration)):	
		line =[]
		print "Writing to ELM" 
		writecallmesg=ser.write("01 0D\r") #record speed
		#print "WriteMesg = ",writecallmesg
		
		#outfile.write("Starttime=")

	 	Speed=""
		#Speed=ser.readline()
		#starttime=datetime.datetime.now().replace(microsecond=0)
		#outfile.write(datetime.datetime.now().replace(microsecond=0))
		#print "Starttime =",starttime
	
		C=ser.read()
		while (C <> '>'):
		 print "Char Read = ",C
		 line.append(C)
		 C=ser.read()
	

		if(C == '>'):
		 print "Char > encountered "
		 print " line = ",line
		 #outfile.write(str(line))
		 if(len(line)==17):
		    VehicleSpeed=RetrieveSpeed(line)
		    print "Returned from Retrieve Speed function : ",VehicleSpeed
		    print "Init speed =",initspeed		    
		    if(VehicleSpeed <> initspeed):
		     #outfile.write("Speed =")
		     #outfile.write(str(VehicleSpeed))
		     endtime=datetime.datetime.now()
		     timeelapsed=endtime-starttime
		     timeinHours=CalculateHours.CalcHours(str(timeelapsed))
		     #outfile.write("\n")
		     #outfile.write("timeelapsed =")
		     #outfile.write(str(timeinHours))
		     #outfile.write("\n")
		     #outfile.write("initspeed =")
		     #outfile.write(initspeed)
		     #outfile.write("\n")
		     #outfile.write("Speed converted to int =\n")
		     #outfile.write(str(int(initspeed,16)))
		     disttraveled+=float(int(initspeed,16))*timeinHours
		     #outfile.write("\n distance traveled = \n")
		     #outfile.write(str(disttraveled))
		     #outfile.write("\n")
                     initspeed=VehicleSpeed
                     starttime=endtime
		     timediff+=timeelapsed.total_seconds()/60
		     print "time elapsed in mins in dist calc loop",timediff
                     timeelapsed=0
		     print " duration in dist calc loop",duration		
			
		if(int(timediff) == int(duration)):
		  print " In loop as timediff equals duration"	
		  timediff=0
		  PostDistance.Post(disttraveled,calcbegintime.strftime('%Y-%m-%dT%H:%M:%SZ'),endtime.strftime('%Y-%m-%dT%H:%M:%SZ'))
		  calcbegintime=endtime
					

		
	#print "Closing serial comm port"
	#ser.close()


	#print "Joinedline after closing serial port = ",joined_line

	#line.replace("\r0:","")
	#line.replace("\r1:","")
	#line.replace("\r2:","")
	#line.replace("\r\r","")

	#print " Length of Array Line :",line.length()
	#print "Line after stripping special characters : ",line

	#print "Total Dist traveled =",disttraveled
	#return disttraveled	
