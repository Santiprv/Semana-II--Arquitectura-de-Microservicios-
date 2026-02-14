def fibonacci(n):
    a, b = 1, 1

    if n <= 2:
        return 1
    
    for i in range(n - 2):
        a, b = b, a + b
        
    return b

n = int(input("Número de reintento: "))
print(f"Debes esperar {fibonacci(n)} segundos.")