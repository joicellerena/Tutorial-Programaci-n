# Ejemplo: leer archivo y contar líneas

with open('muestra.txt', 'w', encoding='utf-8') as f:
    f.write('Linea1\nLinea2\nLinea3\n')

with open('muestra.txt', 'r', encoding='utf-8') as f:
    lineas = f.readlines()
print('Número de líneas:', len(lineas))
