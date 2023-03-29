def prueba(nombre, apellido): # Lo que esta dentro del paréntesis se llama parametro
    print('Bienvenido!')
    print(nombre, apellido)

prueba('Camilo', 'Zapata') # Lo que esta dentro de paréntesis se llama argumento

"""
---------Parametros de forma opcional-----------
"""
def prueba(nombre, apellido='Zapata'): # Lo que esta dentro del paréntesis se llama parametro
    print('Bienvenido!')
    print(nombre, apellido)

prueba('Camilo', 'Hernandez') # Lo que esta dentro de paréntesis se llama argumento
prueba('Daniel')

"""
--------Argumentos nombrados------------------
"""
prueba(apellido='Restrepo', nombre='Andres')