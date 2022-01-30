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