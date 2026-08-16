# 🏥 MediFlow AI: Touchless Medical Screen Navigation Using Hand Gesture Recognition

MediFlow AI is an intelligent, touchless medical image navigation system that enables healthcare professionals to interact with medical images using hand gestures instead of traditional input devices such as a mouse or keyboard.

The system uses Artificial Intelligence, Computer Vision, Deep Learning, and Hand Gesture Recognition to create a contactless environment for navigating medical images.

In hospitals, doctors often need to examine X-rays, CT scans, MRI scans, and other medical images while performing procedures. Touching a keyboard or mouse repeatedly can interrupt the workflow and increase the risk of contamination.

MediFlow AI solves this problem by allowing users to control medical images using simple hand gestures captured through a webcam.

---

# 🎯 Problem Statement

Medical professionals frequently interact with digital medical images while performing examinations and procedures.

Traditional input devices such as keyboards and mice require physical contact, which can:

- Increase the risk of contamination
- Interrupt medical procedures
- Reduce workflow efficiency
- Create hygiene concerns in sterile environments

There is a need for a touchless and intuitive system that allows doctors to interact with medical images without physical contact.

---

# 💡 Proposed Solution

MediFlow AI introduces a gesture-controlled interface that uses a webcam to detect and recognize hand movements in real time.

The system captures hand gestures, processes them using MediaPipe and TensorFlow, and performs specific actions such as:

- Moving the pointer
- Navigating between images
- Zooming in
- Zooming out

This creates a completely touch-free interaction system for medical image navigation.

---

# ✨ Key Features

- 🖐️ Real-time hand gesture recognition
- 🏥 Touchless medical image navigation
- 🔍 Zoom in and zoom out functionality
- ➡️ Next image navigation
- ⬅️ Previous image navigation
- 🖱️ Pointer control using finger movement
- ⚡ Fast gesture detection
- 📷 Webcam-based interaction
- 🤖 AI-powered image processing
- 🧠 Deep learning-based hand recognition

---

# 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Backend development |
| OpenCV | Image processing |
| MediaPipe | Hand landmark detection |
| TensorFlow | Deep learning |
| NumPy | Numerical computations |
| Flask | Web framework |
| PyAutoGUI | Screen control |
| Keras | Neural network implementation |

---

# 🧠 AI and Machine Learning Concepts Used

The project combines multiple AI techniques:

### Computer Vision

- Real-time video capture
- Image preprocessing
- Frame analysis

### Deep Learning

- Hand gesture classification
- Feature extraction
- Model prediction

### MediaPipe Hand Tracking

- Hand landmark detection
- Finger position identification
- Gesture mapping

### Human-Computer Interaction

- Gesture-based navigation
- Touchless user interface
- Real-time user feedback

---

# ✋ Hand Gestures and Their Functions

| Gesture | Action |
| --- | --- |
| ☝️ One Finger | Pointer Control |
| ✌️ Two Fingers | Next Image |
| 🤟 Three Fingers | Previous Image |
| ✊ Closed Hand | Zoom In |
| 🖐️ Five Fingers | Zoom Out |

---

# 🔄 System Workflow

1. The webcam captures the user's hand movements.

2. OpenCV processes the video frames.

3. MediaPipe detects hand landmarks.

4. TensorFlow analyzes the extracted features.

5. The trained model recognizes the gesture.

6. The gesture is mapped to a specific command.

7. The corresponding action is executed.

---

# 🏗️ Project Architecture

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

# 📁 Project Structure

```
MediFlow-AI
│
├── app.py
├── .gitignore
├── README.md
├── LICENSE
│
├── medical_images
│ ├── 1.jpg
│ ├── 2.jpg
│ ├── 3.jpg
│ └── ...
│
├── model
│ └── ResNet50_Hand_frac.h5
│
└── venv (ignored)
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/NIHAL-V-K/MediFlow-AI.git
```

Move into the project directory:

```bash
cd MediFlow-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

# 📦 Required Libraries

```bash
pip install opencv-python
pip install mediapipe
pip install tensorflow
pip install numpy
pip install flask
pip install pyautogui
pip install pillow
```

---

# 🚀 Future Enhancements

- Voice-assisted navigation
- 3D medical image visualization
- Multiple gesture support
- Hospital database integration
- DICOM image support
- Gesture customization
- Advanced AI-based recognition
- Improved medical image analysis

---

# 🎓 Academic Information

**Project Title:**

MediFlow AI: Touchless Medical Screen Navigation Using Hand Gesture Recognition

**Course:**

Master of Computer Applications (MCA)

**Project Type:**

Artificial Intelligence and Computer Vision Project

---

# 👨‍💻 Developed By

**Nihal VK**

MCA Student

Presidency University, Bengaluru

---

# ⭐ If you like this project, please consider giving it a star.
