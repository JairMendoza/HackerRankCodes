class Universidad:
    def __init__(self,nombreUniversidad):
        self.nombreUniversidad = nombreUniversidad
class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad
class Estudiante(Universidad , Carrera):
    def datos(self , nombre , edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}. Estudio en la universidad {} ".format(
            self.nombre,self.edad,self.especialidad,self.nombreUniversidad))


persona = Estudiante("UTEG")
persona.carrera("Computacion")
persona.datos("Jair",22)


