""" STRING """

#Para que un string sea largo y no tome los saltos de lineas se agregan 3 comillas
poema = """Mil pequeños peces blancos
 como si hirviera 
 el color del agua"""

print(poema)

#Para detectar si una palabra esta incluida en un String:
print("agua" in poema) #Devolvera "true"
print("leo" in poema) #Devolvera "false"
print("leo" not in poema) #Devolvera "true"

""" LISTAS """
my_lista = ['c','d','t']
my_lista1 = ['d','e','f']

print(len(my_lista))

my_lista2 = my_lista + my_lista1 #Concatenar listas
print(my_lista2)

my_lista2.append('g') #Agregar un elemento a la lista
my_lista2.pop(3) #Eliminar un elemento a la lista
print(my_lista2)

my_lista2.sort() #Ordena la lista
print(my_lista2)
