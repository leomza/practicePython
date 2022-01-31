""" 
TIPOS DE DATOS

string (str): 'Hello'
integer (int): 1
floating (float): 1.25
listas (lst) -> Es como un array: ['sal', 1 , -3, 'chau']
diccionarios (dic) -> Es como un objeto JSON: {'color: 'rojo', 'numero': 3, 'avion': 'azul'}
tuples (tup) -> Es como una lista pero es inmutable, no se puede agregar ni sacar elementos: ('lun', 'mar', 'mie', 'jue', 'vie') 
sets (set) -> Es como una lista pero solo tiene elementos UNICOS, no tiene elementos repetidos: {'a','b','c','d','e'}
booleanos (bool): True, False
"""


nombre = input('Dime tu nombre')
print('Hola mi amigo ' + nombre)

print(type(nombre))

#CONVERSION DE VARIABLES:
edad = input('Dime tu edad')
print(type(edad))
edad = int(edad)
print(type(edad))

#Para lograr imprimir esa variable debo 'formatear' la cadena de la siguiente forma: {} y al final .format(variables ha imprimir)
print('Tu nueva edad va a ser {} y al siguiente año sera {}'.format(edad+1, edad+2))

#Otra opcion mucho mas legible para imprimir cadenas con tipos mixtos es colocando la letra 'f' delante y las comillas con las variables dentro:
print(f'Tu nueva edad va a ser {edad+1} y al siguiente año sera {edad+2}')
