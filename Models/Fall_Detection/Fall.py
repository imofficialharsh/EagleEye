import cv2
import cvzone
import math
from ultralytics import YOLO

# Load model once globally
fall_model = YOLO('Models/Fall_Detection/yolov8s.pt')

# Load class names once
with open('Models/Fall_Detection/classes.txt', 'r') as f:
    classnames = f.read().splitlines()


def detect(frame):
    """
    Detects falls from a given frame using YOLOv8.

    Args:
        frame (np.ndarray): Frame to process.

    Returns:
        frame (np.ndarray): Frame with visual annotations.
        fall_detected (bool): True if a fall is detected, False otherwise.
    """
    fall_detected = False
    frame = cv2.resize(frame, (980, 740))

    results = fall_model(frame)

    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            class_idx = int(box.cls[0])
            class_name = classnames[class_idx]
            conf_percent = math.ceil(confidence * 100)

            height = y2 - y1
            width = x2 - x1
            threshold = height - width

            # Draw detection for person
            if conf_percent > 80 and class_name == 'person':
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cvzone.putTextRect(frame, f'{class_name}', (x1 + 10, y1 - 10), scale=1, thickness=1,
                                   colorR=(0, 255, 0), colorT=(0, 0, 0))

            # Fall detected condition
            if threshold < 0:
                fall_detected = True
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cvzone.putTextRect(frame, f"Fall Detected!", (x1 + 10, y1 - 10), scale=1, thickness=1,
                                   colorR=(0, 0, 255), colorT=(0, 0, 0))

    return frame, fall_detected
