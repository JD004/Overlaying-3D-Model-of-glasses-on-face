# 🕶️ Overlaying 3D Model of Glasses on Face

This project overlays a 3D glasses model onto a human face using a webcam feed. It uses facial landmark detection and 3D model rendering to create a virtual try-on system. This is useful for AR/VR applications, eyewear retail, or just fun experiments in computer vision.

---

## 📌 Features

- ✅ Real-time face tracking with MediaPipe or Dlib
- 🕶️ Accurate 3D model overlay based on facial landmarks
- 📹 Webcam-based live preview
- 💡 Simple and modular Python codebase

---

## 📂 Project Structure

Overlaying-3D-Model-of-glasses-on-face/
│
├── main.py # Entry point of the application
├── model3D.py # Handles 3D model loading and projection
├── faceTracker.py # Face and landmark tracking logic
├── data/
│ ├── data.obj # 3D model of the glasses
│ └── data.obj.mtl # Material file for the model
├── README.md # This file
└── requirements.txt # Python dependencies
