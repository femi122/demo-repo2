import time

# Function for countdown
def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        time_format = f'{mins:02d}:{secs:02d}'  # Format the time as mm:ss
        print(time_format, end='\r')  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("Time's up!")

# Set the countdown time in seconds
countdown_time = 100

# Start the countdown
countdown(countdown_time)
