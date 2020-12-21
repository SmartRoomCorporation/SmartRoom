import tkinter as tk
from tkinter import Listbox
from PIL import Image
from PIL import ImageTk
from pprint import pprint
up=Image.open("up.png")

#up=up.resize((20,20))
pprint(up)
up_icon=ImageTk.PhotoImage(up)



# creaiamo una finestra dove poi andremo a inserire altri elementi

window = tk.Tk()

#andiamo a personalizzarla dandole un'altezza e larghezza

window.geometry("900x700")
window.title("SmartRoom")
window.resizable(False,False)
window.grid_columnconfigure(0, weight=1)
window.configure(bg="grey")


#ora lo posizioniamo nella nostra schermata

welcome_label = tk.Label(window, text="Welcome in the My SmartRoom", font=("Helvetica",15))
welcome_label.grid(row=0, column=0, sticky="WE",padx=20,pady=10)

welcome_label = tk.Label(window, text="Lista Sensori", font=("Helvetica",15))
welcome_label.grid(row=1, column=0, sticky="WE",padx=20,pady=10)


text = "Sensore 1:"
text_output = tk.Label(window, text=text, fg="Green", font=("Helevetica",16))
text_output.grid(row=2, column=0,sticky="W")
text = "valore:"
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=3, column=0,pady="5",sticky="W")
text = "Trigger:"
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=4, column=0,pady="5",sticky="W")
first_button = tk.Button(text="Aumenta")
first_button.grid(row=4, column=1,padx="30",sticky="W")
first_button = tk.Button(text="Diminuisci")
first_button.grid(row=4, column=1,padx="100",sticky="W")
text = "Stato: "
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=5, column=0,pady="5",sticky="W")



text = "Sensore 2:"
text_output = tk.Label(window, text=text, fg="Green", font=("Helevetica",16))
text_output.grid(row=6, column=0,sticky="W")
text = "valore:"
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=7, column=0,pady="5",sticky="W")
text = "Trigger:"
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=8, column=0,pady="5",sticky="W")
first_button = tk.Button(text="Aumenta")
first_button.grid(row=8, column=1,padx="30",sticky="W")
first_button = tk.Button(text="Diminuisci")
first_button.grid(row=8, column=1,padx="100",sticky="W")
text = "Stato: "
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=9, column=0,pady="5",sticky="W")

text = "Sensore 3:"
text_output = tk.Label(window, text=text, fg="Green", font=("Helevetica",16))
text_output.grid(row=10, column=0,sticky="W")
text = "valore:"
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=11, column=0,pady="5",sticky="W")
text = "Trigger:"
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=12, column=0,pady="5",sticky="W")
first_button = tk.Button(text="Aumenta")
first_button.grid(row=12, column=1,padx="30",sticky="W")
first_button = tk.Button(text="Diminuisci")
first_button.grid(row=12, column=1,padx="100",sticky="W")
text = "Stato: "
text_output = tk.Label(window, text=text, fg="black", font=("Helevetica",16))
text_output.grid(row=13, column=0,pady="5",sticky="W")





#per avviare tale interfaccia utilizziamo il metodo:

if __name__== "__main__":
    window.mainloop()