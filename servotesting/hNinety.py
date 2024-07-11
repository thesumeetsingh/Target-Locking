from pyfirmata import Arduino, SERVO

# Define the pin for the servo (pin 9 in this case)
servo_pin = 9

# Initialize Arduino board
board = Arduino('COM3')  # Replace 'COM3' with your Arduino's port

# Attach the servo to the pin
servo = board.get_pin(f"d:{servo_pin}:s")

print("Moving servo to 0 degrees")
servo.write(0)
print("Servo moved to 0 degrees")
