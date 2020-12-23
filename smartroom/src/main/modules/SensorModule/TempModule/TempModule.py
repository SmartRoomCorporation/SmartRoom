import time
import board
import adafruit_dht as ad
from PIL import Image, ImageTk
import tkinter as tk



class TempModule(SensorModule):
    #This module implements the temperature control function
	dht = adafruit_dht(board.D4)

	def startMeasure(self):
		try:
			temp = dht.temperature
			super().setCurrValue(temp)
			return temp
		except RuntimeException as Error:
			return super().getCurrValue()
		except Exception as Error:
			return super().getCurrValue()

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