# why aint it importing :(
import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture()
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while run:

    success, img = camera.read()
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(imgGray, 1.3, 6)

    # drawing bounding box around face
    # for (x, y, w, h) in faces:
    #     img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
    # if  0xFF == ord('q'):
    #     break
    
    FRAME_WINDOW.image(img)
else:
    st.write('Stopped')