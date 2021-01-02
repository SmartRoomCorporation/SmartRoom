import tkinter as tk
from PIL import Image, ImageTk
from ServerGui.ServerCard import ServerCard
from pprint import pprint
from ServerGui.StatusCircle import StatusCircle
from ServerGui.ServerConfig import ServerConfig

class ServerGui(tk.Tk):

    set_icon = None
    server = ""
    curr_ip = "1.1.1.1"
    curr_port = "0000"
    curr_ttl = "60"
    statusCard = ""

    def __init__(self, server):
        super().__init__()
        self.server = server
        self.curr_ip = server.getIp()
        self.curr_port = server.getPort()
        self.curr_ttl = server.getTtl()
        self.config(relief = "sunken", bd = 2)
        self.geometry("")
        self.minsize(500, 500)
        self.title("SmartRooms Control Utility")

    def run(self):
        #set_img = Image.open("ServerGui/setting.png")
        #set_img = set_img.resize((20, 20))
        #self.set_icon = ImageTk.PhotoImage(set_img)
        self.initGui()
        self.refreshInterface()
        self.refreshSensors()
        self.mainloop()


    def initGui(self):

        self.statusFrame = tk.LabelFrame(self, text = "Server Status:", fg="blue", bg = self["bg"], relief = "raised", bd=1)
        self.statusFrame.pack(fill = tk.BOTH, padx = 10, pady = 10)

#        frame_cs = tk.Frame(self.statusFrame, bg = self["bg"])
#        frame_cs.grid(row = 0, column = 0)
#        lab = tk.Label(frame_cs, text = "Connection status:", bg = self["bg"])
#        lab.pack(side = tk.LEFT,  padx= 5, pady = 5)
#        sc = StatusCircle(frame_cs, height = 50, width = 50, bg = self["bg"])
#        sc.pack(side = tk.LEFT,  padx= 5, pady = 5)

        frame_ip = tk.Frame(self.statusFrame, bg = self["bg"])
        frame_ip.grid(row = 0, column = 0)
        lab1 = tk.Label(frame_ip, text = "IP:", bg = self["bg"])
        lab1.pack(side = tk.LEFT,  padx= 5, pady = 5)
        text1 = tk.StringVar(frame_ip, self.curr_ip)
        ip_lab = tk.Label(frame_ip, textvariable = text1, bg = self["bg"])
        ip_lab.pack(side = tk.LEFT,  padx= 5, pady = 5)

        frame_port = tk.Frame(self.statusFrame, bg = self["bg"])
        frame_port.grid(row = 0, column = 1)
        lab2 = tk.Label(frame_port, text = "Port:", bg = self["bg"])
        lab2.pack(side = tk.LEFT,  padx= 5, pady = 5)
        text2 = tk.StringVar(frame_port, self.curr_port)
        port_lab = tk.Label(frame_port, textvariable = text2, bg = self["bg"])
        port_lab.pack(side = tk.LEFT,  padx= 5, pady = 5)

        self.statusFrame.grid_columnconfigure(2, weight=1)
        self.initSmartRoomsList()
        #configButton = tk.Button(self.statusFrame, image = self.set_icon, command = self.configWindow, bg = self["bg"])
        #configButton.grid(row = 0, column = 3, sticky = "se",  padx= 5, pady = 5)

    def initSmartRoomsList(self):
        self.statusCard = ServerCard(self, self.server.getSmartRooms())
        self.statusCard.config(bg = self["bg"])
        self.statusCard.pack(expand=1, fill = tk.BOTH, padx = 10, pady = 10)
        self.statusCard.initCard()

    def configWindow(self):
        config_window = ServerConfig(master = self)
        config_window.fillWindow(self.curr_ip, self.curr_port, self.curr_ttl)
        self.wm_attributes("-topmost", False)

    def refreshInterface(self):
        self.statusCard.refreshSmartrooms()
        self.after(1000, self.refreshInterface)

    def refreshSensors(self):
        self.statusCard.refreshRoomSensor()
        self.after(3000, self.refreshSensors)
