# File : ReadVIN.py
# Program to read the Vehicle ID - uses the ELM command "09 02" to fetch the VIN number 
# Author: Sooraj Bopanna

import os
import serial
import binascii
import re

def VIN(ser):

	print "In ReadVIN function VIN() "

	RawVINStr=ReadRawString(ser)
	VIN=RetrieveVIN(RawVINStr)
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
			
			line.append(c)
			
			
			if (c =='>'):
				
				brvar=1
				break
			
	return line
