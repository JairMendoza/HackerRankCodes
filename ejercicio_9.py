for i in range(1, 11):
    print(i)
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa un numero: "))
if numero1 < numero2:
    while numero1 <= numero2:
        print(numero1)
        numero1 += 1
else:
    for i in range(numero2 , numero1+1):
        print(i)