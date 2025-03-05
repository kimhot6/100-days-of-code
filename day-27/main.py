from tkinter import *

def on_click():
    mile = int(mile_input.get())
    output.config(text=f"{mile*1.6}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(380,200)
window.config(padx=10,pady=10)

mile_input = Entry(width=7)
mile_input.grid(row=0,column=1)

miles = Label(text="Miles")
miles.grid(row=0,column=2)
miles.config(padx=10)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1,column=0)

output = Label(text="0")
output.grid(row=1,column=1)

Km = Label(text="Km")
Km.grid(row=1,column=2)

button = Button(text="Calculate", command=on_click)
button.grid(row=2,column=1)

window.mainloop()
