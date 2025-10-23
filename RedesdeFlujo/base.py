





# ALGORITMO FordFulkerson(grafo, fuente, sumidero)
#         flujo_maximo = 0
#         MIENTRAS exista un camino aumentante:
#             // Buscar camino aumentante usando BFS o DFS
#             camino = BFS(grafo, fuente, sumidero)
            
#             SI (camino == NULL) ENTONCES
#                 break 
#             FIN SI
            
#             // Encontrar la capacidad residual mínima en el camino
#             flujo_camino = ∞
#             PARA cada arista en el camino:
#                 flujo_camino = MIN(flujo_camino, capacidad_residual)
#             FIN PARA
            
#             PARA cada arista en el camino:
#                 arista.capacidad = arista.capacidad - flujo_camino
                
#                 arista_inversa.capacidad = arista_inversa.capacidad + flujo_camino
#             FIN PARA
            
#             flujo_maximo = flujo_maximo + flujo_camino
#         FIN MIENTRAS
        
#         RETORNAR flujo_maximo
#     FIN



def dfs(grafo, nodo_actual, visitado):
    """
    DFS recursivo simple
    grafo: lista de listas (matriz de adyacencia)
    nodo_actual: nodo desde donde empezamos
    visitado: lista de nodos visitados
    """
    # Marcar el nodo actual como visitado
    visitado[nodo_actual] = True
    
    # Recorrer todos los nodos vecinos
    for vecino in range(len(grafo)):
        # Si hay conexión y no está visitado
        if grafo[nodo_actual][vecino] > 0 and not visitado[vecino]:
            dfs(grafo, vecino, visitado)

def busqueda_anchura(grafo, fuente, sumidero, padres):
    """
    Busca un camino desde la fuente hasta el sumidero
    usando búsqueda en anchura
    """
    visitado = [False] * len(grafo)
    cola = []
    
    cola.append(fuente)
    visitado[fuente] = True
    padres[fuente] = -1  # o sea el padre de la fuente no existe porque él es padre de todos
    
    while cola:
        nodo_actual = cola.pop(0)
        
        for nodo_vecino in range(len(grafo)):
            if not visitado[nodo_vecino] and grafo[nodo_actual][nodo_vecino] > 0:
                cola.append(nodo_vecino)
                visitado[nodo_vecino] = True
                padres[nodo_vecino] = nodo_actual
                
                if nodo_vecino == sumidero:
                    return True
    return False

def ford_fulkerson(grafo, fuente, sumidero):
    """
    Algoritmo de Ford-Fulkerson para encontrar flujo máximo
    """
    # Crear copia del grafo para no modificar el original
    grafo_residual = [fila[:] for fila in grafo]
    flujo_maximo = 0
    padres = [-1] * len(grafo) #lista de padres que inicializa en -1 porque ninguno fue visitado por lo tanto no se quien es el padre
    
    # MIENTRAS exista un camino aumentante:
    while busqueda_anchura(grafo_residual, fuente, sumidero, padres):
        # Encontrar la capacidad residual mínima en el camino
        flujo_camino = float('inf')
        nodo_actual = sumidero
        
        # Recorrer el camino de vuelta para encontrar el flujo mínimo
        while nodo_actual != fuente:
            nodo_anterior = padres[nodo_actual]
            flujo_camino = min(flujo_camino, grafo_residual[nodo_anterior][nodo_actual])
            nodo_actual = nodo_anterior
        
        # Actualizar capacidades residuales
        nodo_actual = sumidero
        while nodo_actual != fuente:
            nodo_anterior = padres[nodo_actual]
            # arista.capacidad = arista.capacidad - flujo_camino
            grafo_residual[nodo_anterior][nodo_actual] -= flujo_camino
            # arista_inversa.capacidad = arista_inversa.capacidad + flujo_camino
            grafo_residual[nodo_actual][nodo_anterior] += flujo_camino
            nodo_actual = nodo_anterior
        
        # flujo_maximo = flujo_maximo + flujo_camino
        flujo_maximo += flujo_camino
    
    return flujo_maximo