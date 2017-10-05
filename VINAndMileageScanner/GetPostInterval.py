# File : GetPostInterval
# SubProgram to Get the Interval in minutes to measure the distance traveled and Post the Message to the Fog Controller
# The parameters in the microservice element is defined as a JSON name value pair. This program monitors a specific JSON Name String "IntervalinMinutes"
# Author: Sooraj Bopanna

import json
from iofog_container_sdk.client import IoFogClient
from iofog_container_sdk.exception import IoFogException

def GetInterval():
                try:
			interval=0
			client=IoFogClient()
			config=client.get_config()
                        JSONconfig =json.dumps(config)
			client=""
		
			for key,val in json.loads(JSONconfig).iteritems():

                                if key=="IntervalinMinutes":
                                        interval=int(val)
				else:
                                         print "Invalid Message Header encountered"
		
			return interval
		except IoFogException, ex:
                        print "Exception occured ", ex
