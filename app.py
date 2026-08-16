import cv2
import mediapipe as mp
import os
import time
from tensorflow.keras.models import load_model
import numpy as np

# =========================
# Load Medical Images
# =========================

folder_path = "medical_images"

images = []

valid_extensions = (".jpg", ".jpeg", ".png")

for file in sorted(os.listdir(folder_path)):

    if file.lower().endswith(valid_extensions):

        path = os.path.join(folder_path, file)

        img = cv2.imread(path)

        if img is not None:

            img = cv2.resize(img, (800, 600))

            images.append(img)

print("Total Images Loaded:", len(images))

current_image = 0
zoom_scale = 1.0
last_predicted_image = -1
disease = "Loading..."
confidence = 0
model = load_model("model/ResNet50_Hand_frac.h5")
print("MODEL LOADED SUCCESSFULLY")
predictions = [
    ("Normal", "95%"),
    ("Pneumonia", "91%"),
    ("COVID Suspected", "88%"),
    ("Lung Infection", "93%"),
    ("Normal", "90%"),
    ("Tuberculosis", "89%")
]

# =========================
# MediaPipe Setup
# =========================

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)

mp_draw = mp.solutions.drawing_utils

# =========================
# Webcam
# =========================

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

last_gesture_time = time.time()

while True:

    success, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    gesture = "No Gesture"

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            tips = [4, 8, 12, 16, 20]

            fingers = []

            # Thumb
            if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other Fingers
            for tip in tips[1:]:

                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers.append(1)

                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)

            current_time = time.time()

            # =========================
            # Gesture Logic
            # =========================

            if current_time - last_gesture_time > 1.5:

                # Closed Fist → Zoom Out
                if total_fingers == 0:

                    gesture = "ZOOM OUT"
                    zoom_scale -= 0.1

                if zoom_scale < 0.5:
                    zoom_scale = 0.5

                    zoom_scale -= 0.1

                    if zoom_scale < 0.5:
                        zoom_scale = 0.5

                    last_gesture_time = current_time

                # Two Fingers → Next Image
                elif total_fingers == 2:

                    gesture = "NEXT IMAGE"

                    current_image = (current_image + 1) % len(images)

                    if current_image >= len(images):
                        current_image = 0

                    last_gesture_time = current_time

                # Four Fingers → Previous Image
                elif total_fingers == 4:

                    gesture = "PREVIOUS IMAGE"

                    current_image = (current_image - 1) % len(images)

                    if current_image < 0:
                        current_image = len(images) - 1

                    last_gesture_time = current_time

                # Thumbs Up → Zoom In
                elif (
                    fingers[0] == 1 and
                    fingers[1] == 0 and
                    fingers[2] == 0 and
                    fingers[3] == 0 and
                    fingers[4] == 0
                ):
 
                    gesture = "ZOOM IN"
                    zoom_scale += 0.1

                if zoom_scale > 3:
                    zoom_scale = 3

                    zoom_scale += 0.1

                    if zoom_scale > 3:
                        zoom_scale = 3

                    last_gesture_time = current_time

    # =========================
    # Show Gesture
    # =========================

    cv2.putText(
        frame,
        gesture,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        3
    )

    # =========================
    # Show Medical Image
    # =========================

    image = images[current_image]

    h, w = image.shape[:2]

    new_w = int(w * zoom_scale)
    new_h = int(h * zoom_scale)

    resized = cv2.resize(image, (new_w, new_h))
        # Image Counter
    cv2.putText(
        resized,
        f"Image: {current_image + 1} / {len(images)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    # REAL ML PREDICTION
    predict_img = cv2.resize(image, (224, 224))

    predict_img = predict_img / 255.0

    predict_img = np.expand_dims(predict_img, axis=0)
    
    prediction = model.predict(predict_img, verbose=0)

    confidence = float(np.max(prediction)) * 100

    if np.argmax(prediction) == 1:
        disease = "FRACTURED"
    else:
        disease = "UNFRACTURED"

    cv2.putText(
        resized,
        f"Prediction: {disease}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )
    cv2.putText(
        resized,
        f"Confidence: {confidence:.2f}%",
        (20,160),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,0),
        2
    )

    # Zoom Percentage
    zoom_percent = int(zoom_scale * 100)

    cv2.putText(
        resized,
        f"Zoom: {zoom_percent}%",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("Medical Image Viewer", resized)

    cv2.imshow("MediFlow AI", frame)

    # Exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()