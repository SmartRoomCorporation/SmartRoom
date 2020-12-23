import tkinter as tk 
class SensorModule:
	curr_value = 0
	left_side = ""
	right_side = ""

	def setCurrValue(self, curr_value):
		self.curr_value = curr_value

	def getCurrValue(self):
		return self.curr_value

	def startMeasure(self):
		return 0

	def createGUIBlock(self, block):
		
		frame1 = tk.Frame(block)
		frame2 = tk.Frame(block)
			
		frame1.configure(highlightbackground="black", highlightcolor="black", highlightthickness=1, width=350, height=200, bd= 0,bg="grey")
		frame2.configure(highlightbackground="black", highlightcolor="black",highlightthickness=0.5,bg="white", width=550, height=200)
			
		frame1.grid(row=0, column=0)
		frame2.grid(row=0, column=1)
        
		left_side=frame1
		right_side=frame2