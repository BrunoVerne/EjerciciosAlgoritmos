class RedFlujo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_arista(self, u, v, capacidad):
        if u not in self.grafo:
            self.grafo[u] = {}
        if v not in self.grafo:
            self.grafo[v] = {}
        self.grafo[u][v] = capacidad
        self.grafo[v][u] = 0

def ford_fulkerson(G, fuente, sumidero):
    Gr = RedFlujo()
    
    for u in G.grafo:
        for v in G.grafo[u]:
            capacidad = G.grafo[u][v]
            if u not in Gr.grafo:
                Gr.grafo[u] = {}
            Gr.grafo[u][v] = capacidad
            if v not in Gr.grafo:
                Gr.grafo[v] = {}
            if u not in Gr.grafo[v]:
                Gr.grafo[v][u] = 0
        
    flujo_maximo = 0
    
    while True:
        visitado = set()
        padre = {}
        cola = [fuente]
        visitado.add(fuente)
        encontrado = False
        
        while cola and not encontrado:
            u = cola.pop(0)
            if u in Gr.grafo:
                for v in Gr.grafo[u]:
                    if v not in visitado and Gr.grafo[u][v] > 0:
                        visitado.add(v)
                        padre[v] = u
                        cola.append(v)
                        if v == sumidero:
                            encontrado = True
                            break
        
        if not encontrado:
            break
        
        flujo_camino = float('inf')
        v = sumidero
        while v != fuente:
            u = padre[v]
            flujo_camino = min(flujo_camino, Gr.grafo[u][v])
            v = u
        
        v = sumidero
        while v != fuente:
            u = padre[v]
            Gr.grafo[u][v] -= flujo_camino
            Gr.grafo[v][u] += flujo_camino
            v = u
        
        flujo_maximo += flujo_camino
    
    visitado = set()
    stack = [fuente]
    visitado.add(fuente)
    
    while stack:
        u = stack.pop()
        if u in Gr.grafo:
            for v in Gr.grafo[u]:
                if v not in visitado and Gr.grafo[u][v] > 0:
                    visitado.add(v)
                    stack.append(v)
    
    A = visitado
    B = set(Gr.grafo.keys()) - A
    
    return flujo_maximo, A, B

def encontrar_conexiones_criticas(G1, fuente, sumidero):
    flujo_maximo, A, B = ford_fulkerson(G1, fuente, sumidero)
    
    conexiones_criticas = []
    
    for vertice in A:
        if vertice in G1.grafo:
            for adyacente in G1.grafo[vertice]:
                if adyacente in B and G1.grafo[vertice][adyacente] > 0:
                    conexiones_criticas.append((vertice, adyacente))
    
    return conexiones_criticas, flujo_maximo

def encontrar_mas_critica(G2, conexiones_criticas, fuente, sumidero):
    flujo_original, _, _ = ford_fulkerson(G2, fuente, sumidero)
    flujo_minimo = float('inf')
    mas_critica = None
    
    for conexion in conexiones_criticas:
        u, v = conexion
        
        cap_uv = G2.grafo[u][v]
        cap_vu = G2.grafo[v][u]
        
        G2.grafo[u][v] = 0
        G2.grafo[v][u] = 0
        
        flujo_actual, _, _ = ford_fulkerson(G2, fuente, sumidero)
        
        if flujo_actual < flujo_minimo:
            flujo_minimo = flujo_actual
            mas_critica = conexion
        
        G2.grafo[u][v] = cap_uv
        G2.grafo[v][u] = cap_vu
    
    return mas_critica

def leer_archivo(nombre_archivo):
    conexiones = []
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                partes = linea.split(',')
                if len(partes) == 3:
                    u, v, capacidad = partes
                    conexiones.append((u.strip(), v.strip(), int(capacidad.strip())))
    return conexiones

def ejecucion(archivo):
    conexiones = leer_archivo(archivo)
    
    G1 = RedFlujo()
    G2 = RedFlujo()
    
    for u, v, capacidad in conexiones:
        G1.agregar_arista(u, v, 1)
        G2.agregar_arista(u, v, capacidad)
    
    fuente = 'P'
    sumidero = 'R'
    
    conexiones_criticas, min_conexiones = encontrar_conexiones_criticas(G1, fuente, sumidero)
    
    if conexiones_criticas:
        mas_critica = encontrar_mas_critica(G2, conexiones_criticas, fuente, sumidero)
        
        conexiones_str = str(conexiones_criticas).replace("'", "")  
        mas_critica_str = str(mas_critica).replace("'", "")  
        
        print(f"{conexiones_str},{mas_critica_str}")
    else:
        print("[],()")

if __name__ == "__main__":
    import sys
    archivo = sys.argv[1]
    ejecucion(archivo)