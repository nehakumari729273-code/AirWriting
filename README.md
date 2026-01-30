Air Writing System Using Hand Gestures
======================================
This project implements an air writing and drawing system that allows a user to write or draw on a virtual canvas using hand gestures captured through a webcam. The system works in real time and does not require any physical contact with the screen or external hardware.
The project is built using OpenCV for video processing and MediaPipe for accurate hand-landmark detection.

Project Overview
=================
The Air Writing System tracks hand movements using a camera and interprets specific finger combinations as commands such as drawing, moving, erasing, changing color, and saving the drawing. A virtual canvas is maintained and merged with the live video feed to give the appearance of drawing in the air.
This project demonstrates practical use of computer vision, gesture recognition, and real-time image processing.

Functionalities
===============
Draw on a virtual canvas using a single finger
Move the cursor without drawing
Change drawing color using finger gestures
Erase content using a full-hand gesture
Save the drawing using a thumbs-up gesture
Automatic adjustment of brush thickness based on finger distance
Real-time processing through webcam

Hand Gesture Controls
=====================
| Gesture               | Function                     |
| --------------------- | ---------------------------- |
| Index finger only     | Drawing                      |
| Index + middle finger | Cursor movement (no drawing) |
| Three fingers         | Change drawing color         |
| All five fingers      | Erase                        |
| Thumb up              | Save drawing                 |

Technologies Used
=================

Python 3.10 or above
OpenCV
MediaPipe
NumPy

Installation and Setup
=======================
Step 1: Clone the Repository
git clone https://github.com/your-username/air-writing-system.git
cd air-writing-system

Step 2: Install Required Libraries
pip install opencv-python mediapipe numpy

Ensure that your system camera is enabled and accessible.

How to Run the Project
======================
python air_writing.py

The webcam window will open.
Perform gestures in front of the camera.
Press the Esc key to exit the application.

Working Explanation
====================

The webcam captures live video frames.
MediaPipe detects hand landmarks in each frame.
Finger states are calculated based on landmark positions.
Predefined gestures are mapped to actions such as draw, erase, and save.
Drawing is performed on a virtual canvas.
The canvas is merged with the video feed and displayed in real time.

Author
======
Neha
Computer Science Student
Interested in Computer Vision and Artificial Intelligence

License
=======
This project is open-source and can be used for learning and educational purposes.
