# File : ReadVIN.py
# Program to read the Vehicle ID - uses the ELM command "09 02" to fetch the VIN number 
# Author: Sooraj Bopanna

import os
import serial
import binascii
import re

def VIN():

	print "In ReadVIN function VIN() "
	ser =serial.Serial('/dev/rfcomm0',38400,timeout=1)
	#ser = serial.Serial('/commportdir/rfcomm0',38400,timeout=1)
	#commport='/dev/rfcomm0'
	#ser =serial.Serial('rfcomm',38400,timeout=1)
	RawVINStr=ReadRawString(ser)
	VIN=RetrieveVIN(RawVINStr)
	ser.close()
	os.system('sudo killall rfcomm')
	return VIN

def RetrieveVIN(VINStr):
	rawstr=VINStr

	joinedrawstr=''.join(rawstr)

	thirdtuple=joinedrawstr[61:81]
	
	secondtuple=joinedrawstr[36:57]
	
	firsttuple=joinedrawstr[23:32]
	
	combinedstr=firsttuple+secondtuple+thirdtuple

	combinedstrwithoutspace=re.sub(' ','',combinedstr)

	VIN=binascii.unhexlify(combinedstrwithoutspace)
	print "In Retrieve VIN = ",VIN
	return VIN

def ReadRawString(ser):
	
	writecallmesg=ser.write("09 02\r")
	line=[]
	brvar =0
	joined_line=''

	while(brvar==0):
		for c in ser.read():
			#print "Read from rfcomm :",c
			line.append(c)
			#print "Line =",line
			
			if (c =='>'):
				#print " Found > Line = ",line
				brvar=1
				break
			
	return line
