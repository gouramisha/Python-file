import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime

# Initialize LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load images and labels
path = 'ImagesAttendance'
images = []
labels = []
classNames = []
label_dict = {}

for idx, file in enumerate(os.listdir(path)):
    img = cv2.imread(os.path.join(path, file), 0)  # read in grayscale
    images.append(img)
    labels.append(idx)
    name = os.path.splitext(file)[0]
    classNames.append(name)
    label_dict[idx] = name

# Train recognizer
recognizer.train(images, np.array(labels))

# Initialize webcam
cap = cv2.VideoCapture(0)

# Attendance CSV
def markAttendance(name):
    filename = 'Attendance.csv'
    now = datetime.now()
    dtString = now.strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(filename):
        df = pd.DataFrame(columns=["Name", "Time"])
        df.to_csv(filename, index=False)

    df = pd.read_csv(filename)
    if name not in df["Name"].values:
        new_entry = {"Name": name, "Time": dtString}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(filename, index=False)
        print(f"Attendance marked for {name} at {dtString}")

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi_gray)
        if confidence < 70:  # threshold for recognition
            name = label_dict[label]
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            markAttendance(name)
        else:
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
