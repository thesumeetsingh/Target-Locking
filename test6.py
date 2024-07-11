from pyfirmata import Arduino, util
import time

# Define the Arduino board port (this might be different on your system)
board = Arduino('COM3')  # Update 'COM3' with your actual port

# Define the pins for the servos
servo_pin_9 = board.get_pin('d:9:s')  # Servo on pin 9
servo_pin_10 = board.get_pin('d:10:s')  # Servo on pin 10

# Function to smoothly move the servo from start_angle to end_angle
def move_servo_smoothly(servo, start_angle, end_angle, step=1, delay=0.05):
    if start_angle < end_angle:
        for angle in range(start_angle, end_angle + 1, step):
            servo.write(angle)
            time.sleep(delay)
    else:
        for angle in range(start_angle, end_angle - 1, -step):
            servo.write(angle)
            time.sleep(delay)

try:
    while True:
        # Move servo on pin 9 from 0 to 180 degrees
        move_servo_smoothly(servo_pin_9, 0, 180)
        time.sleep(1)  # Wait for 1 second
        
        # Move servo on pin 10 from 180 to 0 degrees
        move_servo_smoothly(servo_pin_10, 180, 0)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    board.exit()
