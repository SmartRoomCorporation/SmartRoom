import tkinter as tk
from PIL import Image, ImageTk
from ServerCard import ServerCard
from pprint import pprint
from StatusCircle import StatusCircle
from ServerConfig import ServerConfig

class ServerGui(tk.Tk):

    set_icon = None
    curr_ip = "1.1.1.1"
    curr_port = "0000"

    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.minsize(520, 600)
        self.title("SmartRooms Control Utility")


    def run(self):
        set_img = Image.open("setting.png")
        set_img = set_img.resize((20, 20))
        self.set_icon = ImageTk.PhotoImage(set_img)
        self.initGui()
        self.mainloop()


    def initGui(self):

        self.statusFrame = tk.LabelFrame(self, text = "Server Status:", fg="blue")
        self.statusFrame.pack(fill = tk.BOTH, padx = 10, pady = 10)

        frame_cs = tk.Frame(self.statusFrame)
        frame_cs.grid(row = 0, column = 0)
        lab = tk.Label(frame_cs, text = "Connection status:")
        lab.pack(side = tk.LEFT,  padx= 5, pady = 5)
        sc = StatusCircle(frame_cs, height = 50, width = 50)
        sc.pack(side = tk.LEFT,  padx= 5, pady = 5)

        frame_ip = tk.Frame(self.statusFrame)
        frame_ip.grid(row = 0, column = 1)
        lab1 = tk.Label(frame_ip, text = "IP:")
        lab1.pack(side = tk.LEFT,  padx= 5, pady = 5)
        text1 = tk.StringVar(frame_ip, self.curr_ip)
        ip_lab = tk.Label(frame_ip, textvariable = text1)
        ip_lab.pack(side = tk.LEFT,  padx= 5, pady = 5)

        frame_port = tk.Frame(self.statusFrame)
        frame_port.grid(row = 0, column = 2)
        lab2 = tk.Label(frame_port, text = "Port:")
        lab2.pack(side = tk.LEFT,  padx= 5, pady = 5)
        text2 = tk.StringVar(frame_port, self.curr_port)
        port_lab = tk.Label(frame_port, textvariable = text2)
        port_lab.pack(side = tk.LEFT,  padx= 5, pady = 5)

        self.statusFrame.grid_columnconfigure(3, weight=1)

        configButton = tk.Button(self.statusFrame, image = self.set_icon, command = self.configWindow)
        configButton.grid(row = 0, column = 3, sticky = "se",  padx= 5, pady = 5)

        self.statusCard = ServerCard(self)
        self.statusCard.pack(expand=1, fill = tk.BOTH, padx = 10, pady = 10)

        self.statusCard.initCard()

    def configWindow(self):
        config_window = ServerConfig(master = self)
        config_window.fillWindow(self.curr_ip, self.curr_port)
        self.wm_attributes("-topmost", False)

    def refreshInterface(self):
        self.statusFrame.destroy()
        self.statusCard.destroy()
        self.initGui()
