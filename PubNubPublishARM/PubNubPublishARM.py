import json
import GetUniqueId
import time
import datetime
import base64
#import GetFogMessage
from iofog_container_sdk.client import IoFogClient
from iofog_container_sdk.exception import IoFogException
from iofog_container_sdk.iomessage import IoMessage
from iofog_container_sdk.listener import *
from pubnub.pnconfiguration import PNConfiguration
from pubnub import pubnub

#subkey,pubkey,seckey,pubuid,pubsec,pubchannel,pubmessage

def GetContainerConfig():
                try:

			global subkey,pubkey,seckey,pubuid,pubsec,pubchannel,message
                        client=IoFogClient()
                        #print "Fog Client Initiated"
                        config=client.get_config()
                        #print "executed get config"
                        #print " Config = ",config
                        JSONconfig =json.dumps(config)
                        #print "JSONconfig = ",JSONconfig
			
			client=""

                        for key,val in json.loads(JSONconfig).iteritems():
                                #print " key = ",key
                                #print " val = ",val
				
				if key=="uuid":
					pubuid=val

				elif key=="subscribekey":
					subkey=val

				elif key=="publishkey":
					pubkey=val
		
				elif key=="secretkey":
					seckey=val
			
				elif key=="ssl":
					pubsec=val
			
				#elif key=="message":
					#message=val

				elif key=="channel":
					pubchannel=val

				else:
					 print "Invalid Message Header encountered"
					

                        #return val
			
			print "Values read uuid= %s subkey= %s pubkey = %s secretkey =%s ssl = %s channel =%s"%(pubuid,subkey,pubkey,seckey,pubsec,pubchannel)

                except IoFogException, ex:
                        print "Exception occured ", ex

def PublishMessage(MsgToPublish):
	print "In Publish Message"
	#doublequote="\""
	#try:
	print "Values read uuid= %s subkey= %s pubkey = %s secretkey =%s ssl = %s channel =%s"%(pubuid,subkey,pubkey,seckey,pubsec,pubchannel)
	pn_config=pubnub.PNConfiguration()
		#pn_config.subscribe_key="sub-c-3f58fb7c-6fec-11e7-958a-0619f8945a4f"
	pn_config.subscribe_key=subkey
		#pn_config.publish_key="pub-c-a6f42e4c-611e-488e-8e47-8f93f6ba9409"
	pn_config.publish_key=pubkey
		#pn_config.secret_key="sec-c-ZGY1ZWEzZjktYzQxYi00NTgxLTk0NDEtYWYwNjhmOTliYzM5"
	pn_config.secret_key=seckey
	pn_config.uuid=GetUniqueId.GenerateId()
	#pn_config.uuid=doublequote+pubuid+doublequote
		#pn_config.ssl=True
	pn_config.ssl=pubsec
	
	pubnubobj=pubnub.PubNub(pn_config)

	curr_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	#JSONObject jsonmsgobject = new JSONObject(MsgToPublish)

	#jsonmsgobject = json.dumps(MsgToPublish,default=jsonDefault)

	print "Message to be published to Pubnub = ",MsgToPublish

	#pubmessage={"Id":message,"Timestamp":curr_time}

	#pubnubobj.publish(	
	#'SoorajTestChannel',
	#'Hello World-Sooraj'
	#)

		#pubnubobj.publish().channel('SoorajTestChannel2').message('Hello World-Sooraj1').sync()
	pubnubobj.publish().channel(pubchannel).message(MsgToPublish).sync()
	print "Message Published to Pubnub"
	#except PubnubException as e:
		#print(e)

def GetMessage():
		msgToPublish=""
		msgClient=IoFogClient()
		messages=IoMessage()
		messages=msgClient.get_next_messages()
		#JSONMesg=json.dumps(messages)
		#msg=msgClient.to_json()
		#msgClient.establish_message_ws_connection(MessageListener())
		print "msgClient initiated"
		#print "msgClient = ",json.dumps(msg)
		print "messages object= ",messages
		#print "messages element= ",messages.iomessage.IOMessage
		msglen=len(messages)
		print "message length = ",msglen
		#rawmesg=messages.iomessage.IOMessage
		if msglen>0:
			msgElement=messages[0]
			print "message elemnent = ",msgElement
			print "Tag = ",msgElement.tag
			msgToPublish=json.loads(base64.b64decode(msgElement.contentdata))
		#msgToPublish=msgElement.contentdata
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
		#print "Calling Publish Message"
			print "Calling GetMessage"
			pubMsg=GetMessage()
			if(pubMsg <> ""):
	               		PublishMessage(pubMsg)
	       #RetrieveMessage()
        except KeyboardInterrupt():
                destroy()

	
