import os
import cv2

def create_folder(name):
    # Create a folder with the specified name if it doesn't exist
    folder_path = os.path.join(os.getcwd(), name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder '{name}' created successfully.")
    else:
        print(f"Folder '{name}' already exists.")

def create_trained_model_folder():
    # Create a "trainedmodel" folder if it doesn't exist
    folder_path = os.path.join(os.getcwd(), "trainedmodel")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print("Folder 'trainedmodel' created successfully.")

def capture_images(name):
    # Initialize the camera
    camera = cv2.VideoCapture(0)
    count = 1  # Counter for captured images

    # Load Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = camera.read()
        cv2.imshow("Capture Images", frame)

        key = cv2.waitKey(1)
        if key == ord('y'):  # Press 'y' to capture an image
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                face_roi = frame[y:y+h, x:x+w]
                image_path = os.path.join(os.getcwd(), name, f"{name}{count}.jpg")
                cv2.imwrite(image_path, face_roi)
                print(f"Image {count} captured.")
                count += 1
        elif key == ord('q'):  # Press 'q' to quit
            break

    camera.release()
    cv2.destroyAllWindows()

def train_model(name):
    # Placeholder for training code
    # You would replace this with your actual model training code
    print(f"Training model for user: {name}")
    # For demonstration, we'll just create a dummy trained model file
    model_path = os.path.join(os.getcwd(), "trainedmodel", f"{name}_model")
    open(model_path, 'a').close()  # Create an empty file
    print(f"Trained model saved as: {name}_model")

def main():
    # Take user's name as input
    name = input("Enter your name: ")
    create_folder(name)

    # Create the "trainedmodel" folder if it doesn't exist
    create_trained_model_folder()

    # Capture images until 'q' is pressed
    capture_images(name)

    # Train model and save it with the specified name format
    train_model(name)

if __name__ == "__main__":
    main()
