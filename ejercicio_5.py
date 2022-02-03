vocal = ""
while len(vocal) != 1 :
    vocal = input("Ingresa una letra: ")
vocal = vocal.lower()
if vocal  in "aeiou":
    print("Ingresaste una vocal.")
else:
    print("No ingresaste una vocal.")