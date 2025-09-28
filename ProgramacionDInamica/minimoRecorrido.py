# Un dueño de un camión de transporte se comprometió a trasladar una carga de una
# ciudad A a la ciudad B. Para realizar el recorrido puede optar por diferentes caminos que
# pasan por diferentes ciudades intermedias. Nos acerca un mapa donde para cada tramo que
# une las diferentes ciudades indica el costo de realizar el mismo. Vemos que algunos costos
# son positivos (combustible, peaje, etc) y otros negativos o cero (yendo por esos tramos
# puede ganar unos pesos haciendo algunos encargos "particulares"). Nos solicita que le
# informemos cuál sería el recorrido óptimo para minimizar el gasto total del viaje. Presentar
# un algoritmo polinomial utilizando programación dinámica que lo resuelva



def CaminoMinimo(Grafo G, Nodo A, Nodo B):
    for cada nodo v en G:
        dist[v] = infinito
        prev[v] = null
    dist[A] = 0

    for i = 1 to |V|-1: # |V| es el numero de nodos (ciudades) del grafo
        for cada arista (u,v) en G:
            if dist[u] + w(u,v) < dist[v]:
                dist[v] = dist[u] + w(u,v)
                prev[v] = u

    # Reconstruir camino
    camino = []
    v = B
    while v != null:
        insertar v al inicio de camino
        v = prev[v]

    return dist[B], camino






def bellman_ford(ciudades, aristas, origen, destino):
    """
    ciudades: lista de nombres de ciudades, ej: ['A','B','C']
    aristas: lista de tuplas (u, v, costo), ej: [('A','B',5), ('B','C',-2)]
    origen: ciudad de inicio
    destino: ciudad de llegada
    """
    # Inicializar distancias y predecesores
    dist = {c: float('inf') for c in ciudades}
    prev = {c: None for c in ciudades}
    dist[origen] = 0

    # Relajar todas las aristas |V|-1 veces
    for i in range(len(ciudades) - 1):
        for u, v, costo in aristas:
            if dist[u] + costo < dist[v]:
                dist[v] = dist[u] + costo
                prev[v] = u

    # Comprobar ciclos negativos
    for u, v, costo in aristas:
        if dist[u] + costo < dist[v]:
            raise ValueError("Ciclo de peso negativo detectado")

    # Reconstruir camino óptimo
    camino = []
    v = destino
    while v is not None:
        camino.insert(0, v)
        v = prev[v]

    return dist[destino], camino
