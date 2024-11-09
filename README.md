# FaceByShrey - Face Recognition with Real-Time Annotation

FaceByShrey is a Python-based face recognition application using OpenCV, MediaPipe, and Face Recognition libraries. The program detects faces in real-time from a webcam feed, recognizes previously seen faces, and asks for the name whenever it encounters a new face. This name is then displayed as an annotation on the screen for future detections.

## Features
- **Real-Time Face Detection**: Uses MediaPipe for initial face detection and annotations.
- **Face Recognition**: Detects known faces using `face_recognition` library and assigns names to each.
- **Interactive Naming**: For each new face, prompts the user to input a name.
- **Efficient Processing**: Uses threading and frame skipping to optimize performance.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd FaceByShrey
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe face-recognition numpy
   ```

3. Run the program:
   ```bash
   python face_recognition_app.py
   ```

## Usage

- When you run the application, it will open the webcam feed in a new window.
- Whenever a new face appears, it will prompt you in the console to enter a name for that face.
- The name will then be displayed as a label on the screen each time that face is detected.

### Keyboard Controls
- **Press `Esc`** to exit the application.

## Code Overview

- **MediaPipe Initialization**: Sets up MediaPipe's face detection model for locating faces.
- **Face Recognition and Labeling**: Uses `face_recognition` to check if detected faces match known faces, and updates the annotation with names.
- **Threaded Recognition**: Face recognition runs in a separate thread to avoid blocking the main loop, improving frame rate.
- **Performance Optimization**: Skips every other frame to reduce CPU usage and enhance real-time performance.

## Dependencies
- `opencv-python`: For handling webcam feed and displaying the results.
- `mediapipe`: For fast and efficient face detection.
- `face-recognition`: To encode and compare facial features.
- `numpy`: For efficient array handling.

## Future Enhancements
- Save and load known faces and names for recognition across sessions.
- Improve performance by reducing CPU usage and adding support for GPU processing.

## License
This project is licensed under the MIT License.
```

Replace `<repository-url>` with your repository's URL to complete the README file.
