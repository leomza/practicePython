# METODO INDEX()

miTexto = 'Esta es una prueba'
resultado = miTexto[0]
resultado1 = miTexto.index('s')

print(resultado1)

# EXTRAER SUBSTRINGS (el primer indice lo incluye, el segundo NO):
miVariable = 'Esta palabra sera extraida'
resultado2 = miVariable[5:12]

print(resultado2)

""" 
upper(): Pasar a mayusculas
lower(): Pasar a minusculas
split(): Separar en partes (lista)
join(): Unir items usando separador
find(): Encontrar en sub-string
replace(): Reemplazar un sub-string 
"""
ejemplo = 'Este es el texto de Leonardo'
ejemploSplit = ejemplo.split()
print(ejemploSplit) #Crea una lista que contiene las palabras

a='Aprender'
b='Python'
c='es'
d='genial'
e=(' ').join([a,b,c,d]) #El join solo funcion con listas y al principio pongo como quiero que esten unidos
print(e)

frase='Esta frase de texto es para reemplazar letras'
frase_corta = frase.replace('a', 'leo') #Reemplazará todas las letras 'a' por 'leo'
print(frase_corta)

