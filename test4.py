import cv2
import numpy as np
import time
from pyfirmata import Arduino, util

# Initialize Arduino board (adjust port as needed)
board = Arduino('COM3')  # Change COM3 to your Arduino's port

# Define pins for servos
base_pin = board.get_pin('d:9:s')      # Pin 9 for base servo
shoulder_pin = board.get_pin('d:10:s') # Pin 10 for shoulder servo
elbow_pin = board.get_pin('d:11:s')    # Pin 11 for elbow servo

# Constants for arm dimensions (in inches or any unit)
L1 = 5.0  # Length of shoulder to elbow (shoulder servo to elbow joint)
L2 = 5.0  # Length of elbow to end effector (elbow joint to laser)

# Function to calculate inverse kinematics angles
def inverse_kinematics(x, y):
    try:
        # Calculate distances and angles
        d = np.sqrt(x**2 + y**2)
        alpha = np.arctan2(y, x)
        beta = np.arccos((L1**2 + d**2 - L2**2) / (2 * L1 * d))
        theta1 = alpha + beta
        theta2 = np.arccos((L1**2 + L2**2 - d**2) / (2 * L1 * L2))
        theta3 = np.pi - theta2
        
        # Check if angles are valid (not NaN)
        if not np.isnan(theta1) and not np.isnan(theta3):
            return np.degrees(theta1), np.degrees(theta3)
        else:
            return None, None
    except Exception as e:
        print("Error in inverse kinematics calculation:", e)
        return None, None


# Function to move the robotic arm to specified angles
def move_arm(theta1, theta3):
    base_pin.write(theta1)
    elbow_pin.write(theta3)

# Initialize video capture
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Example face detection and tracking (replace with your actual code)
    # Assume (x, y) are the coordinates of the detected face
    x, y = 100, 100  # Example coordinates, replace with actual detection

    # Perform inverse kinematics
    theta1, theta3 = inverse_kinematics(x, y)
    if theta1 is not None and theta3 is not None:
        move_arm(theta1, theta3)

    # Display the frame with laser position (for visualization)
    cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)  # Green dot at face position
    cv2.imshow("Frame", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()

# Close Arduino connection
board.exit()
