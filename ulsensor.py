import time
from pyfirmata import Arduino, util

# Define the pins for the ultrasonic sensor
trigger_pin = 9
echo_pin = 10

# Initialize the Arduino board
board = Arduino('COM3')  # Change COM3 to your Arduino's port
time.sleep(5)  # Allow time for the board to initialize

# Create a util object to read analog and digital pins
it = util.Iterator(board)
it.start()

# Define the pins as INPUT and OUTPUT
board.digital[trigger_pin].mode = board.digital[echo_pin].mode = board.MODES.OUTPUT

# Function to get distance from ultrasonic sensor
def get_distance():
    # Send a short pulse to trigger the ultrasonic sensor
    board.digital[trigger_pin].write(1)
    time.sleep(0.00001)
    board.digital[trigger_pin].write(0)

    # Measure the duration of the pulse on the echo pin
    duration = board.digital[echo_pin].read_pulse(1, timeout=0.1)  # Timeout in seconds

    # Calculate distance using speed of sound (assumed as 343m/s)
    if duration is not None:
        distance = duration * 34300 / 2  # Convert to centimeters
        return distance
    else:
        return None

try:
    while True:
        distance = get_distance()
        if distance is not None:
            print(f"Distance: {distance:.2f} cm")
        else:
            print("Failed to get distance")
        time.sleep(1)  # Wait for 1 second before taking next reading

except KeyboardInterrupt:
    print("Program terminated by user")
    board.exit()
