from tkinter import *
import tkinter as tk

class ServerConfig(tk.Toplevel):

    curr_ip = "0.0.0.0"
    curr_port = "0000"

    def __init__(self, master = None):
        self.master = master
        super().__init__(master = master)
        self.geometry("390x190")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.title("Connection Setting")


    def fillWindow(self, curr_ip, curr_port):
        self.curr_ip = curr_ip
        self.curr_port = curr_port
        ip_frame = tk.LabelFrame(self, text = "IP:", fg = "blue")
        ip_frame.grid(row = 0, sticky = "nsew", padx = 10, pady = 10)
        lab = tk.Label(ip_frame, text = "Current IP:")
        lab.pack(side = LEFT, padx = 5, pady = 5)

        cur_ip = tk.Label(ip_frame, textvariable = tk.StringVar(ip_frame, self.curr_ip))
        cur_ip.pack(side = LEFT, padx = 5, pady = 5)

        tk.Frame(ip_frame, width = 50).pack(side = LEFT)
        lab1 = tk.Label(ip_frame, text = "New IP:")
        lab1.pack(side = LEFT, padx = 5, pady = 5)

        self.ip_entry = tk.Entry(ip_frame, width=20)
        self.ip_entry.pack(side = LEFT, padx = 5, pady = 5)

        port_frame = tk.LabelFrame(self, text = "PORT:", fg = "blue")
        port_frame.grid(row = 1, sticky = "nsew", padx = 10, pady = 10)
        lab2 = tk.Label(port_frame, text = "Current PORT:")
        lab2.pack(side = LEFT, padx = 5, pady = 5)

        cur_port = tk.Label(port_frame, textvariable = tk.StringVar(port_frame, self.curr_port))
        cur_port.pack(side = LEFT, padx = 5, pady = 5)

        tk.Frame(port_frame, width = 75).pack(side = LEFT)
        lab3 = tk.Label(port_frame, text = "New PORT:")
        lab3.pack(side = LEFT, padx = 5, pady = 5)

        self.port_entry = tk.Entry(port_frame, width=10)
        self.port_entry.pack(side = LEFT, padx = 5, pady = 5)

        back_button = tk.Button(self, text = "Back", command = self.onClose)
        back_button.grid(row = 2, sticky = "sw", padx = 10, pady = 10)

        save_button = tk.Button(self, text = "Save", command = self.onSave)
        save_button.grid(row = 2, sticky = "se", padx = 10, pady = 10)


    def onClose(self):
        self.master.wm_attributes("-topmost", True)
        self.destroy()

    def onSave(self):
        self.master.refreshInterface()
        self.onClose()
