class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 3
        self.energia = 3
        self.felicidad = 3

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1

    def dormir(self):
        if self.energia < 5:
            self.energia += 1

    def jugar(self):
        if self.felicidad < 5:
            self.felicidad += 1
        if self.energia > 0:
            self.energia -= 1

    def actualizar(self):
        if self.hambre < 5:
            self.hambre += 1
        if self.felicidad > 0:
            self.felicidad -= 1
        if self.energia > 0:
            self.energia -= 1

    def esta_vivo(self):
        return self.hambre > 0 and self.felicidad > 0 and self.energia > 0

    def estado(self):
        print(f"{self.nombre}:")
        print(f"🍔 Hambre: {self.hambre}")
        print(f"⚡ Energia: {self.energia}")
        print(f"😄 Felicidad: {self.felicidad}")


def main():
    nombre_tamagotchi = input("Ingresa el nombre de tu Tamagotchi: ")
    tamagotchi = Tamagotchi(nombre_tamagotchi)

    while tamagotchi.esta_vivo():
        tamagotchi.estado()
        print("1. Alimentar Tamagotchi")
        print("2. Hacer que juegue")
        print("3. Hacer que descanse")
        accion = input("¿Qué deseas hacer? ")

        if accion == "1":
            tamagotchi.alimentar()
            print("🍔 Le diste de comer.")
        elif accion == "2":
            tamagotchi.jugar()
            print("🎮 Jugaste con él.")
        elif accion == "3":
            tamagotchi.dormir()
            print("💤 Lo dejaste descansar.")
        else:
            print("Opción incorrecta. Intenta de nuevo.")

        tamagotchi.actualizar()

    print(f"{tamagotchi.nombre} ha muerto. 💀")


if __name__ == "__main__":
    main()

"""Principales correcciones realizadas

1.Los nombres de las funciones y métodos han sido corregidos para seguir el estilo snake_case en lugar de camelCase.
2.Los valores de la energía y la felicidad se han ajustado para que tengan un rango de 0 a 5 en lugar de 0 a 255.
3.Se han corregido los mensajes de impresión en los métodos estado() y main().
4.La función esta_vivo() ahora devuelve True si todos los atributos (hambre, felicidad y energia) son mayores que 0, lo que significa que el Tamagotchi está vivo.
Con estas correcciones, el programa debería funcionar correctamente, y podrás interactuar con tu Tamagotchi mientras se mantiene vivo con las acciones disponibles. """