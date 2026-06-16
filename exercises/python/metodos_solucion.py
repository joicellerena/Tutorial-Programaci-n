# Solución: determinar si un número es primo

def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Ingresa un número: "))
print(es_primo(n))
