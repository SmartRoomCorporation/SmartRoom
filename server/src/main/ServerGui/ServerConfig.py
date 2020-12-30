from tkinter import *
import tkinter as tk

class ServerConfig(tk.Toplevel):

    curr_ip = "0.0.0.0"
    curr_port = "0000"

    def __init__(self, master = None):
        self.master = master
        super().__init__(master = master, bg = master["bg"])
        self.geometry("")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.title("Connection Setting")


    def fillWindow(self, curr_ip, curr_port, curr_ttl):
        self.curr_ip = curr_ip
        self.curr_port = curr_port
        self.curr_ttl = curr_ttl

        ip_frame = tk.LabelFrame(self, text = "IP:", fg = "blue",  bg = self["bg"])
        ip_frame.grid(row = 0, sticky = "nsew", padx = 10, pady = 10)
        lab = tk.Label(ip_frame, text = "Current IP:", bg = self["bg"])
        lab.pack(side = LEFT, padx = 5, pady = 5)

        cur_ip = tk.Label(ip_frame, textvariable = tk.StringVar(ip_frame, self.curr_ip), bg = self["bg"])
        cur_ip.pack(side = LEFT, padx = 5, pady = 5)

        tk.Frame(ip_frame, width = 50, bg = self["bg"]).pack(side = LEFT)

        self.ip_entry = tk.Entry(ip_frame, width=20)
        self.ip_entry.pack(side = RIGHT, padx = 5, pady = 5)

        lab1 = tk.Label(ip_frame, text = "New IP:", bg = self["bg"])
        lab1.pack(side = RIGHT, padx = 5, pady = 5)

        port_frame = tk.LabelFrame(self, text = "PORT:", fg = "blue", bg = self["bg"])
        port_frame.grid(row = 1, sticky = "nsew", padx = 10, pady = 10)
        lab2 = tk.Label(port_frame, text = "Current PORT:", bg = self["bg"])
        lab2.pack(side = LEFT, padx = 5, pady = 5)

        cur_port = tk.Label(port_frame, textvariable = tk.StringVar(port_frame, self.curr_port), bg = self["bg"])
        cur_port.pack(side = LEFT, padx = 5, pady = 5)

        tk.Frame(port_frame, width = 75, bg = self["bg"]).pack(side = LEFT)

        self.port_entry = tk.Entry(port_frame, width=10)
        self.port_entry.pack(side = RIGHT, padx = 5, pady = 5)

        lab3 = tk.Label(port_frame, text = "New PORT:", bg = self["bg"])
        lab3.pack(side = RIGHT, padx = 5, pady = 5)

        ttl_frame = tk.LabelFrame(self, text = "TTL:", fg = "blue", bg = self["bg"])
        ttl_frame.grid(row = 2, sticky = "nsew", padx = 10, pady = 10)
        lab4 = tk.Label(ttl_frame, text = "Current TTL:", bg = self["bg"])
        lab4.pack(side = LEFT, padx = 5, pady = 5)

        cur_ttl = tk.Label(ttl_frame, textvariable = tk.StringVar(ttl_frame, self.curr_ttl), bg = self["bg"])
        cur_ttl.pack(side = LEFT, padx = 5, pady = 5)

        tk.Frame(ttl_frame, width = 75, bg = self["bg"]).pack(side = LEFT)

        self.ttl_entry = tk.Entry(ttl_frame, width=10)
        self.ttl_entry.pack(side = RIGHT, padx = 5, pady = 5)

        lab5 = tk.Label(ttl_frame, text = "New TTL:", bg = self["bg"])
        lab5.pack(side = RIGHT, padx = 5, pady = 5)

        back_button = tk.Button(self, text = "Back", command = self.onClose, bg = self["bg"])
        back_button.grid(row = 3, sticky = "sw", padx = 10, pady = 10)

        save_button = tk.Button(self, text = "Save", command = self.onSave, bg = self["bg"])
        save_button.grid(row = 3, sticky = "se", padx = 10, pady = 10)


    def onClose(self):
        self.master.wm_attributes("-topmost", True)
        self.destroy()

    def onSave(self):
        self.master.refreshInterface()
        self.onClose()
