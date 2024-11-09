import cv2
import mediapipe as mp
import face_recognition
import numpy as np
import threading
# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
# Dictionary to store known faces and their names
known_face_encodings = []
known_face_names = []
# Function to get user input for a new face's name
def add_new_face(face_encoding):
    global known_face_encodings, known_face_names
    name = input("Enter the name for the detected face: ")
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)
# For webcam input
cap = cv2.VideoCapture(0)
frame_count = 0  # Counter to skip frames for performance optimization
frame_skip = 2  # Skip every other frame for performance
resize_factor = 0.5  # Resize factor for reducing resolution

# Define a worker thread function for face recognition
def recognize_faces(frame):
    # Convert the BGR image to RGB for face_recognition processing
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces using face_recognition
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
    # Check if faces match known faces and annotate
    flipped_frame = cv2.flip(frame, 1)  # Flip the image horizontally
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]
        else:
            add_new_face(face_encoding)  # Prompt for a name for the new face
        # Calculate the flipped rectangle coordinates
        flipped_left = flipped_frame.shape[1] - right
        flipped_right = flipped_frame.shape[1] - left
        # Draw the face rectangle on the flipped image
        cv2.rectangle(flipped_frame, (flipped_left, top), (flipped_right, bottom), (0, 255, 0), 2)  # Green rectangle for the face
        # Draw the name text in the correct position (mirrored)
        cv2.putText(flipped_frame, name, (flipped_left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return flipped_frame

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        # Resize the image to reduce processing load
        image = cv2.resize(image, (0, 0), fx=resize_factor, fy=resize_factor)
        
        # Increment frame count for skipping
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue  # Skip frames to improve performance
        
        # Process MediaPipe Face Detection for visualization
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Draw detections on the image (annotations like bounding boxes)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
        # Run face recognition in a separate thread for better performance
        flipped_image = recognize_faces(image)
        # Display the flipped (mirrored) image with the correct annotations
        cv2.imshow('FaceByShrey', flipped_image)
        # Exit on pressing the 'Esc' key
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
