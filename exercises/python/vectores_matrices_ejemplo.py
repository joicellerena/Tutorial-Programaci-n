# Ejemplo: operaciones con vectores y matrices (listas anidadas)

# Suma de vectores
v1 = [1, 2, 3]
v2 = [4, 5, 6]
suma = [a+b for a, b in zip(v1, v2)]
print('Suma:', suma)

# Transpuesta simple
m = [[1,2,3],[4,5,6]]
trans = [list(row) for row in zip(*m)]
print('Transpuesta:', trans)
