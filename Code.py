# Import the time module
import time

# Initialize the variable i to 100
i = 100

# Print "START" to the console
print("START")

# Print "Loading..." to the console
print("Loading...")

# Start a while loop that continues as long as i is greater than or equal to 0
while i >= 0:
    # Print the current value of i, followed by a space, without a newline at the end
    print(i, end = ' ')

    # Pause execution for 36 seconds
    time.sleep(36)

    # Decrement i by 1
    i -= 1
