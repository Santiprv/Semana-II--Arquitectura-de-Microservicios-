angulo1 = float(input("Introduce el primer angulo: "))
angulo2 = float(input("Introduce el segundo angulo: "))
angulo3 = float(input("Introduce el tercer angulo: "))

angulos = (angulo1, angulo2, angulo3)


if angulo1 == angulo2 == angulo3 and angulo1 + angulo2 + angulo3 == 180:
    print("Es un triangulo equilatero")
        

elif angulo1 != angulo2 == angulo3 or angulo1 == angulo2 != angulo3 and angulo1 + angulo2 + angulo3 == 180:
    print("Es un triangulo Isoceles")
    if angulo1 or angulo2 or angulo3 == 90:
         print("Es un triangulo Isoceles y uno de sus angulos de 90 grados")
            

elif angulo1 != angulo2 != angulo3 and angulo1 + angulo2 + angulo3 == 180: 
     print("Es un triangulo Escaleno")
     if angulo1 or angulo2 or angulo3 == 90:
        print("Es un triangulo Escaleno y uno de sus angulos es de 90 grados")
            
else:
     print("La suma de los angulos excede de 180")


