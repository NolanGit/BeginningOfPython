import time
def GetTime():
	CurrentHour=int(time.strftime('%H',time.localtime(time.time())))
	CurrentMin=int(time.strftime('%M',time.localtime(time.time())))
	CurrentTime=CurrentHour+CurrentMin/100
	CurrentWeek1=str(time.strftime('%a',time.localtime(time.time())))
	CurrentWeek2=int(time.strftime('%w',time.localtime(time.time())))
	#CurrentWeekInt=
	return CurrentTime,CurrentWeek1,CurrentWeek2
CurrentTime,CurrentWeek1,CurrentWeek2=GetTime()
print(CurrentTime,CurrentWeek1,CurrentWeek2)
