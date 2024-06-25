import cv2
import numpy as np

# black image
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Test Window')
cv2.imshow('Test Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()