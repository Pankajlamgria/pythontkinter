from tkinter import *
root=Tk()
root.geometry("1300x750")
root.minsize(222,111)

f1=Frame(root,bg="pink",borderwidth=6,relief="flat",height="50")
f1.pack(fill="x")
l1=Label(f1,text="WELCOME TO PANKAJ'S PYTHONG GUI",font=("momicsans ms",14,"bold"),bg="pink",fg="white")
l1.pack(pady=10)
f2=Frame(root,bg="pink",borderwidth=6,relief="flat",width=200)
f2.pack(side="left",fill="y",pady="1",padx="2")
l2=Label(f2,text="Home",font=("momicsans ms",14,"bold"),bg="pink",padx="30",borderwidth=2,relief="sunken")
l3=Label(f2,text="About",font=("momicsans ms",14,"bold"),bg="pink",padx="30",borderwidth=2,relief="sunken")
l4=Label(f2,text="New",font=("momicsans ms",14,"bold"),bg="pink",padx="30",borderwidth=2,relief="sunken")
l5=Label(f2,text="Download",font=("momicsans ms",14,"bold"),bg="pink",padx="30",borderwidth=2,relief="sunken")
l2.pack(fill="x")
l3.pack(fill="x")
l4.pack(fill="x")
l5.pack(fill="x")


root.mainloop()