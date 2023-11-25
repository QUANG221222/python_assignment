from datetime import datetime,date
today=date.today()
if today.weekday()==0:
    today="Monday"
elif today.weekday()==1:
    today="Tuesday"
elif today.weekday()==2:
    today="Wednesday"
elif today.weekday()==3:
    today="Thursday"
elif today.weekday()==4:
    today="Friday"
elif today.weekday()==5:
    today="Saturday"
else :today="Sunday"
now=datetime.now()
print("Current date and time")
print(today,",",now.strftime("%Y\\%m\\%d, %H:%M:%S"))