diccionario = {"Guatemala": "Ciudad de Guatemala",
                 "El Salvador": "San Salvador", 
                 "Honduras": "Honduras",
                 "Nicaragua": "Managua", 
                 "Costa Rica": "San Jose", 
                 "Panama": "Panama", 
                 "Argentina": "Buenos Aires", 
                 "Colombia": "Bogota", 
                 "Venezuela": "Caracas", 
                 "España": "Madrid"}
pais = input("Ingrese un pais: ")

if pais.capitalize() in diccionario:
    print("La capital de " , pais , "es: " , diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario.")
