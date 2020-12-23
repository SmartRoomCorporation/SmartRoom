import tkinter as tk
from PIL import Image, ImageTk
from ServerStatusCard import ServerStatusCard
from pprint import pprint

class ServerGui:
    window = tk.Tk()
    window.geometry("600x600")
    window.title("SmartRooms Control Server")

    def run(self):
        self.initGui()
        self.window.mainloop()

    def initGui(self):
        statusCard = ServerStatusCard(self.window)
        statusCard.pack(expand=1, fill = tk.BOTH)
        statusCard.initCard()
