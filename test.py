import imutils
import requests
import cv2
import numpy as np
#from PIL import Image
#import tensorflow as tf
#from keras.preprocessing import image
from cv2 import imdecode, imshow, waitKey, destroyAllWindows

url = "http://192.168.0.112:8080/shot.jpg"
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    print(img_arr)
    img = imdecode(img_arr, -1)
    img = imutils.resize(img, width=224, height=224)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    imshow("Android_cam", img)
    #cv2.imshow("capture",img)

    # Press Esc key to exit
    if waitKey(1) == 27:
        break

destroyAllWindows()
