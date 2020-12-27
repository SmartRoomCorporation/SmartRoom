import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import os,sys,inspect
from pprint import pprint
from .FaceRecon import FaceRecon

class Camera:

    video_capture = None
    waitingCameraFrame = ""
    waitingCameraFrameSingle = ""
    cameraBusy = True
    fr = ""
    fullScreen = False

    def initCamera(self):
        self.waitingCameraFrame = self.waitingCameraFrameInit()
        self.waitingCameraFrameSingle = self.waitingCameraFrameSingleInit()
        self.fr = FaceRecon()
        self.displayWaiting()

    def checkCamera(self):
        if(self.video_capture == None): return False
        return not self.video_capture is None and self.video_capture.isOpened()

    def checkCameraIsBusy(self):
        if(self.video_capture == None): return False
        return not self.video_capture.grab()

    def getResDir(self):
        current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parent_dir = os.path.dirname(current_dir)
        dirname = os.path.dirname(parent_dir)
        return str(dirname)

    def closeCamera(self):
        self.video_capture.release()
        self.video_capture = None
        self.displayWaiting()

    def openCamera(self):
        self.video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def getCameraCurrentFrame(self):
        if(not self.checkCamera() or self.checkCameraIsBusy()): return None
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
        access = False
        if(frame is None): return None
        else: access, frame = self.fr.processFrame(frame, True)
        cv2.imshow('FaceRecon', frame)

    def waitingCameraFrameInit(self):
        loader=Image.open(self.getResDir()+"/res/assets/general/loading.png")
        loader = ImageTk.PhotoImage(loader)
        return loader

    def waitingCameraFrameSingleInit(self):
        return cv2.imread(self.getResDir()+"/res/assets/general/loading.png")

    def setFullScreen(self):
        cv2.destroyAllWindows()
        if(self.fullScreen):
            cv2.namedWindow('FaceRecon', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('FaceRecon', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        else:
            cv2.namedWindow('FaceRecon', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('FaceRecon', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        self.displayWaiting()
        self.fullScreen = not self.fullScreen

    def setFullScreenDblClick(self, event, x, y, flags, param):
        if(event == cv2.EVENT_LBUTTONDBLCLK):
            self.setFullScreen()

    def displayWaiting(self):
        cv2.imshow('FaceRecon', self.waitingCameraFrameSingle)
        cv2.setMouseCallback('FaceRecon', self.setFullScreenDblClick)