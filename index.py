import pymysql

connection = pymysql.connect(
	host="localhost",
	user="root",
	password="",
	db="usersdb"
	)

cursor = connection.cursor()

valores = "INSERT INTO useragencia(ecampus, nombrec, status, umfs, udul, rol) VALUES('60900000', 'Nahum', 'Activo', 'nahumra', 'nrangel', 'TA')"

try:
	cursor.execute(valores)
	connection.commit()
	print("Se han insertado los valores dentro de la BD")
except:
	print("No se ha podido ingresar valores a la BD")


connection.close()
