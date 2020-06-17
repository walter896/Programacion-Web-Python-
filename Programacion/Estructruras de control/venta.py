venta1 = int(input('Ingrese el total de las ventas del dia 1: '))
venta2 = int(input('Ingrese el total de las ventas del dia 2: '))

if venta1 > venta2 :
	print ('Se vendió mas el dia 1')
elif venta1 < venta2 :
	print('Se vendio mas el dia 2')
else :
	print('Se vendio lo mismo ambos dias')

