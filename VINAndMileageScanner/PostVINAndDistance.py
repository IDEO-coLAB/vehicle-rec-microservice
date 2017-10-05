# File : PostVINAndDistance.py
# This subprogram is used to Post the VIN and Distance traveled properties to the Fog controller as a JSON Message
# The main payload (VIN and Distance) needs to be converted to the base64 format, which is the standard reuirement for the ioFog message
# The base64 converted message is encapsulated in the IoMessage format using the SendMesgToFog function
# Author: Sooraj Bopanna

import os
import json
import base64
import urllib2
from iofog_container_sdk.client import IoFogClient
from iofog_container_sdk.exception import IoFogException
from iofog_container_sdk.iomessage import IoMessage
from iofog_container_sdk.listener import *

def Post(VIN,distance,starttime,endtime):
	DistMesg={"VIN":VIN,"StartTime":starttime,"EndTime":endtime,"TotalDistance":distance}
	print "Distance Message = ",DistMesg
	JSONDistMesg=json.dumps(DistMesg)
	print "JSON Dist Mesg = ",JSONDistMesg
	b64Dist=ConverttoBase64(JSONDistMesg)
	print "Base 64 Dist Mesg = ",b64Dist
	responseMesg=SendMesgToFog(b64Dist)

	print " Message Post Response = ",responseMesg
	print "\n"

	return responseMesg

def SendMesgToFog(base64Dist):
        client=IoFogClient()
        msg=IoMessage()
        msg.infotype="application/json"
        msg.infoformat="text/utf-8"
        msg.contentdata=base64Dist
        msg.contextdata=""
        msg.tag="Distance"
        msg.groupid=""
        msg.authid=""
        msg.authgroup=""
        msg.hash=""
        msg.previoushash=""
        msg.nonce=""

        try:
                receipt = client.post_message(msg)
        except IoFogException, e:
                print "Exception Sending Message to Fog"
                print "\n"
                print(e)

        return receipt


def ConverttoBase64(DistStr):
	b64VIN=base64.b64encode(str(DistStr))
	return b64VIN
