import time
def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds}s", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
countdown(60)  # 1-minute timer
