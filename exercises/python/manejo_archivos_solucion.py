# Solución: ejemplo simple de CSV de calificaciones
import csv
calificaciones = [('Ana', 15), ('Juan', 12), ('María', 17)]
with open('calificaciones.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['nombre','nota'])
    writer.writerows(calificaciones)

# Leer y calcular promedio
suma = 0
cont = 0
with open('calificaciones.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        suma += float(row['nota'])
        cont += 1
print('Promedio:', suma/cont)
