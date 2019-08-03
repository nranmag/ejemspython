from datetime import *

#print(datetime.now(),"\n")
formato = "%m-%d-%y %H:%M:%S"

#Abrir y leer archivo LOG
f = open('log1.log','r')
#Leyendo primera linea
mensaje = f.readline()
m = mensaje[1:18]
m = datetime.strptime(m, formato)
print(m)
#Leyendo ultima linea
mensaje2 = f.readlines()[-1]
#print("\n\n",mensaje2)
m2 = mensaje2[1:18]
m2 = datetime.strptime(m2, formato)
print(m2)
#Cerrando archivo
f.close()
#Recopilar datos para diferencia
data1 = m
data2 = m2

diff = data2 - data1 
#Operaciones con fecha y hora
days, seconds = diff.days, diff.seconds 
hours = days * 24 + seconds // 3600 
minutes = (seconds % 3600) // 60 
seconds = seconds % 60 

print("El workflow duró: ",hours,"hrs ",minutes,"m ",seconds,"s")