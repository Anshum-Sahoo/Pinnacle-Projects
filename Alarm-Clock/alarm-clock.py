from datetime import datetime
from playsound import playsound
import time

while True:
    alarm_time = input("Enter alarm time (HH:MM): ")

    try:
        datetime.strptime(alarm_time, "%H:%M")
        break
    except ValueError:
        print("Invalid format! Use HH:MM (e.g., 07:30)")


print("\nChoose Alarm Tone")
print("1. Tone 1")
print("2. Tone 2")

tone = input("Enter choice: ")

if tone == "2":
    sound = r"D:\Pinnacle-Projects\Alarm-Clock\alarm2.mp3"
else:
    sound = r"D:\Pinnacle-Projects\Alarm-Clock\alarm.mp3"

print(f"\nAlarm set for {alarm_time}")


while True:
    current_time = datetime.now().strftime("%H:%M")

    print(f"Current Time: {current_time}", end="\r")

    if current_time == alarm_time:
        print("\n\nWake Up!! It's Time...")

        playsound(sound)

        
        choice = input("Do you want to snooze for 5 minutes? (y/n): ")

        if choice.lower() == "y":
            print("Alarm snoozed for 5 minutes...")
            time.sleep(300)  # 5 minutes

            print("Wake Up!! Snooze Finished...")
            playsound(sound)

        print("Alarm Completed!")
        break

    time.sleep(1)
