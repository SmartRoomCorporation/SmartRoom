from tkinter import *   # from x import * is bad practice
from StatusCircle import StatusCircle
from PIL import Image, ImageTk


class SmartroomListElement(Frame):
    sc = ""
    smartroom = ""

    def __init__(self, parent, origin, smartroom, *args, **kw):
        super().__init__(master = parent,  *args, **kw)
        self.parent = parent
        self.origin = origin
        self.smartroom = smartroom

        set_img = Image.open("setting.png")
        set_img = set_img.resize((20, 20))
        self.set_icon = ImageTk.PhotoImage(set_img)

        smart_frame = Frame(self, bg = self["bg"])
        smart_frame.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

        label1 = Label(smart_frame, text="Room:", bg = self["bg"])
        label1.pack(side = LEFT, padx = 5, pady = 5)
        label = Label(smart_frame, text = smartroom, bg = self["bg"])
        label.pack(padx = 5, pady = 5)

        conn_frame = Frame(self, bg = self["bg"])
        conn_frame.grid(row = 0, column = 1, padx = 5, pady = 5)
        label2 = Label(conn_frame, text="Connection status: ", bg = self["bg"])
        label2.pack(padx = 10, pady = 5, side = LEFT)
        self.sc = StatusCircle(conn_frame, height = 30, width = 30, bg = self["bg"])
        self.sc.pack(padx = 5, pady = 5)

        self.grid_columnconfigure(2, weight=1)
        settingButton = Button(self, image = self.set_icon, command = self.showSmartRoom, bg = self["bg"])
        settingButton.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = E)

    def changeStatus(self):
        self.sc.change();

    def showSmartRoom(self):
        self.origin.roomCard()
