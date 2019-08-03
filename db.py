import pymysql

datos = {
	"user":"root",
	"password":"",
	"database":"userdb",
	"host":"127.0.0.1"
}

try:
	con = pymysql.connect(** datos)
	print("Recursos conectados")
except:
	print("Error de conexion")