import cv2
import threading
from ultralytics import YOLO

model = YOLO('best.pt')
model.conf = 0.25

def capture_and_detect():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Perform object detection
        results = model.predict(source=frame, show=True)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

thread = threading.Thread(target=capture_and_detect)
thread.start()
thread.join()