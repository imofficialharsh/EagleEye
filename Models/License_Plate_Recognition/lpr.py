# Models\License_Plate_Recognition\lpr.py

import cv2
import os
import cvzone
import numpy as np
import easyocr
from ultralytics import YOLO
from datetime import datetime


# Load LPR Model
lpr_model = YOLO(r"Models/License_Plate_Recognition/best.pt")

# Initialize OCR
reader = easyocr.Reader(['en'])


def detect(frame):
    """
    Detects license plates in the frame and draws OCR results.
    """
    # Initialize the set here, once per frame
    seen_plates = set()
    
    results = lpr_model.predict(frame, conf=0.5, iou=0.3, verbose=False)

    for result in results:
        for re in result.boxes:
            x1, y1, x2, y2 = map(int, re.xyxy[0])

            # Draw bounding box around license plate
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Extract license plate region
            plate_roi = frame[y1:y2, x1:x2]

            # OCR on the extracted plate
            ocr_result = reader.readtext(plate_roi)
            
            # The set should NOT be initialized here
            # seen_plates = set()

            # Display top result if available
            if ocr_result:
                text = ocr_result[0][1]
                cvzone.putTextRect(frame, f"Plate", (x1, y2 + 30), scale=1,
                                   thickness=1, colorR=(255, 0, 0), colorT=(0, 0, 0))
                
                if text not in seen_plates:
                    seen_plates.add(text)
                    # Ensure the Output/LPR directory exists
                    if not os.path.exists("./Output/LPR"):
                        os.makedirs("./Output/LPR")
                    with open("./Output/LPR/detected_plates.csv", "a") as f:
                        f.write(f"{text}, {datetime.now()}\n")
    return frame