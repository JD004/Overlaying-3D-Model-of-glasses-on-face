# 3D Glasses Overlay Project

This project overlays a 3D glasses model onto a user's face in real-time using **MediaPipe**, **OpenCV**, and **NumPy**. The program captures video from a webcam, detects facial landmarks, and projects a 3D model (such as glasses) onto the user's face based on the real-time landmarks.

## Features

- **Real-time facial landmark detection** using MediaPipe's FaceMesh.
- **Dynamic 3D glasses overlay**: A 3D model of glasses is projected onto the user's face and scales accordingly.
- **Interactive**: The glasses adjust in position and size depending on the face's orientation and dimensions.

## Prerequisites

Before running the project, make sure the following dependencies are installed:

- **Python 3.x**: Ensure that Python is installed on your system.
- **OpenCV**: For video processing and computer vision tasks.
- **MediaPipe**: For facial landmark detection and facial mesh generation.
- **NumPy**: For matrix manipulation and computations.

### Install the required dependencies:

```bash
pip install opencv-python mediapipe numpy
```
### Project Setup

Clone Repo
To get started, clone the project repository to your local machine:

```bash
git clone https://github.com/your-username/3D-Glasses-Overlay.git
cd 3D-Glasses-Overlay
```
2. Download the 3D Model
Ensure that you have a 3D model in .obj format (such as glasses) to overlay onto the face. The model should be named oculos.obj (or modify the code accordingly to reflect the correct name). Place the .obj file in the same directory as the Python script.

3. Webcam Setup
Ensure your webcam is functioning properly as the program uses the webcam feed to detect facial landmarks and project the glasses model.

##Running the Program
Once everything is set up, you can run the project by executing the following command:

```bash
python glasses_overlay.py
```
##How to Use
Run the Program:

Execute the script using the command python glasses_overlay.py.
The webcam window will open, and you will see the 3D glasses overlay on your face.
Adjusting the Webcam Position:

If the glasses do not align correctly, adjust the position and orientation of your webcam. Ensure your face is in the frame with proper lighting for accurate landmark detection.
Exit the Program:

To stop the webcam and close the program, press the Esc key.

##License
This project is licensed under the MIT License - see the LICENSE file for details.

##Acknowledgments
OpenCV: For real-time computer vision tools.
MediaPipe: For face detection and facial mesh algorithms.
NumPy: For matrix operations.
3D Object File Format (.obj): For representing 3D models.


### Key Sections in the README:
1. **Project Overview**: A brief description of the project and what it does.
2. **Features**: A summary of the features of the project.
3. **Prerequisites**: Information about the required dependencies and how to install them.
4. **Project Setup**: Instructions to clone the repo, set up the project, and place the 3D model file.
5. **Running the Program**: Instructions to run the program and details on how the code works.
6. **How to Use**: Step-by-step instructions for using the program.
7. **Future Improvements**: Suggestions for expanding the project in the future.
8. **License**: Licensing details.
9. **Acknowledgments**: Credits to libraries used in the project.

This should give users a clear understanding of how to use the project, set it up, and troubleshoot any issues they might encounter.
