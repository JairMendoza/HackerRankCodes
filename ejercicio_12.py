class Marino:
    def hablar(self):
        print("Hola...")

class Pulpo:
    def hablar(self):
        print("soy un pulpo.")

class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje = mensaje
        print(self.mensaje)



pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca.")

marino = Marino()
marino.hablar()
