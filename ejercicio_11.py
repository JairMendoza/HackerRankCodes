class alumno:
    nombre = ""
    nota = 0
    def obtenerDatos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.nota = int(input("Ingresa tu nota: "))
    def imprimirDatos(self):
        print("Su nombre es: {}".format(self.nombre))
        print("Su nota es: {}".format(self.nota))
    def calificar(self):
        if self.nota >= 6:
            print("Felicidades has aprobado!")
        else:
            print("Lo sentimos reprobaste. :c")

alumno1 = alumno()
alumno1.obtenerDatos()
alumno1.imprimirDatos()
alumno1.calificar()


class calcular:
    base = 0
    exponente = 0
    resultado = 0
    def potenciar(self):
        self.resultado = pow(self.base , self.exponente)
        print("El resultado es: {}".format(self.resultado))
operacion = calcular()
operacion.base = int(input("Ingresa la base: "))
operacion.exponente = int(input("Ingresa el expponente: "))
operacion.potenciar()


    