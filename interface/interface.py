import tkinter as tk


# creaiamo una finestra dove poi andremo a inserire altri elementi

window = tk.Tk()

#andiamo a personalizzarla dandole un'altezza e larghezza

window.geometry("600x600")
window.title("SmartRoom")
#window.resizable(False,False)
#window.configure(background = "grey")

def first_print():
    text = "Stanza 1"
    text_output = tk.Label(window, text=text, fg="red", font=("Helevetica",16))
    text_output.grid(row=0, column=1,sticky="W")

def second_function():
    text = "Stanza 2"
    text_output = tk.Label(window, text=text, fg="green", font=("Helevetica",16))
    text_output.grid(row=1, column=1, padx=50, sticky="W")

#definiamo un button

first_button = tk.Button(text="Click 1" ,command=first_print)
#ora lo posizioniamo nella nostra schermata

first_button.grid(row=0, column=0,sticky="W")

second_button=tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20,sticky="W")

#per avviare tale interfaccia utilizziamo il metodo:

if __name__== "__main__":
    window.mainloop()

