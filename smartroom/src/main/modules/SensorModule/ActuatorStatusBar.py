import tkinter as tk


class ActuatorStatusBar(tk.Frame):

    MIN = 0
    MID = 1
    MAX = 2
    status = 0
    dim = 0

    def __init__(self, parent, dim = 10):
        super().__init__(master = parent)
        self.dim = dim
        self.createBar()

    def createBar(self):
        self.min_block = tk.Frame(self, width = self.dim, height = self.dim, bd = 1, bg = "red", relief = "solid")
        self.mid_block = tk.Frame(self, width = self.dim, height = self.dim, bd = 1, bg = "white", relief = "solid")
        self.max_block = tk.Frame(self, width = self.dim, height = self.dim, bd = 1, bg = "white", relief = "solid")
        self.min_block.pack(side = tk.LEFT)
        self.mid_block.pack(side = tk.LEFT)
        self.max_block.pack(side = tk.LEFT)

    def changeStatus(self, status):
        self.status=status
        if self.status == self.MIN :
            self.min_block.config(bg = "red")
            self.mid_block.config(bg = "white")
            self.max_block.config(bg = "white")
           
        elif self.status == self.MID :
            self.min_block.config(bg = "white")
            self.mid_block.config(bg = "orange")
            self.max_block.config(bg = "white")
            
        elif self.status == self.MAX :
            self.min_block.config(bg = "white")
            self.mid_block.config(bg = "white")
            self.max_block.config(bg = "green")
            
        else:
            self.status = 0
            self.min_block.config(bg = "white")
            self.mid_block.config(bg = "white")
            self.max_block.config(bg = "white")
