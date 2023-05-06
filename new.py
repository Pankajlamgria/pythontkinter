from tkinter import *
# to work with jpg file
from PIL import Image,ImageTk

root=Tk()
root.geometry("1300x750")
root.minsize(222,111)


# for png image
# photo=PhotoImage(file="screenshot.png")
# label=Label(image=photo)
# new_label=Label(text="hello world")
# label.pack()


# for jpg image
# photo=Image.open("myimg.jpg")
# newphoto=ImageTk.PhotoImage(photo)
# newlabel=Label(image=newphoto)
# newlabel.pack()


# label attributes
label=Label(text='''hellkdfjls flksjfl lajdfla dfa\nlksjfl sjalfjlf ladfs\nlksj flalfjpa\na lkfjaf
            sjflsjflalfsdj\nlajflasflkjalfd\n akflajsflajf''',fg="cyan",bg="grey",borderwidth='3',relief="sunken" 
            ,padx="23",pady="50",font=("The Times Roman ",23,"italic"))

label.pack(pady="50",padx="32",fill="y",side="left",anchor="sw")
root.mainloop()