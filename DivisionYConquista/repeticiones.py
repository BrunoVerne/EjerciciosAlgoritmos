# Dado “L” un listado ordenado de “n” elementos y un elemento “e” determinado.
# Deseamos conocer la cantidad total de veces que “e” se encuentra en “L”. Podemos hacerlo
# en tiempo O(n) por fuerza bruta. Presentar una solución utilizando división y conquista que
# mejore esta complejidad.

def solucion(n, elemento):
    elementos = len(n)
    contador = 0
    return contar(n, 0, elementos-1, elemento)
        

def contar(n, inicio, fin, elemento):
    if inicio  > fin :
        return 0
    
    elif inicio == fin:
        if elemento == n[fin]:
            return 1
        return 0
    
    mitad = (fin+inicio) // 2
    contador_izq = contar(n, inicio, mitad, elemento)
    contador_der = contar(n, mitad+1, fin, elemento)

    return contador_der + contador_izq


if __name__ == "__main__":
    lista1 = [1,1,2,3,4,5,6,7,7,7,7,7,8,8]
    print(solucion(lista1, 1))
    
    



#COMPLEJIDAD TEMPORAL: O(n) COMPLEJIDAD ESPACIAL: O(log(n)) EC DE RECURRENCIA: T(n) = 2T(n/2) +  O(1)
    