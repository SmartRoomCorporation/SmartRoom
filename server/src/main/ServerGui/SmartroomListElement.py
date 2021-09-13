from tkinter import *   # from x import * is bad practice
from ServerGui.StatusCircle import StatusCircle
from PIL import Image, ImageTk


class SmartroomListElement(LabelFrame):
    sc = ""
    smartroom = ""
    set_icon = ""
    set_img = Image.open("ServerGui/setting.png")
    set_img = set_img.resize((20, 20))

    def __init__(self, parent, origin, key, *args, **kw):
        super().__init__(master = parent,  *args, **kw)
        self.parent = parent
        self.origin = origin
        self.smartroom = key

        self.set_icon = ImageTk.PhotoImage(self.set_img)

        smart_frame = Frame(self, bg = self["bg"])
        smart_frame.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

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
        self.origin.window.server.retriveSensorList(self.smartroom)
        self.origin.roomCard(self.smartroom)
