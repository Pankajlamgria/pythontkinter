from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("333x222")
photo=PhotoImage(file="screenshot.png")
label=Label(image=photo)
new_label=Label(text="hello world")
# label.pack()
new_label.pack()

root.mainloop()