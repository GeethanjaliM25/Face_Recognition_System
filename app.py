import streamlit as st
import face_recognition
import pickle
import numpy as np
from PIL import Image, ImageDraw
import glob
import cv2

# 🎯 Load latest trained model
@st.cache_resource
def load_model():
    model_files = glob.glob("face_recognizer_*.pkl")

    if not model_files:
        st.error("❌ No trained model found. Run train_model.py first.")
        st.stop()

    MODEL_PATH = sorted(model_files)[-1]

    with open(MODEL_PATH, "rb") as f:
        encodings, names = pickle.load(f)

    return encodings, names

known_encodings, known_names = load_model()

st.title("👤 Face Recognition System")

# 🔥 STRICT SETTINGS (IMPORTANT)
THRESHOLD = 0.35
MIN_CONFIDENCE = 60

# 🎛 Mode selection
option = st.radio("Choose Mode", ["Upload Image", "Live Webcam"])

# =========================
# 📤 IMAGE UPLOAD MODE
# =========================
if option == "Upload Image":

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)

        face_locations = face_recognition.face_locations(img_array)
        face_encodings = face_recognition.face_encodings(img_array, face_locations)

        draw = ImageDraw.Draw(image)

        st.write(f"🔍 Faces detected: {len(face_locations)}")

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            name = "Unknown"
            confidence = 0

            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                best_distance = face_distances[best_match_index]

                confidence = round((1 - best_distance) * 100, 2)

                # ✅ STRICT CONDITION
                if best_distance < THRESHOLD and confidence > MIN_CONFIDENCE:
                    name = known_names[best_match_index]

            # 🟩 Draw box
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=3)

            # 🏷 Label
            draw.text((left, top - 10), f"{name} ({confidence}%)", fill=(0, 255, 0))

        st.image(image, caption="Result", use_column_width=True)

# =========================
# 🎥 WEBCAM MODE
# =========================
elif option == "Live Webcam":

    run = st.checkbox("Start Webcam")

    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        ret, frame = camera.read()

        if not ret:
            st.error("❌ Camera not working")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            name = "Unknown"
            confidence = 0

            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                best_distance = face_distances[best_match_index]

                confidence = round((1 - best_distance) * 100, 2)

                # ✅ STRICT CONDITION
                if best_distance < THRESHOLD and confidence > MIN_CONFIDENCE:
                    name = known_names[best_match_index]

            # 🟩 Draw box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # 🏷 Label
            cv2.putText(frame,
                        f"{name} ({confidence}%)",
                        (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2)

        FRAME_WINDOW.image(frame, channels="BGR")

    camera.release()