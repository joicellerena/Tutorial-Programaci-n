# Solución: transponer y producto matricial

def transponer(m):
    return [list(row) for row in zip(*m)]


def producto(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Ejemplo
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print('A x B =', producto(A,B))
