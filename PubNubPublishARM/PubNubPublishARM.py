# File : GetVehicleId.py
# Main Program to Publish Message from IoFog controller to Pubnub channel. The pubnub configuration parameters are made available with the JSON configuration 
# for the Microservice element
# Author: Sooraj Bopanna

import json
import GetUniqueId
import time
import datetime
import base64
from iofog_container_sdk.client import IoFogClient
from iofog_container_sdk.exception import IoFogException
from iofog_container_sdk.iomessage import IoMessage
from iofog_container_sdk.listener import *
from pubnub.pnconfiguration import PNConfiguration
from pubnub import pubnub



def GetContainerConfig():
                try:

			global subkey,pubkey,seckey,pubuid,pubsec,pubchannel,message
                        client=IoFogClient()
                        
                        config=client.get_config()
                        
                        JSONconfig =json.dumps(config)
                        
			
			client=""

                        for key,val in json.loads(JSONconfig).iteritems():

				if key=="subscribekey":
					subkey=val

				elif key=="publishkey":
					pubkey=val
		
				elif key=="secretkey":
					seckey=val
			
				elif key=="ssl":
					pubsec=val
			

				elif key=="channel":
					pubchannel=val

				else:
					 print "Invalid Message Header encountered"
					
			
			print "Values read subkey= %s pubkey = %s secretkey =%s ssl = %s channel =%s"%(subkey,pubkey,seckey,pubsec,pubchannel)

                except IoFogException, ex:
                        print "Exception occured ", ex

def PublishMessage(MsgToPublish):
	print "In Publish Message"
	
	print "Values read subkey= %s pubkey = %s secretkey =%s ssl = %s channel =%s"%(subkey,pubkey,seckey,pubsec,pubchannel)
	pn_config=pubnub.PNConfiguration()
		
	pn_config.subscribe_key=subkey
		
	pn_config.publish_key=pubkey
		
	pn_config.secret_key=seckey
	pn_config.uuid=GetUniqueId.GenerateId()

	pn_config.ssl=pubsec
	
	pubnubobj=pubnub.PubNub(pn_config)


	print "Message to be published to Pubnub = ",MsgToPublish


	pubnubobj.publish().channel(pubchannel).message(MsgToPublish).sync()
	print "Message Published to Pubnub"
	

def GetMessage():
		msgToPublish=""
		msgClient=IoFogClient()
		messages=IoMessage()
		messages=msgClient.get_next_messages()
	
	
		print "messages object= ",messages
		
		msglen=len(messages)
		print "message length = ",msglen
	
		if msglen>0:
			msgElement=messages[0]
			print "message elemnent = ",msgElement
			print "Tag = ",msgElement.tag
			msgToPublish=json.loads(base64.b64decode(msgElement.contentdata))
			print "Contentdata = ",msgToPublish

		else: 
			msgToPublish=""	
	
		return msgToPublish

def jsonDefault(object):
    return object.__dict__

def destroy():
	pass


if __name__=='__main__':
        try:
                while True:
			GetContainerConfig()
		
			print "Calling GetMessage"
			pubMsg=GetMessage()
			if(pubMsg <> ""):
	               		PublishMessage(pubMsg)
	       
        except KeyboardInterrupt():
                destroy()

	
