from datetime import datetime   
import winsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    print(current_hour+":"+current_minute+":"+current_seconds, end="\r", flush=True)
    if(alarm_period<=current_period):
        if(alarm_hour<=current_hour):
            if(alarm_minute<=current_minute):
                if(alarm_seconds<=current_seconds):
                    print("Wake Up!")
                    winsound.Beep(2700, 4700)
                    break