#coding=utf-8
from enum import Enum
Month=Enum('Month',('JAN','FEB','MAR','APRL','MAY','JUNE','JULY','OGU','SEPT','OCT','NOV','DEC'))
print(Month.JAN)
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
from enum import Enum,unique
@unique
class Weekday(Enum):
	SUN=0
	MON=1
	TUE=2
	WEN=3
	TUR=4
	FRI=5
	SAT=6
print(Weekday(1))
print(Weekday.SUN)
class Gender(Enum):
		Male=1
		Female=2
class Student(object):
	def __init__(self,name,gender):
		self.name=name
		self.gender=Gender(gender)
s=Student('bart',1)
print(s.name,s.gender)