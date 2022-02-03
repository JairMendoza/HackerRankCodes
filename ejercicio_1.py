cadena = "Te quiero solo como amigo"

#Imprimiendo los dos primeros caracteres
print(cadena [0 : 2])

#Imprimiendo los tres ultimos caracteres
print(cadena [-3 : ])

#imprimiendo cada dos caracteres
contador = 0
dosCaracteres = ""
for imprimir in cadena:
    if contador % 2 == 0:
        dosCaracteres +=imprimir
    contador += 1

print(dosCaracteres)
# esto es mucho mas efectivo que hacer el for de arriba y hace lo mismo OJO!!!!
print(cadena[: : 2])

#Imprimiedo la cadena invertida
longitud = len(cadena)
print(cadena[longitud:: -1])
# esto es mucho mas efectivo que hacer lo de arriba y hace lo mismo OJO!!!!
print(cadena[: : -1])

#Imprimiendo la cadena en los dos sentidos
dosSentidos = cadena + cadena[longitud:: -1]
print(dosSentidos)
print(cadena + cadena[: : -1])