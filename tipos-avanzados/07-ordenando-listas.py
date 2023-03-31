numeros = [1, 20, 30, 50, 80, 4]

#numeros.sort() # Ordena la lista de menors a mayor
#numeros.sort(reverse=True) # Ordena la lista de mayor a menor
numeros2 = sorted(numeros) # Devuelve una NUEVA lista ordenada
numeros3 = sorted(numeros, reverse=True) # Devuelve una NUEVA lista ordenada de mayor a menor
print(numeros3)
print(numeros2)

usuarios = [['Camilo', 4], ['Felipe', 10], ['Miguel', 2]]

usuarios.sort(key=lambda el: el[1])
print(usuarios)