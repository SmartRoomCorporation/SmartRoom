from tkinter import *
import tkinter as tk

class ServerConfig(tk.Toplevel):

    def __init__(self, master = None):
        self.master = master
        super().__init__(master = master)
        self.geometry("200x300")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        ip_frame = tk.LabelFrame(self, text = "IP:", fg = "blue")
        ip_frame.pack(fill = tk.X)
        lab = tk.Label(ip_frame, text = "Current IP:")
        lab.grid(column = 0, columnspan = 1, row = 0, padx = 5, pady = 5, sticky = tk.W)
        ip_frame.grid_columnconfigure(0, weight=0)
        cur_ip = tk.Label(ip_frame, text = "192.168.0.111")
        cur_ip.grid(column = 1, columnspan = 1, row = 0, padx = 5, pady = 5)
        ip_text = tk.Text(ip_frame, height=1, width=20)
        ip_text.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = tk.W)

    def onClose(self):
        self.master.wm_attributes("-disabled", False)
        self.destroy()
