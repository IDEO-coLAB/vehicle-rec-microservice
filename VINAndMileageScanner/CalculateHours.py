# File : CalculateHours.py
# Subprogram to convert the time difference measured within the speed change to hours. The converted time is used in calculating the distance traveled
# Author: Sooraj Bopanna

import re
def CalcHours(TimeStr):
	str =TimeStr

	strlen=len(str)


	SecSubstring=str[(strlen-9):strlen]

	MinSubstring=str[(strlen-12):(strlen-10)]	
	
	HourSubstring=str[0:(strlen-13)]
	
	TotTimeinHours=int(HourSubstring)+(float(MinSubstring)/60)+(float(SecSubstring)/3600)
	

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

