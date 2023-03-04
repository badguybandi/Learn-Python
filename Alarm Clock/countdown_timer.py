from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def timer(seconds:int):

    time_elapsed = 0

    print(f"{CLEAR}")
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        secondes_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Countdown will end in: {minutes_left:02d}:{secondes_left:02d}")

    playsound("beep.mp3")
        

minutes = int(input("Enter minutes to wait: "))
seconds = int(input("Enter seconds to wait: "))
total_seconds = minutes * 60 + seconds

timer(total_seconds)