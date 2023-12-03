import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsv_color[0][0][0] - 0, 100, 100
    upperLimit = hsv_color[0][0][0] + 0, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit