import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import os,sys,inspect
from pprint import pprint
#from FaceRecon import FaceRecon

class Camera:

    video_capture = ""
    waitingCameraFrame = ""
    waitingCameraFrameSingle = ""
    #fr = FaceRecon()

    def initCamera(self):
        self.video_capture = cv2.VideoCapture(0)
        self.waitingCameraFrame = self.waitingCameraFrameInit()
        self.waitingCameraFrameSingle = self.waitingCameraFrameSingleInit()

    def checkCamera(self):
        return self.video_capture.isOpened()

    def getResDir(self):
        current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parent_dir = os.path.dirname(current_dir)
        dirname = os.path.dirname(parent_dir)
        return str(dirname)

    def closeCamera(self):
        self.video_capture.release()

    def getCameraCurrentFrame(self):
        ret, frame = self.video_capture.read()
        return frame

    def getCameraSimpleStream(self): # simple stream from camera for GUI
        frame = self.getCameraCurrentFrame()
        if(frame is None):
            return self.waitingCameraFrame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(img)
        return imgtk

    def showFaceRecon(self): # show the GUI for FaceRecognition module
        frame = self.getCameraCurrentFrame()
        if(frame is None): frame = self.waitingCameraFrameSingle
        cv2.imshow('Video', frame)

    def waitingCameraFrameInit(self):
        loader=Image.open(self.getResDir()+"/res/assets/general/loading.png")
        loader = ImageTk.PhotoImage(loader)
        return loader

    def waitingCameraFrameSingleInit(self):
        return cv2.imread(self.getResDir()+"/res/assets/general/loading.png")