import math

def calculo_nodos(x1,x2,y1,y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distancia < 10:
        return True
    
    else:
        return False

x1 = float(input("Ingrese x1: "))
x2 = float(input("Ingrese x2: "))
y1 = float(input ("Ingrese y1: "))
y2 = float(input("Ingrese y2: "))

resultado = calculo_nodos(x1,x2,y1,y2)

print(resultado)



