import cv2
import easyocr
import matplotlib.pyplot as plt

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture a single frame
ret, frame = cap.read()

# Check if the frame was captured successfully
if ret:
    # Save the captured image
    cv2.imwrite('D:/electronicDesign/sendMedicine/captured_image.png', frame)

    # Create an EasyOCR reader object
    reader = easyocr.Reader(['en'])

    # Use EasyOCR to recognize text in the captured image
    results = reader.readtext(frame, detail=0, allowlist='12345678')

    print(results)

    # Display the captured image
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print("Failed to capture image")

# Release the camera
cap.release()