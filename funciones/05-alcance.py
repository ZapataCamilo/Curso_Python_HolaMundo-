"""
Usar variables globales es una mala practica
"""
saludo = 'Hola Global'

def saludar():
    global saludo
    saludo = 'Hola Mundo'


def saludoperson():
    saludo = 'Hola persona'
    print(saludo)

print(saludo)
saludar()
print(saludo)
