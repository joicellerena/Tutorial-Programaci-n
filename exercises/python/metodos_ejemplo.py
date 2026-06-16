# Ejemplo: factorial usando función

def factorial(n):
    if n < 2:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))  # 120
