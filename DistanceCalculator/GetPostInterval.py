import json
from iofog_container_sdk.client import IoFogClient
from iofog_container_sdk.exception import IoFogException

def GetInterval():
                try:
			interval=0
			client=IoFogClient()
			config=client.get_config()
                        #print "executed get config"
                        #print " Config = ",config
                        JSONconfig =json.dumps(config)
                        #print "JSONconfig = ",JSONconfig
			client=""
		
			for key,val in json.loads(JSONconfig).iteritems():
                                #print " key = ",key
                                #print " val = ",val

                                if key=="IntervalinMinutes":
                                        interval=int(val)
				else:
                                         print "Invalid Message Header encountered"
		
			return interval
		except IoFogException, ex:
                        print "Exception occured ", ex
