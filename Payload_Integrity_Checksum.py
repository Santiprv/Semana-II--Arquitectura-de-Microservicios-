API = str(input("Ingrese una API: "))

suma_total = sum(ord(letra) for letra in API)

if suma_total % 2 == 0: 
    print("Paquete Integro")
else:
    print("Paquete no Integro")
