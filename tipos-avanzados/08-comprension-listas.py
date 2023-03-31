usuarios = [['Camilo', 4], ['Felipe', 10], ['Miguel', 2]]

'''nombres = []
for i in usuarios:
    nombres.append(i[0])
print(nombres)'''

nombre = [i[0] for i in usuarios]

# Filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)