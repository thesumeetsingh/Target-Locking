import os
import cv2

def load_trained_models():
    trained_models = {}  # Dictionary to store loaded trained models

    # Load trained models from the "trainedmodel" folder
    trainedmodel_path = os.path.join(os.getcwd(), "trainedmodel")
    for model_file in os.listdir(trainedmodel_path):
        if model_file.endswith("_model"):
            name = model_file.split("_")[0]  # Extract username from model filename
            model_path = os.path.join(trainedmodel_path, model_file)
            # Placeholder for loading the actual trained model
            # You would replace this with your model loading code
            trained_models[name] = model_path  # Store model path in the dictionary

    return trained_models

def detect_and_recognize_faces(frame, trained_models):
    # Convert frame to grayscale for face recognition
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face_roi = gray_frame[y:y+h, x:x+w]

        # Placeholder for face recognition (replace this with your actual recognition code)
        recognized = False
        for name, model_path in trained_models.items():
            # Here you would use your actual face recognition algorithm or library
            # For demonstration, we'll just check if the model file exists
            if os.path.exists(model_path):
                recognized = True
                cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                break

        if not recognized:
            cv2.putText(frame, "(unidentified)", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return frame

def main():
    # Load trained models
    trained_models = load_trained_models()

    # Initialize the camera
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Detect and recognize faces in the frame
        frame = detect_and_recognize_faces(frame, trained_models)

        # Display the frame
        cv2.imshow("Face Recognition", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
