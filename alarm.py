import time
from datetime import datetime

def set_alarm(alarm_time):
    """Set an alarm."""
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing! Wake up!")
            break
        time.sleep(30)  # Check every 30 seconds

def alarm_clock():
    alarm_time = input("Set the alarm time (HH:MM format): ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    alarm_clock()
