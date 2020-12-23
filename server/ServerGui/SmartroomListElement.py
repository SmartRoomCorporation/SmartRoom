from tkinter import *   # from x import * is bad practice
from tkinter.ttk import *
from StatusCircle import StatusCircle
from PIL import Image, ImageTk
import ServerStatusCard


class SmartroomListElement(Frame):
    sc = ""
    smartroom = ""

    def __init__(self, parent, origin, smartroom, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        self.parent = parent
        self.origin = origin
        self.smartroom = smartroom

        set_img = Image.open("setting.png")
        set_img = set_img.resize((20, 20))
        self.set_icon = ImageTk.PhotoImage(set_img)

        self.grid_columnconfigure(4, weight=1)
        label1 = Label(self, text="Room:", font = ("Calibri", 13))
        label1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
        label = Label(self, text = smartroom, font = ("Calibri", 12))
        label.grid(row = 0, column = 1, padx = 20, pady = 5)

        label2 = Label(self, text="Connection status: ", font = ("Calibri", 13))
        label2.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
        self.sc = StatusCircle(self, height = 50, width = 50)
        self.sc.grid(row = 0, column = 3, padx = 5, pady = 5)

        settingButton = Button(self, image = self.set_icon, command = self.showSmartRoom)
        settingButton.grid(row = 0, column = 4, padx = 5, pady = 5, sticky = E)

    def changeStatus(self):
        self.sc.change();

    def showSmartRoom(self):
        self.origin.roomCard()
