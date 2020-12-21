import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk
from FaceRecon import FaceRecon

class Camera:

    video_capture = ""
    fr = FaceRecon()

    def initCamera(self):
        self.video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def getCameraCurrentFrame(self):
        ret, frame = self.video_capture.read()
        return frame

    def getCameraSimpleStream(self): # simple stream from camera for GUI
        frame = self.getCameraCurrentFrame()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(img)
        return imgtk

    def showFaceRecon(self): # show the GUI for FaceRecognition module
        frame = self.getCameraCurrentFrame()
        cv2.imshow('Video', frame)