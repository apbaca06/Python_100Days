from tkinter import *
# document: http://tcl.tk/man/tcl8.6/TkCmd/entry.html

window = Tk()
window.title("GUI Program")
window.minsize(500, 600)


my_label = Label(text="I'm a label.", font=("Arial", 24, "italic"))

# Pack the label on to the screen
my_label.pack(side="top")
my_label.pack(expand=False)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")

my_button = Button(text="Click Me", command=button_clicked)
my_button.pack(side="top")

input = Entry(width=10)
input.pack()



# Keep the window on the screen
window.mainloop()
