#import ConnecttoBLEDevice
import MeasureDistance
import GetPostInterval
import time

def GetDistance():
		#connection = ConnecttoBLEDevice.Connect()
		#time.sleep(10)
		#print "In Get Veh Id : Connection = ",connection
		#if connection != "Failed":
		interval=GetPostInterval.GetInterval()
		Distance = MeasureDistance.ReadDistance(interval)
		#print "Interval = ",interval
		#response=PostDistance.Post(Distance)
def destroy():
        pass

if __name__=='__main__':
        try:
		while True:
	                GetDistance()
        except KeyboardInterrupt():
                destroy()

