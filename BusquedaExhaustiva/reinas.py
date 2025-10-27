# Resuelva el problema de las reinas en el tablero de ajedrez mediante backtracking
# planteado como permutaciones. Brinde el pseudocódigo y determine la cantidad máxima
# posible de subproblemas a explorar

def resolver_reinas(N):
    Q = [0] * N  # Q[i] será la columna de la reina en la fila i
    soluciones = []
    backtrack(0, Q, N, soluciones)
    return soluciones

def backtrack(fila, Q, N, soluciones):
    if fila == N:  # Todas las reinas colocadas
        soluciones.append(Q.copy())
        return
    for columna in range(N):
        if es_valido(Q, fila, columna):
            Q[fila] = columna
            backtrack(fila + 1, Q, N, soluciones)
            Q[fila] = 0  # Retroceso

def es_valido(Q, fila, columna):
    for i in range(fila):
        if Q[i] == columna:  # Misma columna
            return False
        if abs(Q[i] - columna) == abs(i - fila):  # Misma diagonal
            return False
    return True

if __name__ == "__main__":
    N = 4
    sols = resolver_reinas(N)
    print(f"Se encontraron {len(sols)} soluciones para N={N}:")
    for sol in sols:
        print(sol)        
        
        
        
        
        
        
