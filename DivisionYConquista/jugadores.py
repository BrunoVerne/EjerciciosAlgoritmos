


# Se realiza un torneo con n jugadores en el cual cada jugador juega con todos los otros
# n-1. El resultado del partido solo permite la victoria o la derrota. Se cuenta con los resultados
# almacenados en una matriz. Queremos ordenar los jugadores como P1, P2, …, Pn tal que P1 le
# gana a P2, P2 le gana a P3, …, Pn-1 le gana a Pn (La relación “le gana a” no es transitiva). Ejemplo:
# P1 le gana a P3, P2 le gana a P1 y P3 le gana a P2. Solución: [P1, P3,P2]. Resolver por división y
# conquista con una complejidad no mayor a O(n log n).
def main():
    # Matriz de resultados para 3 jugadores según tu ejemplo:
    # P0 le gana a P2
    # P1 le gana a P0  
    # P2 le gana a P1
    # Solución esperada: [P0, P2, P1] o alguna permutación que cumpla
    
    matriz_resultados = [
        # P0   P1   P2
        [None, False, True],   # P0: pierde con P1, gana a P2
        [True, None, False],   # P1: gana a P0, pierde con P2
        [False, True, None]    # P2: pierde con P0, gana a P1
    ]
    
   
    
    # Ejecutar tu algoritmo
    resultado = ganadores(matriz_resultados)
    
    print("Jugadores ordenados:", resultado)


def ganadores(matriz_resultados):
    cantidad_jugadores =  []
    
    for i in range(len(matriz_resultados)):  # si la matriz es de n x n recorro n porque recorro solo una columna
        cantidad_jugadores.append(i)
        
    return ordenar_ganadores(cantidad_jugadores, matriz_resultados)
    

def ordenar_ganadores(cantidad_jugadores, matriz_resultados):
    n = len(cantidad_jugadores)
    if(n <=1):
        return cantidad_jugadores
    
    mitad = n // 2 
    izquierdo = ordenar_ganadores(cantidad_jugadores[:mitad],matriz_resultados)
    derecho = ordenar_ganadores(cantidad_jugadores[mitad:],matriz_resultados)
    
    return merge(izquierdo, derecho, matriz_resultados)
        



def merge(izquierdo, derecho, matriz_resultados):
    resultado = []
    i =0
    j = 0
    while i < len(izquierdo) and j < len(derecho):
        
        
        jugador_izq = izquierdo[i]   # índice global del jugador
        jugador_der = derecho[j]     # índice global del jugador
        
        if ganaA(jugador_izq, jugador_der, matriz_resultados):
            resultado.append(jugador_izq)
            i += 1
        else:
            resultado.append(jugador_der)
            j += 1
    
    while i < len(izquierdo):
        resultado.append(izquierdo[i])
        i += 1
        
    while j < len(derecho):
        resultado.append(derecho[j])
        j += 1
        
    return resultado


def ganaA(i,j, matriz_resultados):
    return matriz_resultados[i][j]

    
    



if __name__ == "__main__":
    main()    