Premium = 1000
Standard = 100 
servidor_mantenimiento  = 0

tipo_de_usuario = input("Ingrese el tipo de usuario: ").upper()
estado_servidor = input("Ingrese el estado del servidor: ").upper()

if estado_servidor == "mantenimiento":
    print(f"{servidor_mantenimiento}")

elif tipo_de_usuario == "standard" and estado_servidor == "activo":
    print(f"{Standard}")

elif tipo_de_usuario == "premium" and estado_servidor == "activo":
    print(f"{Premium}")






