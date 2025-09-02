# Models\Crowd_Detection\crowd.py

from ultralytics import YOLO
import cv2
import cvzone

# Load the YOLO model only once globally (outside the function)
crowd_model = YOLO("Models/Crowd_Detection/yolov8m.pt")


def detect(frame):
    """
    Detects people in a given frame using YOLOv8 and returns the processed frame and count.

    Args:
        frame (np.ndarray): Input frame from video or webcam.

    Returns:
        frame (np.ndarray): Output frame with boxes and count overlay.
        count (int): Number of people detected.
    """

    # Run inference on the frame
    results = crowd_model(frame)

    # Extract person bounding boxes
    person_boxes = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls = int(box.cls[0])
        if cls == 0:  # Class 0 is 'person'
            person_boxes.append((x1, y1, x2, y2))
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Optional: center points (currently unused)
    detect = [(int((x1 + x2)/2), int((y1 + y2)/2))
              for (x1, y1, x2, y2) in person_boxes]

    # Display total people count
    cvzone.putTextRect(frame, f"Total People: {len(person_boxes)}", (0, 30), scale=1,
                       thickness=1, colorR=(0, 0, 255), colorT=(0, 0, 0))

    return frame, len(person_boxes)
