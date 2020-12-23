from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk

class TempModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0
	guiBlock = ""

	def __init__(self):
    		self.guiBlock = super().createGUIBlock()
    		createTempGui(self.guiBlock)

	def startMeasure(self):
		if (self.count == 0):
			self.count = self.count + 1
			return self.setCurrValue(20)
		elif (self.count > 0 and self.count < 20):
			if (self.count % 3) == 0:
				if (self.getCurrValue() > 10): self.setCurrValue(self.getCurrValue() - 1)
				else: self.setCurrValue(self.getCurrValue() + 1)
		elif (self.count > 30 and self.count < 60):
			if (self.count % 3) == 0:
				if (self.getCurrValue() < 28): self.setCurrValue(self.getCurrValue() + 1)
				else: self.setCurrValue(self.getCurrValue() - 1)
		elif (self.count > 70): self.count = 0
		self.count = self.count + 1
		return self.getCurrValue()
	
	def getGUIBlock(self):
    		return self.guiBlock

	def createTempGui(self, block):
			upimg = Image.open("up.png")
			upimg = upimg.resize((20,20))
			up_icon = ImageTk.PhotoImage(upimg)
			up1=Image.open("down.png")
			up1=up1.resize((20,20))
			up_icon1=ImageTk.PhotoImage(up1)
			text = "Sensore 1:"
			text_output = tk.Label(block, text=text, fg="Green", font=("Helevetica",16))
			text_output.grid(row=2, column=0,sticky="W")
			text = "valore:"
			text_output = tk.Label(block, text=text, fg="black", font=("Helevetica",13))
			text_output.grid(row=3, column=0,pady="5",sticky="W")
			text = "Trigger:"
			text_output = tk.Label(block, text=text, fg="black", font=("Helevetica",13))
			text_output.grid(row=4, column=0,pady="5",sticky="W")
			first_button = tk.Button(image=up_icon)
			first_button.grid(row=4, column=1,padx="30",sticky="W")
			first_button = tk.Button(image=up_icon1)
			first_button.grid(row=4, column=1,padx="100",sticky="W")
			text = "Stato: "
			text_output = tk.Label(block, text=text, fg="black", font=("Helevetica",13))
			text_output.grid(row=5, column=0,pady="5",sticky="W")