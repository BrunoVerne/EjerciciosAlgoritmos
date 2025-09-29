
def solucion(lista, opciones):
    inicio = 0
    n = len(lista)
    votaciones = [0] * len(opciones)
    for i in range(len(opciones)):
        ultimo_indice = contarindices(lista,inicio,n-1, opciones[i])
        votaciones[i] = (ultimo_indice - inicio) + 1 
        inicio = ultimo_indice + 1 

    return votaciones

def contarindices(n, inicio, fin, elemento):
    if fin <= inicio:
        if n[fin] == elemento:
            return fin
        return inicio
    
    medio = (inicio + fin) // 2

    if n[medio] == elemento:

        if n[fin] != elemento:
            if  fin - medio == 1:
                return medio
            return contarindices(n, medio, fin, elemento)
        else:  
            return fin 
    

    if n[medio] < elemento:
        return contarindices(n, medio+1, fin, elemento)
    
    else:
        return contarindices(n, inicio, medio, elemento)


    


if __name__ == "__main__":
    lista = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

    print(solucion(lista, [1,2,3,4]))
    
    

#COMPLEJIDAD TEMPORAL: O(m*log(n)) COMPLEJIDAD ESPACIAL O(log(n)  m):  EC DE RECURRENCIA: T(n) = T(n/2) + 0(1), T(n, m) = m × T(n) + O(m)