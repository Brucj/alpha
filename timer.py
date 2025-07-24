import time
import threading

def format_time(total_seconds):
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    microseconds = int((total_seconds - int(total_seconds)) * 1_000_000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{microseconds:06}"

def countdown(total_seconds, reset_event):
    original_time = total_seconds
    while total_seconds > 0:
        if reset_event.is_set():
            total_seconds = original_time
            reset_event.clear()
        print(f"\rTime left: {format_time(total_seconds)}", end="")
        time.sleep(0.1)
        total_seconds -= 0.1
    print("\nTime's up!")

def listen_for_reset(reset_event):
    while True:
        user_input = input("\nType 'reset' to reset the timer: ").strip().lower()
        if user_input == 'reset':
            reset_event.set()

if __name__ == "__main__":
    try:
        hours = int(input("Enter hours: ") or 0)
        minutes = int(input("Enter minutes: ") or 0)
        seconds = int(input("Enter seconds: ") or 0)
        microseconds = int(input("Enter microseconds: ") or 0)
        total_seconds = hours * 3600 + minutes * 60 + seconds + microseconds / 1_000_000

        # Event to signal reset
        reset_event = threading.Event()

        # Thread for listening to reset command
        listener_thread = threading.Thread(target=listen_for_reset, args=(reset_event,), daemon=True)
        listener_thread.start()

        countdown(total_seconds, reset_event)
    except ValueError:
        print("Please enter valid numbers.")

