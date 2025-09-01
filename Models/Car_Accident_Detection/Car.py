import numpy as np
import cv2
import cvzone
from ultralytics import YOLO

# Load YOLO model
model = YOLO(r"Models/Car_Accident_Detection/best.pt")

# Load class labels
with open(r"Models/Car_Accident_Detection/coco.txt", "r") as f:
    classes = f.read().split("\n")


def detect(frame):
    results = model.predict(frame, conf=0.5, iou=0.3, verbose=False)
    


    for result in results:
        for re in result.boxes:
            x1, y1, x2, y2 = map(int, re.xyxy[0])
            if int(re.cls[0]) < len(classes):
                name = classes[int(re.cls[0])]

                # If class is "Accident Detection !" (your custom class name)
                if "Accident" in name:
                    # Highlight accident
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cvzone.putTextRect(frame, f"Accident Detected!", (x1 + 10, y1 - 10), scale=1,
                                       thickness=1, colorR=(0, 0, 255), colorT=(0, 0, 0))


    return frame
