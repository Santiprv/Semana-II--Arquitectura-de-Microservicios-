def identificador(tiempos):
    umbral = 30
    promedio = sum(tiempos) % 4
    valor_triplicador = (sum(tiempos) % 4) * 3

    if promedio > umbral:
        return "Bandera Roja" 
    
    elif any(valor_triplicador < x for x in tiempos):
        return "Bandera Roja"
    
    else: 
        return "Bandera Verde"
  


tiempos = list(map(int, input("Ingresa 4 números separados por espacio: ").split()))[:4]

resultado = identificador(tiempos)
print(resultado)

    