opcion=''
nombres=[]
while(opcion != 'salir'):
	opcion=input('Que opcion desea ejecutar: ')
	if(opcion == 'listar'):
		nombre=input('Inserte el nombre: ')
		a=nombre in nombres
		if(a==True):
			print('Ese nombre ya existe')
		if(a==False):
			nombres.append(nombre)
	if(opcion == 'imprimir'):
		print(nombres)
