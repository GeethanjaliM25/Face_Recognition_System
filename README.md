# 👤 Face Recognition System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Face Recognition](https://img.shields.io/badge/Face--Recognition-AI-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📌 Overview

A **web-based Face Recognition System** built using **Streamlit**, **OpenCV**, and the `face_recognition` library that detects and identifies faces from uploaded images and live webcam feeds


The system uses **pre-trained face encodings** with **Euclidean distance-based matching** and strict thresholding to improve accuracy and reduce false positives.

---

# ✨ Features 

- 👤 Face Detection & Recognition
- 📤 Image Upload Support
- 🎥 Live Webcam Detection
- 🟩 Bounding Box Visualization
- 📊 Confidence Score Display
- ❌ Unknown Face Detection
- ⚡ Fast & Interactive Streamlit UI.

---

# 🧠 How It Works

## 1️⃣ Face Detection
Faces are detected using the `face_recognition` library.

## 2️⃣ Face Encoding
Each detected face is converted into a **128-dimensional embedding vector**.

## 3️⃣ Face Matching
The input face encoding is compared with stored face encodings using **Euclidean distance**.

## 4️⃣ Thresholding

- If distance `< threshold` → Known Person
- Else → Unknown Person

---

# 🏗️ Project Structure

```bash
face_recognition_pretrained/
│── app.py
│── train_model.py
│── face_recognizer_XXXX.pkl
│── requirements.txt
│── README.md
│
├── dataset/
│   ├── Person1/
│   ├── Person2/
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
└── venv_py39/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repository-link>
cd face_recognition_pretrained
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv_py39
```

### Activate Environment

```bash
venv_py39\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install dlib-bin
pip install face-recognition --no-deps
pip install face-recognition-models Click
pip install streamlit opencv-python numpy pandas pillow
```

---

# 🧠 Train the Model

## Add Images to Dataset

```bash
dataset/
   ├── Geethanjali/
   ├── Punya/
```

## Run Training Script

```bash
python train_model.py
```

This generates:

```bash
face_recognizer_XXXXXXXX.pkl
```

---

# ▶️ Run the Application

```bash
python -m streamlit run app.py
```

Open in browser:

```bash
http://localhost:8501
```

---

# 🎯 Usage

## 📤 Image Mode

- Upload an image
- System detects and recognizes faces automatically

## 🎥 Webcam Mode

- Start webcam
- Real-time face recognition begins

---

# ⚙️ Configuration

```python
THRESHOLD = 0.35
MIN_CONFIDENCE = 60
```

- Lower threshold → More strict recognition
- Helps reduce false matches

---

# 🚀 Future Enhancements

- 📸 Save unknown faces automatically
- 🧾 Attendance Management System
- 🗄️ Database Integration
- 📊 Analytics Dashboard
- ☁️ Cloud Deployment

---

# 📌 Technologies Used

- Python
- Streamlit
- OpenCV
- face_recognition
- NumPy
- Pillow

---

# 👩‍💻 Author

**Geethanjali M**  
B.E Student | AI & ML Enthusiast

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork it
- 📢 Share it

---
