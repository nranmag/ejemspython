from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

Label(miFrame, text="Hola que tal?", fg="red", font=("Comic Sans MS", 18)).place(x=200, y=50)

root.mainloop()