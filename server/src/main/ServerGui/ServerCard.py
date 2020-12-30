from tkinter import *
import tkinter as tk
from VerticalScrolledFrame import VerticalScrolledFrame
from SmartroomListElement import SmartroomListElement


class ServerCard(tk.Frame):

    window = ""
    array = ["SmartRoom 0", "SmartRoom 1", "SmartRoom 2","SmartRoom 3", "SmartRoom 4", "SmartRoom 5","SmartRoom 6", "SmartRoom 7", "SmartRoom 8"]
    smartrooms = ""
    def __init__(self, window,  *args, **kw):
        tk.Frame.__init__(self, window, *args, **kw)

    def initCard(self):
        label = tk.Label(text = "SmartRooms:", fg = "blue", bg = self["bg"])
        self.frame = VerticalScrolledFrame(self, labelwidget = label, bg = self["bg"])
        self.frame.pack(expand=1, fill = BOTH)

        for name in self.array:
            smart_frame = SmartroomListElement(self.frame.interior, self, name, bg = self["bg"], relief = "raised", bd=1)
            smart_frame.pack(padx = 2, pady = 2, fill = X)

    def refreshSmartrooms(self):
        self.frame.destroy()
        self.initCard()

    def roomCard(self):
        self.frame.destroy()
        self.frame = tk.Frame(self, bg = self["bg"])
        self.frame.pack()
        b = tk.Button(self.frame, text = "Back", command = self.refreshSmartrooms)
        b.pack()

    def setSmartrooms(self, smartrooms):
        self.smartrooms = smartrooms
