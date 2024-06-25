import cv2
import easyocr
import time

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create an EasyOCR reader object
reader = easyocr.Reader(['en'])

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured
    if ret:
        # Use EasyOCR to recognize text in the captured frame
        results = reader.readtext(frame, detail=0, allowlist='12345678')
        print(results)

        # Display the captured frame
        # cv2.imshow('Real-time Image', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # cv2.waitKey(1)  # Display the window for a short time

        # Wait for 10 seconds before capturing the next frame
        # time.sleep(10)
    else:
        print("Failed to capture image")
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()