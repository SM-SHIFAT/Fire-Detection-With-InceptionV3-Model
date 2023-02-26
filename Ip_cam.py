import os
import shutil
import time
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
import datetime
import imutils
import numpy as np
import requests
from cv2 import imdecode, imshow, waitKey, destroyAllWindows
import emailsent

def fireAlert():
        print("fire")
        #emailsent.sentMail()
def moveImage(source_dir,dst):
        print("Image Moved")
        for f in os.listdir(source_dir):
                shutil.move("./output/" + f, dst)
                # os.remove(os.path.join(dire, f))

tempdate = datetime.datetime(2000, 5, 31, 9, 30)
url = "http://192.168.0.112:8080/shot.jpg"
#Load the saved model
#model = tf.keras.models.load_model('InceptionV3.h5')
#model = tf.keras.models.load_model('keras_model.h5')
model = tf.keras.models.load_model('Final_Model_9000.h5')
video = cv2.VideoCapture(0)
source_dir = "./output"
dst = "./newTrainingData"
count = 0
while True:
        #Frame Data
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = imdecode(img_arr, -1)

        # Convert the captured frame into RGB
        im = Image.fromarray(img, 'RGB')
        mailimage = image.img_to_array(im)

        # Resizing into 224x224 because we trained the model with this image size.
        im = im.resize((224, 224))
        img_array = image.img_to_array(im)
        img_array = np.expand_dims(img_array, axis=0) / 255


        probabilities = model.predict(img_array)[0]
        #Calling the predict method on model to predict 'fire' on the image
        prediction = np.argmax(probabilities)
        #if prediction is 0, which means there is fire in the frame.
        if prediction == 0:
                if probabilities[prediction]>0.85:
                        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

                        #print(probabilities[prediction])
                        count=count+1
                        print(count)
                        if count ==1:
                                tempdate = datetime.datetime.now()

                        if count%5 == 0:
                                now = datetime.datetime.now()
                                cv2.imwrite("./output/frame%d.jpg" % now.microsecond, mailimage)

                        if count == 2: ## 45 is the value
                                now = datetime.datetime.now()
                                if (now - tempdate).seconds < 60:
                                        cv2.imwrite("./output/frame%d.jpg" % now.microsecond, mailimage)
                                        fireAlert()
                                        moveImage(source_dir, dst)
                                        count = 0

                                else:
                                        count = 0
                                        moveImage(source_dir,dst)





        #cv2.imshow("Capturing", frame)
        imshow("Android_cam", img)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
video.release()
cv2.destroyAllWindows()