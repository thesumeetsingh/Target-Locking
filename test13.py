from pyfirmata import Arduino, SERVO
import time

# Define Arduino board and pins
board = Arduino('/dev/ttyACM0')  # Adjust the port as needed
servo_pin1 = board.get_pin('d:9:s')  # Servo on pin 9
servo_pin2 = board.get_pin('d:10:s')  # Servo on pin 10

# Define servo positions
min_angle = 0
max_angle = 90
delay_time = 0.05  # Adjust delay for speed control

try:
    while True:
        # Move both servos simultaneously
        for angle in range(min_angle, max_angle + 1):
            servo_pin1.write(angle)
            servo_pin2.write(angle)
            time.sleep(delay_time)

        # Move back to initial position
        for angle in range(max_angle, min_angle - 1, -1):
            servo_pin1.write(angle)
            servo_pin2.write(angle)
            time.sleep(delay_time)

except KeyboardInterrupt:
    # Clean up on Ctrl+C
    board.exit()
    print("\nProgram terminated.")
