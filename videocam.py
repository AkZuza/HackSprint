import cv2
import streamlit as st
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import threading

st.title("Webcam Live Feed")
run = st.checkbox('Run')
run = True
# am= st.radio("select mode",["Autonomous","Manual"])
FRAME_WINDOW = st.image([])

tsm = YOLO('traffic_sign.pt')
tsm.to('cuda')

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.frame_ready = False

    def start(self):
        threading.Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)
                if self.grabbed:
                    self.frame_ready = True

    def stop(self):
        self.stopped = True

    def is_frame_ready(self):
        return self.frame_ready
    
    def get_frame(self):
        self.frame_ready = False
        return self.frame

if run:
    getter = VideoGet().start()

def get_results(model, frame):
    if frame is not None:
        results = model.predict(source=frame, stream=True, device=1)
        for r in results:
            annotator = Annotator(frame)
            boxes = r.boxes
            detected.clear()
            for box in boxes:
                b = box.xyxy[0]
                c = box.cls
                annotator.box_label(b, model.names[int(c)])
        frame = annotator.result()
    


frame = None
img = None
detected = list()
model = tsm
while run:
    frame = getter.frame

    if frame is not None:
        results = model.predict(source=frame, stream=True, device=1)
        for r in results:
            annotator = Annotator(frame)
            boxes = r.boxes
            detected.clear()
            for box in boxes:
                b = box.xyxy[0]
                c = box.cls
                annotator.box_label(b, model.names[int(c)])
        img = annotator.result()

    # tst = threading.Thread(target=get_results, args=(tsm, framel))
    # yt = threading.Thread(target=get_results, args=(yolo, framel))

    # tst.start()
    # yt.start()
    # tst.join()
    # yt.join()

    if img is not None:
        FRAME_WINDOW.image(img, channels="BGR") 
        
    # if img is not None:
    #     cv2.imshow('Video', img)
        
else:
    st.write('Stopped')
    getter.stop()
