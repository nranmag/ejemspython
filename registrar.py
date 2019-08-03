from tkinter import *
from tkinter import messagebox

def registrar(*args):
	#Mandar los datos a la BD.
	import pymysql
	connection = pymysql.connect(
	host="localhost",
	user="root",
	password="",
	db="usersdb"
	)
	cursor = connection.cursor()
	valores = "INSERT INTO useragencia(ecampus) VALUES(eCampus)"#(eCampus, nombreCompleto, status, userMfs, userDuluth, rol)"
	try:
		cursor.execute(valores)
		connection.commit()
		messagebox.showinfo("Guardado", "Se han insertado los valores dentro de la BD")
	except:
		messagebox.showerror("Error al cargar datos...", "No se ha podido ingresar valores a la BD")

	connection.close()
