from tkinter import *
from datetime import date

root = Tk()
root.title("[LOG OF _____]")
root.geometry("400x300")


##82B1C2

lbl = Label(text="<HELLO>", fg= "darkblue", bg= "#BDCBD1",height= 1,width=300)
name_lbl = Label(text="<ENTER LOG NAME>", bg= "#BDCBD1",fg="darkblue")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "[WELCOME TO THE APPLICATION.\n LOG DATE:-]"
    greet = "[HELLO "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height= 3)
btn = Button(text="<END>", command= display,fg= "darkblue", bg= "#BDCBD1",height=1,width=300)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
