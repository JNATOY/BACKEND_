class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")


persona1 = Persona("Miguel", 40)

# persona1.saludar()

"""Crear un Objeto Gato que tenga los atributos nombre y color
y que tenga los métodos dormir y estado"""

class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.estaDurmiendo = False

    def cambiarEstado(self, estado):
        self.estaDurmiendo = estado

    def estado(self):
        if self.estaDurmiendo == False:
            print(f"{self.nombre} está despierto")
        else:
            print(f"{self.nombre} está durmiendo")

gato = Gato("Michi", "Blanco")
gato.estaDurmiendo = False
gato.cambiarEstado(True)
# gato.estado()

"""Crear un objeto Usuario que tenga los atributos id, nombre, email, password
que tenga un metodo que me muestre sus datos ordenados en un diccionario
y otro metodo que encripte la password del usuario"""

import hashlib
from pprint import pprint

class Usuario:
    def __init__(self, id, nombre, email, password):
        self.id = id
        self.nombre = nombre
        self.correo = email
        self.password = self.hashPassword(password)

    def mostrarUsuario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password
        }
    
    def hashPassword(self, password):
        pwd_bytes = password.encode()
        hash_pwd = hashlib.sha256(pwd_bytes).hexdigest()
        return hash_pwd
    
usuario = Usuario(1, "Cesar Mayta", "cesar@gmail.com", "osito123")

pprint(usuario.mostrarUsuario())






""" notas:

1.hacer objeto de usuario

2.se crea un metodo que se muestre lo datos en un diccionario

3. creando metodo que nos permite encriptar una contraseña

4.se convierte en bytes la contraseña , luego seleccionamos el algoritmo que queremos incriptar y luego usamos un metodo para que muestre los caracteres.

5.Finalemnte, que se guarde en pasword encriptado.

6.nota: hay dos librerias que se usara haslib y pprint.

7.sha256 (es el algoritmo para encriptar la contraseña)

8.hexdigest(es el metodo que nos retona la contraseña encriptada)
 """