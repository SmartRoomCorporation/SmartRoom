import tkinter as tk
from PIL import Image, ImageTk
from ServerCard import ServerCard
from pprint import pprint
from StatusCircle import StatusCircle
from ServerConfig import ServerConfig

class ServerGui:
    window = tk.Tk()
    window.geometry("600x600")
    window.title("SmartRooms Control Server")
    set_icon = None
    
    def __init__(self):
        set_img = Image.open("setting.png")
        set_img = set_img.resize((20, 20))
        self.set_icon = ImageTk.PhotoImage(set_img)

    def run(self):
        self.initGui()
        self.window.mainloop()


    def initGui(self):
        self.statusFrame = tk.LabelFrame(self.window, text = "Server Status:", fg="blue")
        self.statusFrame.pack(fill = tk.BOTH)

        lab = tk.Label(self.statusFrame, text = "Connection status:")
        lab.grid(column = 0, row = 0, padx = 5, pady = 5)

        sc = StatusCircle(self.statusFrame, height = 50, width = 50)
        sc.grid(column = 2, row = 0, padx = 5, pady = 5)

        lab1 = tk.Label(self.statusFrame, text = "IP:")
        lab1.grid(column = 0, row = 2, padx= 5, pady = 5, sticky = tk.W)
        lab2 = tk.Label(self.statusFrame, text = "Port:")

        lab2.grid(column = 1, row = 2, padx = 5, pady = 5)
        self.statusFrame.grid_columnconfigure(3, weight=1)

        configButton = tk.Button(self.statusFrame, image = self.set_icon, command = self.configWindow)
        configButton.grid(column = 3, row = 0, padx = 5, pady = 5, sticky = tk.E)

        statusCard = ServerCard(self.window)
        statusCard.pack(expand=1, fill = tk.BOTH)

        statusCard.initCard()

    def configWindow(self):
        ServerConfig(master = self.window)
        self.window.wm_attributes("-disabled", True)
