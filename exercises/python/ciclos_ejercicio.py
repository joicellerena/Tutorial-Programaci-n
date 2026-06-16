# Ejercicio: sumar los primeros N números pares
N = int(input("Ingresa N (cantidad de pares a sumar): "))
contador = 0
suma = 0
num = 2
while contador < N:
    suma += num
    num += 2
    contador += 1
print(f"La suma de los primeros {N} números pares es: {suma}")
