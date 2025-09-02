# Models\Face_detection\face.py

import cv2

# Load the DNN model
net = cv2.dnn.readNetFromCaffe(
    "Models/Face_detection/deploy.prototxt.txt",
    "Models/Face_detection/res10_300x300_ssd_iter_140000.caffemodel"
)


def detect(frame, conf_threshold=0.5):
    h, w = frame.shape[:2]

    # Create blob from image
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0, size=(300, 300),
                                 # Mean subtraction values for Caffe
                                 mean=(104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    # Loop over detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > conf_threshold:
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (x1, y1, x2, y2) = box.astype("int")

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # cv2.putText(frame, f"{confidence*100:.1f}%", (x1, y1 - 10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return frame
