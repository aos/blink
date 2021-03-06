import numpy as np
import cv2
import logging
import indicoio
from sys import platform as sys_pf
from dotenv import load_dotenv, find_dotenv
import os
import matplotlib.pyplot as plt
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

load_dotenv(find_dotenv())

# Indico API key
indicoio.config.api_key = os.getenv('API_KEY')

# import xml file
face_cascade = cv2.CascadeClassifier(
    './resources/haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier('./resources/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cv2.namedWindow("WD")

# figure for plot
fig = plt.gcf()
fig.show()
fig.canvas.draw()

emotions = ["Angry", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
result_matrix = np.zeros((1, len(emotions)))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Face detection
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Sentiment Image Analysis
        out = indicoio.fer(roi_gray)

        # append the result to the matrix
        result_matrix = np.vstack([result_matrix, [out[x] for x in emotions]])

        # logging
        logging.basicConfig(
            level=logging.DEBUG,
            filename="logfile.log",
            filemode="a+",
            format="%(asctime)-15s %(levelname)-8s %(message)s"
        )
        logging.info(out)

        # eye detection
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Plot data
        if ret:
            print(result_matrix)

            fig.clf()
            plt.plot(result_matrix)
            plt.legend(emotions, loc='upper left')
            fig.canvas.draw()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyWindow("WD")
