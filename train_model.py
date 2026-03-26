import face_recognition
import os
import pickle
from datetime import datetime

# 📁 Dataset folder (make sure this exists)
DATASET_PATH = "dataset"

known_encodings = []
known_names = []

print("🔄 Training started...\n")

# Loop through each person folder
for person_name in os.listdir(DATASET_PATH):
    person_folder = os.path.join(DATASET_PATH, person_name)

    if not os.path.isdir(person_folder):
        continue

    print(f"📂 Processing: {person_name}")

    # Loop through each image
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        try:
            # Load image
            image = face_recognition.load_image_file(image_path)

            # Get face encodings
            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(person_name)
                print(f"   ✅ Encoded: {image_name}")
            else:
                print(f"   ⚠️ No face found: {image_name}")

        except Exception as e:
            print(f"   ❌ Error: {image_name} → {e}")

# 🚨 Check if any faces were processed
if len(known_encodings) == 0:
    print("\n❌ No faces found in dataset. Check your images.")
    exit()

# 🧠 Save model with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_filename = f"face_recognizer_{timestamp}.pkl"

with open(model_filename, "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("\n🎉 Training completed successfully!")
print(f"📁 Model saved as: {model_filename}")