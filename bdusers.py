from tkinter import *
from tkinter import messagebox
import db

ppal=Tk()
ppal.title("Login")
ppal.iconbitmap("logo2.ico")

def logindb():
	conexion = db.con
	cursor = conexion.cursor()
	sql = "SELECT *FROM admin"
	cursor.execute(sql)
	row = cursor.fetchone()
	if user.get()==row[2] and passw.get()==row[3]:
		vlogin.destroy()
		messagebox.showinfo("Bienvenido","Has iniciado sesion como Admin")
		acceso()
	else:
		messagebox.showerror("Error de Sesión","Lo siento no eres Admin")
		user.set("")
		passw.set("")

def regdb():
	conexion = db.con
	cursor = conexion.cursor()
	sql = "INSERT INTO admin VALUES(*args)"
	cursor.execute(sql)
	conexion.commit()

def ventnvo():
	v=Tk()
	v.title("Ingresar nuevo User")
	v.iconbitmap("logo2.ico")
	vnvo=Frame(v, width=400, height=200)
	vnvo.pack()
	eCampus=StringVar()
	nombreCompleto=StringVar()
	status=StringVar()
	userDuluth=StringVar()
	userMfs=StringVar()
	rol=StringVar()
	id_eti=Label(vnvo, text="E-campus:", font=("Calibri", 14))
	id_eti.grid(row=0, column=0, padx=5, pady=5, sticky="e")
	id_txt=Entry(vnvo, textvariable=eCampus, font=("Calibri", 14))
	id_txt.grid(row=0, column=1, padx=5, pady=5)
	nom_eti=Label(vnvo, text="Nombre completo:", font=("Calibri", 14))
	nom_eti.grid(row=1, column=0, padx=5, pady=5, sticky="e")
	nom_txt=Entry(vnvo, textvariable=nombreCompleto, font=("Calibri", 14))
	nom_txt.grid(row=1, column=1, padx=5, pady=5)
	stat_eti=Label(vnvo, text="Status:", font=("Calibri", 14))
	stat_eti.grid(row=2, column=0, padx=5, pady=5, sticky="e")
	stat_txt=Entry(vnvo, textvariable=status, font=("Calibri", 14))
	stat_txt.grid(row=2, column=1, padx=5, pady=5)
	udul_eti=Label(vnvo, text="User Duluth:", font=("Calibri", 14))
	udul_eti.grid(row=3, column=0, padx=5, pady=5, sticky="e")
	udul_txt=Entry(vnvo, textvariable=userDuluth, font=("Calibri", 14))
	udul_txt.grid(row=3, column=1, padx=5, pady=5)
	umfs_eti=Label(vnvo, text="User MFS:", font=("Calibri", 14))
	umfs_eti.grid(row=4, column=0, padx=5, pady=5, sticky="e")
	umfs_txt=Entry(vnvo, textvariable=userMfs, font=("Calibri", 14))
	umfs_txt.grid(row=4, column=1, padx=5, pady=5)
	rol_eti=Label(vnvo, text="Rol:", font=("Calibri", 14))
	rol_eti.grid(row=5, column=0, padx=5, pady=5, sticky="e")
	rol_txt=Entry(vnvo, textvariable=rol, font=("Calibri", 14))
	rol_txt.grid(row=5, column=1, padx=5, pady=5)
	b=Button(v, text="Registrar", font=("Calibri", 16))
	b.pack()
	v.mainloop()

user = StringVar()
passw = StringVar()

vlogin=Frame(ppal, width=370, height=250)
vlogin.pack()
ifondo=PhotoImage(file="fondo1.png")
Label(vlogin, image=ifondo).place(x=-200, y=-200)
Label(vlogin, text="Escribe tu Usuario de MFS", font=("Calibri", 16)).place(x=20,y=30)
Entry(vlogin, width="25", textvariable=user, font=("Calibri", 16)).place(x=60,y=60)
Label(vlogin, text="Password", font=("Calibri", 16)).place(x=20,y=110)
p=Entry(vlogin, width="25", textvariable=passw, font=("Calibri", 16))
p.place(x=60,y=140)
p.config(show="*")
b=Button(vlogin, text="Ingresar", font=("Calibri", 16), command=logindb)
b.place(x=150, y=190)

def salir():
	resp=messagebox.askquestion("Salir", "¿Deseas cerrar la aplicación?")
	if resp=="yes":
		ppal.destroy()

def acceso():
	acces=Frame(ppal, width=800, height=700)
	acces.pack()
	ppal.title("Ventana Principal")
	ifondo=PhotoImage(file="fondo1.png")
	Label(ppal, image=ifondo).place(x=10, y=10)
	#Creación de la Barra de Menús y submenus#
	bmenu=Menu(ppal)
	archivo=Menu(bmenu, tearoff=0)
	archivo.add_command(label="Nuevo User", command=ventnvo, font=("Calibri", 14))
	archivo.add_command(label="Guardar", font=("Calibri", 14))
	archivo.add_command(label="Cerrar", command=salir, font=("Calibri", 14))
	buscarb=Menu(bmenu, tearoff=0)
	buscarb.add_command(label="Buscar por E-campus", font=("Calibri", 14))
	buscarb.add_command(label="Buscar por User MFS", font=("Calibri", 14))
	buscarb.add_command(label="Buscar por User Duluth", font=("Calibri", 14))
	herram=Menu(bmenu, tearoff=0)
	ayuda=Menu(bmenu, tearoff=0)
	ayuda.add_command(label="Acerca de...", font=("Calibri", 16))
	bmenu.add_cascade(label="Archivo", font=("Calibri", 16), menu=archivo)
	bmenu.add_cascade(label="Buscar", menu=buscarb)
	bmenu.add_cascade(label="Herramientas", menu=herram)
	bmenu.add_cascade(label="Ayuda", menu=ayuda)
	ppal.config(menu=bmenu)
	ppal.mainloop()

ppal.mainloop()