# MediFlow AI: Touchless Medical Screen Navigation Using Hand Gesture Recognition

An AI-powered medical image navigation system that enables healthcare professionals to interact with medical images through real-time hand gesture recognition, eliminating the need for traditional input devices and creating a more efficient and hygienic clinical environment.

## Overview

MediFlow AI is an intelligent medical image navigation system that enables healthcare professionals to interact with medical images through hand gestures instead of traditional input devices such as a mouse or keyboard.

The project combines Artificial Intelligence, Computer Vision, Deep Learning, and Hand Gesture Recognition to create a touchless environment for medical image manipulation. The system captures hand movements through a webcam, recognizes predefined gestures, and converts them into navigation commands.

The primary objective of this project is to improve workflow efficiency and reduce physical contact with computer peripherals in medical environments.

---

## Problem Statement

Medical professionals frequently interact with digital medical images such as X-rays, CT scans, MRI scans, and ultrasound images during examinations and medical procedures.

Traditional input devices require physical contact, which can create several challenges:

- Increased risk of contamination
- Interruptions during medical procedures
- Reduced workflow efficiency
- Difficulty maintaining sterile conditions

A contactless system that allows medical professionals to navigate medical images without touching a keyboard or mouse can significantly improve the clinical workflow.

---

## Proposed Solution

MediFlow AI provides a gesture-controlled interface that enables users to navigate medical images using simple hand movements.

The system captures video frames through a webcam and processes them using Computer Vision and Deep Learning techniques. Hand landmarks are detected and analyzed, and the recognized gestures are mapped to specific navigation commands.

The entire interaction process is performed in real time, creating a smooth and intuitive user experience.

---

## Objectives

- Develop a touchless medical image navigation system
- Implement real-time hand gesture recognition
- Reduce dependence on traditional input devices
- Improve workflow efficiency in medical environments
- Create a hygienic and contactless user interface

---

## Key Features

- Real-time hand gesture recognition
- Medical image navigation using hand movements
- Pointer control
- Image zoom functionality
- Next and previous image navigation
- Webcam-based interaction
- Deep learning-based gesture recognition
- Real-time image processing

---

## Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Core programming language |
| OpenCV | Image processing |
| MediaPipe | Hand landmark detection |
| TensorFlow | Deep learning |
| Keras | Neural network implementation |
| NumPy | Numerical computation |
| Flask | Backend framework |
| PyAutoGUI | System interaction and screen control |

---

## Artificial Intelligence and Machine Learning Techniques

### Computer Vision

- Video frame capture
- Image preprocessing
- Frame analysis

### Deep Learning

- Gesture classification
- Feature extraction
- Prediction generation

### Hand Tracking

- Hand landmark detection
- Finger position identification
- Gesture mapping

### Human-Computer Interaction

- Gesture-based navigation
- Real-time interaction
- Contactless user interface

---

## Gesture Controls

| Gesture | Function |
| --- | --- |
| One Finger | Pointer Control |
| Two Fingers | Next Image |
| Three Fingers | Previous Image |
| Closed Hand | Zoom In |
| Five Fingers | Zoom Out |

---

## System Workflow

1. Capture hand movements through a webcam.
2. Process video frames using OpenCV.
3. Detect hand landmarks using MediaPipe.
4. Extract hand features.
5. Analyze features using the trained TensorFlow model.
6. Recognize the corresponding gesture.
7. Execute the associated navigation command.

---

## System Architecture

```
Webcam
   ↓
OpenCV
   ↓
MediaPipe
   ↓
TensorFlow Model
   ↓
Gesture Recognition
   ↓
Medical Image Navigation
```

---

## Project Structure

```
MediFlow-AI
│
├── app.py
├── README.md
├── LICENSE
├── .gitignore
│
├── medical_images/
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   └── ...
│
├── model/
│   └── ResNet50_Hand_frac.h5
│
└── venv/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/NIHAL-V-K/MediFlow-AI.git
```

Navigate to the project directory:

```bash
cd MediFlow-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Required Dependencies

```bash
opencv-python
mediapipe
tensorflow
numpy
flask
pyautogui
pillow
```

---

## Future Enhancements

- Voice-controlled navigation
- Support for additional hand gestures
- 3D medical image visualization
- DICOM image support
- Gesture customization
- Integration with hospital information systems
- Improved gesture recognition accuracy

---

## Applications

- Hospitals
- Diagnostic centers
- Radiology departments
- Surgical environments
- Medical training laboratories
- Contactless healthcare systems

---

## Conclusion

MediFlow AI demonstrates how Artificial Intelligence and Computer Vision can be integrated to create a practical healthcare solution.

By replacing traditional input devices with hand gesture recognition, the system provides a more efficient, intuitive, and hygienic approach to medical image navigation. This project highlights the potential of AI-driven touchless interfaces in modern healthcare environments.

---

## Developer

**Nihal VK**

Master of Computer Applications (MCA)

Presidency University, Bengaluru
