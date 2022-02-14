#Para que un string sea largo y no tome los saltos de lineas se agregan 3 comillas
poema = """Mil pequeños peces blancos
 como si hirviera 
 el color del agua"""

print(poema)

#Para detectar si una palabra esta incluida en un String:
print("agua" in poema) #Devolvera "true"
print("leo" in poema) #Devolvera "false"
print("leo" not in poema) #Devolvera "true"