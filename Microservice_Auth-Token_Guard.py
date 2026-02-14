def validador(token):
    numero = any(caracter.isdigit() for caracter in token)
    palabra_prohibida = "TEST"

    if token[:4].upper() == palabra_prohibida:
        return "No validado"

    elif len(token) >= 12 and numero:
        return "Validado"
    


token = input("Ingrese su token: ")

resultado = validador(token)

print(resultado)