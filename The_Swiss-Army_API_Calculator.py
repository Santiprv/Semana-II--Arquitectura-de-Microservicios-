def suma(a,b):
    operacion = a + b
    resultado = operacion
    print(resultado)

def resta(a,b):
    operacion = a - b
    resultado = operacion
    print (resultado)

def multiplicacion(a,b):
    operacion = a*b
    resultado = operacion
    print(resultado)

def division(a,b):
    operacion = a/b
    resultado = operacion
    print(resultado)

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

def binario(n):
    print(bin(n))

def hexadecimal(n):
    print(hex(n))


print("Bienvenidos a la calculadora\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Fibonacci\n6.Binario\n7.Hexadecimal")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: ")) 
    suma(a,b)

elif opcion == 2:
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))
    resta(a,b)

elif opcion == 3:
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))
    multiplicacion(a,b)

elif opcion == 4:
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))
    division(a,b)

elif opcion == 5:
    n = int(input("Ingrese cuantos numeros de la serie quiere: "))
    fibonacci(n)

elif opcion == 6:
    n = int(input("Ingrese que numero quiere convertir en binario: "))
    binario(n)

elif opcion == 7:
    n = int(input("Ingrese que numero quiere convertir en hexadecimal: "))
    hexadecimal(n)



