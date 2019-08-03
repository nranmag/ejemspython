from tkinter import *

raiz=Tk()

raiz.title("Ventana de Pruebas")

#raiz.resizable(0,0) #nos deja mover ya sea altura o anchura

raiz.iconbitmap("logo1.ico")

#raiz.geometry("650x350") #el tamaño de la ventana

raiz.config(bg="blue")

miFrame=Frame() #creamos nuestro primer frame pero debemos empaquetarlo, siguiente linea

miFrame.pack() #empaquetado para que pueda correr dentro de la raíz

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

raiz.mainloop()