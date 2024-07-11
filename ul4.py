import time
from pyfirmata import Arduino, util

# Define the pins for the ultrasonic sensor
trigger_pin = 9
echo_pin = 10

# Initialize the Arduino board
board = Arduino('COM3', baudrate=9600)  # Change COM3 to your Arduino's port
time.sleep(5)  # Allow time for the board to initialize

# Create a util object to read analog and digital pins
it = util.Iterator(board)
it.start()

# Set trigger_pin as OUTPUT
board.digital[trigger_pin].mode = 1  # 1 corresponds to OUTPUT in pyfirmata

# Function to get distance from ultrasonic sensor
def get_distance():
    # Send a short pulse to trigger the ultrasonic sensor
    board.digital[trigger_pin].write(1)
    time.sleep(0.00001)
    board.digital[trigger_pin].write(0)

    # Measure the duration of the pulse on the echo pin
    start_time = time.time()
    end_time = start_time  # Initialize end_time
    while board.digital[echo_pin].read() == 0:
        start_time = time.time()

    while board.digital[echo_pin].read() == 1:
        end_time = time.time()

    # Calculate duration of pulse and distance using speed of sound (343m/s)
    pulse_duration = end_time - start_time
    distance = pulse_duration * 34300 / 2  # Convert to centimeters
    return distance


try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)  # Wait for 1 second before taking next reading

except KeyboardInterrupt:
    print("Program terminated by user")
    board.exit()
