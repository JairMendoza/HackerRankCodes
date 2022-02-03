def funcionDecoradora(funcionParametro):
    #*args es para que la funcion interior soporte el envio de argumentos (genera una tupla)
    #**kwargs es para que la funcion interior soporte argumentos clave valor (a = 23)(genera un diccionario)
    #tambien se puede especificar el nombre de la variable
    def funcionInterior(*args , **kwargs):
        #codigo de decoracion
        print("Vamos a realizar un calculo.")
        funcionParametro(*args , **kwargs)

        #codifo de decoracion
        print("Hemos terminado el calculo")
    return funcionInterior
@funcionDecoradora
def suma(a , b):
    print(a + b)

def resta(a , b):
    print(a - b)
@funcionDecoradora
def potencia(base , exponente):
    print(pow(base , exponente))

suma(5 , 3)
resta(9 , 3)
potencia(base = 5 ,exponente = 3)
