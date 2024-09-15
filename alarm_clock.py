import time
import os

def alarm_clock(seconds):
    print(f"Alarm set for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up! Wake up!")
    # Play a sound (requires external sound file or os-level beep command)
    os.system("echo -e '\a'")

seconds = int(input("Enter time only in seconds to set the alarm: "))
alarm_clock(seconds)