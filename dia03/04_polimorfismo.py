"""Polimorfismo en programación es un funcion/metodo/operador
con el mismo nombre que se puede ejecutar en muchas formas"""

texto = "Hola soy un texto"
diccionario = {
    "id": 1,
    "nombre": "Arturo",
    "edad": 30
}
tupla = (1, "Texto", False)
lista = [False, "Texto", 100.5]

print(len(texto)) # ✔️
print(len(diccionario)) # ✔️
print(len(tupla)) # ✔️
print(len(lista)) # ✔️

for letra in texto: # ✔️
    print(letra)

for clave in diccionario: # ✔️
    print(clave)

for item in tupla: # ✔️
    print(item)

for item in lista: # ✔️
    print(item)



""" Nota:

1. pass significa que python no haga nada y continue

2.la funcion len se puede ejecutar de muchas formas.

3. En el editor se pone CTRL +i , y se muestra los emojis.

4.EL POLIMORFISMO se cumple en el for  tambien. 

5.Una tupla es una coleccion de datos, no se pude modificar en cambio una lista si se puede modificar

"""
