def suma(*numeros): # Esto es llamado xargs, estos son unos parametros iterables
    resultado = 0
    for i in numeros:
        resultado += i
    print(resultado)

suma(10, 20)
suma(10, 20, 30, 40)
suma(10, 10, 5, 4, 10)