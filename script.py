import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
import datetime

def fireAlert():
        print("fire")

tempdate = datetime.datetime(2000, 5, 31, 9, 30)

#Load the saved model
#model = tf.keras.models.load_model('InceptionV3.h5')
#model = tf.keras.models.load_model('keras_model.h5')
model = tf.keras.models.load_model('Final_Model_9000.h5')
video = cv2.VideoCapture(0)
count = 0
while True:
        _, frame = video.read()
#Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')
#Resizing into 224x224 because we trained the model with this image size.
        im = im.resize((224,224))
        img_array = image.img_to_array(im)
        img_array = np.expand_dims(img_array, axis=0) / 255

        probabilities = model.predict(img_array)[0]
        #Calling the predict method on model to predict 'fire' on the image
        prediction = np.argmax(probabilities)
        #if prediction is 0, which means there is fire in the frame.
        if prediction == 0:
                if probabilities[prediction]>0.85:
                        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                        #print(probabilities[prediction])
                        count=count+1
                        print(count)
                        if count ==1:
                                tempdate = datetime.datetime.now()
                        if count == 50:
                                now = datetime.datetime.now()
                                if (now - tempdate).seconds < 60:
                                        fireAlert()
                                        count = 0
                                else:
                                        count = 0



        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
video.release()
cv2.destroyAllWindows()