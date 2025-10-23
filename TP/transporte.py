import sys

def ejecucion(productos, subconjuntos):
    productos_lista = productos.split(",")
    
    # Convertir subconjuntos a lista de tuplas
    subconjuntos_lista = [tuple(s.split(',')) for s in subconjuntos.replace('),(', '|').strip('()').split('|')]
    
    # Ordenar por longitud descendente
    subconjuntos_ordenados = sorted(subconjuntos_lista, key=len, reverse=True)
    
    mejor_solucion = None
    min_camiones = float('inf')
    
    def calcular_cota(camiones, cubiertos, idx):
        productos_restantes = len(set(productos_lista) - cubiertos)
        if productos_restantes == 0:
            return len(camiones)
        
        # Encontrar el subconjunto compatible más grande
        max_len = 0
        for i in range(idx, len(subconjuntos_ordenados)):
            if not (set(subconjuntos_ordenados[i]) & cubiertos):
                max_len = max(max_len, len(subconjuntos_ordenados[i]))
        
        if max_len == 0:
            return float('inf')
        
        return len(camiones) + (productos_restantes + max_len - 1) // max_len
    
    def backtrack(camiones, cubiertos, idx):
        nonlocal mejor_solucion, min_camiones
        
        # Si ya cubrimos todos los productos
        if cubiertos == set(productos_lista):
            if len(camiones) < min_camiones:
                mejor_solucion = camiones.copy()
                min_camiones = len(camiones)
            return
        
        if idx >= len(subconjuntos_ordenados):
            return
        
        # Poda: si la cota es mayor o igual que la mejor solución actual, podar
        cota = calcular_cota(camiones, cubiertos, idx)
        if cota >= min_camiones:
            return
        
        backtrack(camiones, cubiertos, idx + 1)
        
        subconjunto_actual = subconjuntos_ordenados[idx]
        conjunto_actual = set(subconjunto_actual)
        if not (conjunto_actual & cubiertos):
            backtrack(camiones + [subconjunto_actual], cubiertos | conjunto_actual, idx + 1)
    
    backtrack([], set(), 0)
    return mejor_solucion if mejor_solucion is not None else []

if __name__ == "__main__":
    productos = sys.argv[1]
    subconjuntos = sys.argv[2]
    resultado = ejecucion(productos, subconjuntos)
    if resultado:
        print(",".join(f"({','.join(s)})" for s in resultado))
    else:
        print("No se encontró solución")