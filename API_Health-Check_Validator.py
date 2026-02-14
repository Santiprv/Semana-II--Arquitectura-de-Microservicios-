def health_check(latencia, uso_cpu, estado_db):
    if latencia < 200 and uso_cpu < 80  and estado_db == "conectada":
        return True
    else:
        return False
    


latencia = float(input("Introduce la latencia: "))
uso_cpu = int(input("Introduce el uso del cpu (en porcentaje): "))
estado_db = input("Introduce el estado de la base de datos (conectada o no conectada): ")

resultado = health_check(latencia, uso_cpu, estado_db)
print(resultado)
