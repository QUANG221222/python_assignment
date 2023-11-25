from datetime import datetime, timedelta

start_time=datetime.strptime("06:52:00", "%H:%M:%S")
easy_pace=timedelta(minutes=8, seconds=15)
tempo_pace=timedelta(minutes=7, seconds=12)

total_time=2*easy_pace+3*tempo_pace

time_get_home=start_time+total_time
print("Time you get home for breakfast:  ",time_get_home.time())