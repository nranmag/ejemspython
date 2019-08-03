from tkinter import * # Python3
 
def __Cancel(event=None): pass
 
root = Tk()
root.title("Título")
root.resizable(0,0)
root.attributes("-toolwindow",-1)
root.protocol('WM_DELETE_WINDOW', __Cancel )
 
root.mainloop()
 