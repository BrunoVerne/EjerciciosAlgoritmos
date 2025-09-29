# Seconoce como “Longest increasing subsequences” al problema de, dado un vector de
#  numérico, encontrar la subsecuencia más larga de números (no necesariamente
#  consecutivos) donde cada elemento sea mayor a los anteriores. Ejemplo: En la lista → 2, 1, 4,
#  2, 3, 9, 4, 6, 5, 4, 7. Podemos ver que la subsecuencia más larga es de longitud 6 y
#  corresponde a la siguiente “1, 2, 3, 4, 6, 7”. Resolver el problema mediante programación
#  dinámica.

def subsequences(vector):
    n= len(vector)
    OPT = [0] * n
    contador_max = 0
    for i in range(n):
        contador_local = 0
        for j in range(i):
            if vector[j] <= vector[i]:
                OPT[i] = max(OPT[i], OPT[j]+1)
        contador_max = max(contador_max, contador_local)
    return contador_max


if __name__ == "__main__":
    lista = [2, 1, 4,2, 3, 9, 4, 6, 5, 4, 7]
    print(subsequences(lista))
    
    
    

#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.