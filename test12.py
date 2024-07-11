from pyfirmata import Arduino, SERVO
import time

# Define the pin for the servo (pin 9 in this case)
servo_pin = 9

# Initialize Arduino board
board = Arduino('COM3')  # Replace 'COM3' with your Arduino's port

# Set the servo pin mode
board.digital[servo_pin].mode = SERVO

# Get the servo object
servo = board.digital[servo_pin]

# Move the servo to 0 degrees
servo.write(0)
time.sleep(1)  # Wait for the servo to reach the position

# Close the connection to the Arduino
board.exit()
