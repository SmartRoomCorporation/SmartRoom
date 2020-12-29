from tkinter import *
from tkinter.ttk import *

class StatusCircle(Canvas):
    parent = ""
    circle = ""
    status = False

    def __init__(self, parent, *args, **kw):
        Canvas.__init__(self, parent, *args, **kw)
        self.circle = self.create_oval(20,20,35,35, width=2, fill = 'red')

    def change(self):
        if self.status is True:
            self.itemconfig(self.circle, fill='red')
            self.status = False
        else:
            self.itemconfig(self.circle, fill='lime')
            self.status = True
