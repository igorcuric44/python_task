import re

def add_time(*args):
	dayx=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

	#print(args)
	
	z=re.match("(\d{1,2}):(\d+)\s{1}(AM|PM)",args[0])
	v=re.match("(\d+):(\d+)",args[1])

	day=0
	hour1=0;hour2=0
	minute1=0;minute2=0
	mm=0;mt=0
	dd=0;dt=0
	xx=""
	strx=""
	tt=0;zz=0
	
	if v:
		l=v.groups()
		hour2=int(l[0])
		minute2=int(l[1])
	
	#print(hour2)
	#print(minute2)
	
	if z:
		t=z.groups()
	
		if t[2]=="PM":
			hour1=int(t[0])+12
		elif t[2]=="AM":
			hour1=int(t[0])
		minute1=int(t[1])
	
	hour=hour1+hour2
	minute=minute1+minute2
	
	#print(hour)
	#print(minute)
	
	if(minute>=60):
		mm=int(minute/60)
		minute=minute%60
	
	hour=hour+mm
	
	if(hour>=24):
		day=int(hour/24)
		hour=hour%24
	
	
	if(hour>12):
		hour=hour-12
		xx="PM"
	else:
		if(hour==0):
			hour=12
		else:
			hour=hour
		xx="AM"
	
	#print("day",day)
	
	
	if len(args)==3:
		pp=args[2].title()
		tt=dayx.index(pp)
		#print(tt)
		tt=tt+day
		zz=tt%7
	
	
	hourx=str(hour)
	
	if minute<10:
		minutex="0"+str(minute)
	else:
		minutex=str(minute)	
	
	#print(zz,dayx[zz])
	
	if len(args)==3:
		strx=hourx+":"+minutex+" "+xx+", "+dayx[zz]
	else:
		strx=hourx+":"+minutex+" "+xx
	
	if day==1:
		strx=strx+" (next day)"
	elif day>1:
		strx=strx+" ("+str(day)+" days later)"
	else:
		strx=strx
	
	return strx


