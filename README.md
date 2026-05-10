# 👤 Face Recognition System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![OpenCV] (https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Face Recognition](https://img.shields.io/badge/Face--Recognition-AI-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

A **web-based Face Recognition System** built using **Streamlit** that detects and identifies faces in images and live webcam feed.

This system uses **pre-trained face encodings** and applies **Euclidean distance-based matching with strict thresholding** to ensure accurate recognition and avoid false positives.

--

## ✨ Features

* 👤 Face Detection & Recognition
* 📤 Image Upload Support
* 🎥 Live Webcam Detection
* 🟩 Bounding Box Visualization
* 📊 Confidence Score Display
* ❌ Unknown Face Detection (Strict Thresholding)
* ⚡ Fast and Interactive UI using Streamlit

---

## 🧠 How It Works

1. **Face Detection**
   Detects faces using `face_recognition` library.

2. **Face Encoding**
   Converts faces into 128-dimensional vectors.

3. **Face Matching**
   Compares input face with trained faces using **Euclidean distance**.

4. **Thresholding**

   * If distance < threshold → Known Person
   * Else → Unknown

---

## 🏗️ Project Structure

```
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

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd face_recognition_pretrained
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv_py39
```

Activate:

```bash
venv_py39\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install dlib-bin
pip install face-recognition --no-deps
pip install face-recognition-models Click
pip install streamlit opencv-python numpy pandas pillow
```

---

## 🧠 Train Model

1. Add images to dataset:

```
dataset/
   ├── Geethanjali/
   ├── Punya/
```

2. Run training:

```bash
python train_model.py
```

👉 This generates:

```
face_recognizer_XXXXXXXX.pkl
```

---

## ▶️ Run Application

```bash
python -m streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🎯 Usage

### 📤 Image Mode

* Upload an image
* System detects and recognizes faces

### 🎥 Webcam Mode

* Start webcam
* Real-time face recognition

---

## ⚙️ Configuration

```python
THRESHOLD = 0.35
MIN_CONFIDENCE = 60
```

* Lower threshold → more strict
* Prevents false matches

---

## 🚀 Future Enhancements

* 📸 Save unknown faces automatically
* 🧾 Attendance system
* 🗄️ Database integration
* 📊 Analytics dashboard
* ☁️ Deployment on cloud

---

## 📌 Technologies Used

* Python
* Streamlit
* OpenCV
* face_recognition
* NumPy
* Pillow

---

## 👩‍💻 Author

**Geethanjali M**
B.E Student | AI & ML Enthusiast

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---
