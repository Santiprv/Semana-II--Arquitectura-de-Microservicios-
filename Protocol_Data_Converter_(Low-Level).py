
print("1.Convertir a binario\n2.Convertir a hexadecimal")

opcion = int(input("Ingresa una opcion: "))


if opcion == 1:
    decimal = float(input("Ingresa un número: "))
    
    if decimal == 0:
        print("El binario es: 0")
    else:
        binario_final = ""
        temp_decimal = decimal 
        
        while temp_decimal > 0:
            residuo = temp_decimal % 2
            binario_final = str(residuo) + binario_final
            temp_decimal = temp_decimal // 2
            
        print(f"El número {decimal} en binario es: {binario_final}")

elif opcion == 2:
    decimal = float(input("Ingresa un número: "))
    hex_caracteres = "0123456789ABCDEF"
    hex_final = ""
    temp_decimal = decimal
    
    if temp_decimal == 0:
        hex_final = "0"
    else:
        while temp_decimal > 0:
            residuo = temp_decimal % 16
            hex_final = hex_caracteres[residuo] + hex_final
            temp_decimal = temp_decimal // 16
            
    print(f"El número {decimal} en hexadecimal es: {hex_final}")
    
