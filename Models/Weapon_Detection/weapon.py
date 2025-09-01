import cv2
import numpy as np

# Load YOLOv3 model for weapon detection
weapon_net = cv2.dnn.readNet(
    "Models/Weapon_Detection/yolov3_training_2000.weights",
    "Models/Weapon_Detection/yolov3_testing.cfg"
)

# Set preferable backend and target (OpenCV optimization)
weapon_net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
weapon_net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

weapon_classes = ["Weapon"]
weapon_output_layers = weapon_net.getUnconnectedOutLayersNames()
weapon_colors = np.random.uniform(0, 255, size=(len(weapon_classes), 3))


def detect(frame):
    height, width = frame.shape[:2]

    # resize frame to speed up detection (you can adjust scale)
    input_frame = cv2.resize(frame, (416, 416))

    # Convert image to blob format
    blob = cv2.dnn.blobFromImage(input_frame, scalefactor=1/255.0, size=(416, 416),
                                 mean=(0, 0, 0), swapRB=True, crop=False)

    weapon_net.setInput(blob)
    outs = weapon_net.forward(weapon_output_layers)

    class_ids = []
    confidences = []
    boxes = []

    # Parse detections
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                # Scale back to original frame size
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Max Suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw boxes and labels
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(weapon_classes[class_ids[i]])
            color = (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame
