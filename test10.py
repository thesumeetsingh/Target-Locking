import cv2
from pyfirmata import Arduino, SERVO

# Define the pins for the servos
horizontal_pin = 3  # Change this to your actual pin number
vertical_pin = 4  # Change this to your actual pin number

# Initialize Arduino board
board = Arduino('COM3')  # Change COM3 to your Arduino's port

# Setup the servos
horizontal_servo = board.get_pin(f's:{horizontal_pin}:s')
vertical_servo = board.get_pin(f's:{vertical_pin}:s')

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to move the laser to a specific position
def move_laser(horizontal_angle, vertical_angle):
    horizontal_servo.write(horizontal_angle)
    vertical_servo.write(vertical_angle)

# Initialize video capture from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # If faces are detected, get the position of the first face (assuming only one person)
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        # Calculate angles based on face position (adjust as needed)
        horizontal_angle = int((x + w/2) * 180 / frame.shape[1])  # Convert x-coordinate to angle
        vertical_angle = int((y + h/2) * 180 / frame.shape[0])  # Convert y-coordinate to angle
        move_laser(horizontal_angle, vertical_angle)
    
    # Display the frame with rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Face Detection', frame)
    
    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()