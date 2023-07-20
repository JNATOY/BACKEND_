class MiClase:
    def metodoNormal(self):
        self.__metodoPrivado()

    def __metodoPrivado(self):
        print("Soy un método privado")

clase = MiClase()

clase.metodoNormal()

""" 1. para convertir un metodo privado se pone dos guines bajo
2.para ocultar un algoritmo se puede poner como metodo privado

3.Se usa cuando sea necesario """