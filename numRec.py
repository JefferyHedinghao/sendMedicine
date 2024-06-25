import easyocr
import cv2
import matplotlib.pyplot as plt

# create a reader object
reader = easyocr.Reader(['en'])

# read the image
image = cv2.imread('D:/electronicDesign/sendMedicine/2.png')

# easyocr recognize
results = reader.readtext(image, detail = 0, allowlist='12345678')

print(results)

# show the image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()