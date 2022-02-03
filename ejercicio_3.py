from math import sqrt
valorA = int(input("Ingrese el valor de 'a': "))
valorB = int(input("Ingrese el valor de 'b': "))
valorC = int(input("Ingrese el valor de 'c': "))
x1 = 0
x2 = 0
if ((valorB ** 2) - (4 * valorA * valorC)) < 0:
    print("No se puede realizar la operacion porque no se puede sacar raiz a un numero negativo.")
else:
    x1 = (-valorB + sqrt((valorB**2) - (4 * valorA * valorC))) / (2 * valorA)
    x2 = (-valorB - sqrt((valorB**2) - (4 * valorA * valorC))) / (2 * valorA)
    print("La solucion es: \nRespuesta 1: " , x1 , "\nRespuesta 2: " , x2)


