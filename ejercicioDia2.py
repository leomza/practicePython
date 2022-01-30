nombre = input('Ingrese su nombre')
ventas = input('Ingrese sus ventas')

comision= round((int(ventas)*13)/100,2)

print(f'Felicidades {nombre} sus ventas fueron de ${ventas} y su comision ganada es de ${comision}')
