preguntas=int(input('ingrese la cantidad de preguntas '))
print('cantidad de prefuntas: ', preguntas)

correctas=int(input('ingrese la cantidad de preguntas correctas '))
print('cantidad de preguntas correctas: ', correctas)

porcentaje= correctas * 100/ preguntas
print('el porcentaje es: ',"{:.2f}".format(porcentaje))

if (porcentaje >= 90):
	print('Excelente')
elif (porcentaje >=70):
	print('Bueno')
elif (porcentaje >= 60):
	print('Aprobado')
else: 
	print('No alcanzo')

