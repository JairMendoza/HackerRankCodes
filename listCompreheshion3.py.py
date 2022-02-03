num_doble_cuadrado = [(num, num*2, num**2) for num in range(10)]
print(num_doble_cuadrado)

saludos = ['hola', 'saludos', 'hi']
nombres = ['j2logo', 'antonio', 'vega']
frases = ['{} {}'.format(saludo.title(), nombre.title()) for saludo in saludos for nombre in nombres]
print(frases)