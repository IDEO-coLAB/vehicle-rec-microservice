def fileread():
	file=open("OBDScannerConfig.txt","r")
	file.seek(0)
	Sensorname=file.read().rstrip()
	file.close()
	return Sensorname


if __name__=='__main__':
	try:
		SensorName=fileread()
		print "SensorName = %s",SensorName
	except KeyBoardInterrupt:		
		destroy()

