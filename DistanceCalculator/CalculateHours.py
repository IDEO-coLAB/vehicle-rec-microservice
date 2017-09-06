import re
def CalcHours(TimeStr):
	str =TimeStr

	strlen=len(str)
	
	#SecSubstring =str[5:14]

	#MinSubstring =str[2:4]
	
	#HourSubstring=str[0]


	SecSubstring=str[(strlen-9):strlen]

	MinSubstring=str[(strlen-12):(strlen-10)]	
	
	HourSubstring=str[0:(strlen-13)]
	#print "In CalcHours =",str	
	#print "Len = ",len(str)
	#print "Sec =",SecSubstring
	#print "Modsec =",SecSubstring
	#print "Min =",MinSubstring
	#print "Modmin =",MinSubstring
	#print "Hour =",HourSubstring
	#print "ModHour =",HourSubstring

	floatsec=float(SecSubstring)/3600
	floatmin=float(MinSubstring)/60
	#print " Sec in hours =%f",floatsec
	#print "Sec in hours =%f",float(SecSubstring)/3600
	#print "Min in Hours =%f",floatmin
	
	#print "Min+Sec =",floatmin+floatsec

	TotTimeinHours=int(HourSubstring)+(float(MinSubstring)/60)+(float(SecSubstring)/3600)
	
	#print "TotTimeinHours =",TotTimeinHours

	return TotTimeinHours

def Destroy():
        pass

def loop():
        TempTimeStr="0:23:01.016232"
	TotTime=CalcHours(TempTimeStr)
	print "in loop tottime = ",TotTime
	TempTimeStr="10:23:04.234567"
	TotTime=CalcHours(TempTimeStr)
	print "in loop tottime2 =",TotTime

if __name__=='__main__':
        try:
                loop()
        except KeyboardInterrupt():
                Destroy()

