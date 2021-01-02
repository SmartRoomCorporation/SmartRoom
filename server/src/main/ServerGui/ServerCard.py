from tkinter import *
import tkinter as tk
from ServerGui.VerticalScrolledFrame import VerticalScrolledFrame
from ServerGui.SmartroomListElement import SmartroomListElement
import json

class ServerCard(tk.Frame):

    window = ""
    smartrooms = ""
    smartroom = ""
    smartroomframes = dict()
    frame = ""
    back_button = ""
    showroom = False
    SENSORSSTATUS = "SENSORSSTATUS"

    def __init__(self, window, smartrooms,  *args, **kw):
        tk.Frame.__init__(self, window, *args, **kw)
        self.window = window
        self.smartrooms = smartrooms

    def initCard(self):
        label = tk.Label(text = "SmartRooms:", fg = "blue", bg = self["bg"])
        self.frame = VerticalScrolledFrame(self, labelwidget = label, bg = self["bg"], relief = "raised", bd=1)
        self.frame.pack(expand=1, fill = BOTH)

    def refreshSmartrooms(self):
        for key, smartroom in self.smartrooms.items():
            if key not in self.smartroomframes:
                label = tk.Label(text = key, fg = "blue")
                smart_frame = SmartroomListElement(self.frame.interior, self, smartroom,labelwidget = label, bg = self["bg"], relief = "sunken", bd=1)
                smart_frame.pack(padx = 2, pady = 2, fill = X)
                self.smartroomframes[key] = smart_frame


    def roomCard(self, smartroom):
        self.smartroom = smartroom
        self.frame.destroy()
        label = tk.Label(text = smartroom.getMacAddress(), fg = "blue", bg = self["bg"])
        self.frame = VerticalScrolledFrame(self, labelwidget = label, bg = self["bg"], relief = "raised", bd=1)
        self.frame.pack(expand=1, fill = BOTH)
        self.showroom = True
        self.smartroom.setActive(True)
        for key, value in smartroom.getSensorsList().items():
            value.setGui(True)
            value.createTempGui(self.frame.interior)

        self.back_button = tk.Button(self.window, text = "Back", command = self.resumeSmartroomsList)
        self.back_button.pack()

    def resumeSmartroomsList(self):
        for key, value in self.smartroom.getSensorsList().items():
            value.setGui(False)
        self.showroom = False
        self.smartroom.setActive(False)
        self.frame.destroy()
        self.back_button.destroy()
        self.initCard()
        for key, smartroom in self.smartrooms.items():
            label = tk.Label(text = key, fg = "blue")
            smart_frame = SmartroomListElement(self.frame.interior, self, smartroom,labelwidget = label, bg = self["bg"], relief = "sunken", bd=1)
            smart_frame.pack(padx = 2, pady = 2, fill = X)
            self.smartroomframes[key] = smart_frame

    def refreshRoomSensor(self):
        if self.showroom:
            for key, value in self.smartrooms.items():
                if(value.getActive()):
                    value.getServerInstance().getServer().publish(value.getMacAddress(), json.dumps(self.SENSORSSTATUS), qos=0, retain=False)
