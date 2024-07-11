from pyfirmata import Arduino
import time

board = Arduino()  # Initialize the Arduino board
servo_pin = 9  # Change this to your actual servo pin number
servo = board.get_pin(f'd:{servo_pin}:s')

try:
    while True:
        servo.write(0)  # Move to 0 degrees
        time.sleep(1)
        servo.write(180)  # Move to 180 degrees
        time.sleep(1)

except KeyboardInterrupt:
    servo.write(90)  # Return to 90 degrees before exiting
    board.exit()
