from tkinter import *

window = Tk()
window.minsize(250,150)
window.title("Mile to Km Converter")
window.config(padx=5,pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

mile_input = Entry(width="10")
mile_input.grid(column=1,row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)

km_value_label = Label(text="0")
km_value_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

def convert():
    mile_value = mile_input.get()
    km_value = float(mile_value) * 1.609
    km_value_label.config(text=str(km_value))

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1,row=2)

window.mainloop()
