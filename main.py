import cv2
from utils import get_limits
from PIL import Image

color = [0, 255, 255] # yellow in BGR color space

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # change the size of the frame
    frame = cv2.resize(frame, (0, 0), fx=0.8, fy=0.801)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get the limits for the color
    lowerLimit, upperLimit = get_limits(color)

    # Create a mask for the color
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    print(bbox)
    # Display the resulting frame
    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


