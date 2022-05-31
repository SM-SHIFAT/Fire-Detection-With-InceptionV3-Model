# Import essential libraries
import imutils
import numpy as np
import requests
import cv2

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
from cv2 import imdecode, imshow, waitKey, destroyAllWindows

url = "http://192.168.0.112:8080/shot.jpg"

# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    imshow("Android_cam", img)

    # Press Esc key to exit
    if waitKey(1) == 27:
        break

destroyAllWindows()