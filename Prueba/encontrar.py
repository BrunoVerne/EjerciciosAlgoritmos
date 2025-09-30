# tengo una matriz tal que el elemento es mayor al que esta abajo y a su derecha
# encontrar el indice de cierto elemento si existe, retornar alguno de ellos no es necesario encontrar mas de uno

def encontrar(matriz, inicio_col, fin_col, inicio_fila, fin_fila, elemento):
    if fin_col < inicio_col or fin_fila < inicio_fila:
        return None
    
    mitad_col = (inicio_col + fin_col) // 2
    mitad_fila = (inicio_fila + fin_fila) // 2
    valor = matriz[mitad_fila][mitad_col]

    if valor > elemento:
        if matriz[mitad_fila + 1][mitad_col] == elemento:
            return (mitad_fila+1, mitad_col)
        
        elif matriz[mitad_fila][mitad_col+1] == elemento:
            return (mitad_fila, mitad_col+1)

        return encontrar(matriz,inicio_col, mitad_col-1, inicio_fila, mitad_fila-1, elemento)
    
        
    elif valor < elemento:
        if matriz[mitad_fila-1][mitad_col] == elemento:
            return (mitad_fila-1, mitad_col)
        
        elif matriz[mitad_fila][mitad_col-1] == elemento:
            return (mitad_fila, mitad_col-1)
        
        return encontrar(matriz, mitad_col+1, fin_col, mitad_fila+1, fin_fila, elemento)
    
    return mitad_col, mitad_fila


if __name__ == "__main__":
    matriz = [[15,13,12],
              [14,11,9],
              [8,7,6]]
    n = len(matriz)
    print(encontrar(matriz,0,n-1,0,n-1,9))
    print(encontrar(matriz,0,n-1,0,n-1,11))
    print(encontrar(matriz,0,n-1,0,n-1,12))
    print(encontrar(matriz,0,n-1,0,n-1,8))
    print(encontrar(matriz,0,n-1,0,n-1,13))