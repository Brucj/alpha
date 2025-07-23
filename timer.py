print('Hello GitHub!')
print('This is a Python script.')
print('It is running successfully.')
import time
def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds}s", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stop procrastinating!")
countdown(60)  # 10-minute timer