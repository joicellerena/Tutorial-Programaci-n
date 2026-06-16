# Solución: eliminar duplicados manteniendo orden

def eliminar_duplicados(L):
    resultado = []
    for x in L:
        if x not in resultado:
            resultado.append(x)
    return resultado

print(eliminar_duplicados([1,2,3,2,1,4]))
