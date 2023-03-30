def no_space(texto):
    new_text = ''
    for char in texto:
        if char != ' ':
            new_text += char
    return new_text

def reverse(texto):
    new_texto = ''
    for char in texto:
        new_texto = char + new_texto
    return new_texto

def es_palidromo(texto):
    texto = no_space(texto)
    texto = texto.lower()
    return reverse(texto) == texto

print('Reconocer', es_palidromo("Reconocer"))
print('Somos o no somos', es_palidromo("Somos o no somos"))