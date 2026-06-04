from datetime import datetime
from playsound import playsound
import time
Time=input("Give the Time when you want to set your alarm(HH:MM): ")
while True:
    current_time = datetime.now().strftime("%H:%M")
    
    if current_time==Time:
        print("Wake Up!! Its time...")
        playsound(r"D:\Pinnacle-Projects\Alarm-Clock\alarm.mp3")        
        break

    time.sleep(1)
