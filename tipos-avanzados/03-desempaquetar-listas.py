numeros = [1, 2, 3]

# Mal!
'''primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]'''

primero, segundo, tercero = numeros
print(primero)
#--------------------------------------
primero, *otros = numeros # otros empaquetas las otras variables de la lista
print(primero, otros)