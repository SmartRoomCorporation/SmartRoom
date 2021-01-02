from tkinter import *
from tkinter.ttk import *

class StatusCircle(Canvas):
    parent = ""
    circle = ""
    status = False

    def __init__(self, parent, *args, **kw):
        Canvas.__init__(self, parent, *args, **kw)
        self.circle = self.createCircle(20, 20, 5)
        self.itemconfig(self.circle, fill = 'red')

    def change(self, val=None):
        if(val is None):
            
            if self.status is True:
                self.itemconfig(self.circle, fill = 'red')
                self.status = False
            else:
                self.itemconfig(self.circle, fill = 'lime')
                self.status = True
        else: 
            if val is True:
                self.itemconfig(self.circle, fill = 'lime')
                self.status = True
            else:
                self.itemconfig(self.circle, fill = 'red')
                self.status = False

    
    def createCircle(self, x, y, r): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.create_oval(x0, y0, x1, y1)
