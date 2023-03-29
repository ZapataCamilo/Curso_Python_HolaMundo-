print('Bienvenidos')
print('Para salir escribe salir')

numero1 = ''
while True:
    if not numero1:
        numero1 = input('Ingrese numero: ')
        if numero1.lower() == 'salir':
            break
        numero1 = int(numero1)
    op = input('Ingrese operacion: ')
    if op.lower() == 'salir':
        break
    numero2 = input('Ingrese el siguiente numero: ')
    numero2 = int(numero2)
    if op.lower() == 'suma':
        print(numero1 + numero2)
    elif op.lower == 'resta':
        print(numero1 - numero2)
    elif op.lower == 'mul':
        print(numero1 * numero2)
    elif op.lower() == 'div':
        print(numero1 / numero2)
    
