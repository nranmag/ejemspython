print("Verificación de Acceso")

edad_usuario=int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100:
	print("Edad incorrecta")
else:	
	print("Acceso permitido")
print("El programa ha terminado")