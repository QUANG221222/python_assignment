start_time=6*3600+52*60
easy_pace=8*60+15
tempo_pace=7*60+12
total_time=2*easy_pace+3*tempo_pace
time_get_home=total_time+start_time
print(time_get_home)
hours=time_get_home/3600
min=(hours-int(hours))*60
second=time_get_home
print("Tổng thời gian về đến nhà: ",int(hours),":",int(min),":",int(second))