# Se realiza un experimento de conductividad de un nuevo material en aleación con
# otro. Se formaron muestras numeradas de 1 a n. A mayor número, mayor concentración del
# nuevo material. Además se realizaron “n” mediciones a diferentes temperaturas de
# conductividad para cada muestra. Los resultados fueron expresados en una matriz M de
# nxn. Se observa que un mismo material cuanto mayor temperatura tiene mayor
# conductividad. Además, cuanto mayor concentración a la misma temperatura, también
# mayor conductividad. En conclusión podemos, al analizar la matriz, ver dos progresiones.
# Cada fila tiene números ordenados de forma creciente y cada columna tiene números
# ordenados de forma creciente. Dada la matriz M, los experimentadores quieren encontrar
# en qué posición se encuentra un determinado número. Proponga una solución utilizando
# división y conquista
def encontrar(M, col_min, col_max, fila_min, fila_max, numero):

    if fila_min > fila_max or col_min > col_max:
        return False
    
    mitad_fila = (fila_min + fila_max) // 2
    mitad_col = (col_min + col_max) // 2
    
    valor = M[mitad_fila][mitad_col]
    if valor == numero:
        return [mitad_fila, mitad_col]
    
    elif valor > numero:
        # izquierda
        res = encontrar(M, col_min, mitad_col - 1, fila_min, fila_max, numero)
        if res:
            return res
        # arriba
        return encontrar(M, col_min, col_max, fila_min, mitad_fila - 1, numero)
    
    else: # valor < numero
        # derecha
        res = encontrar(M, mitad_col + 1, col_max, fila_min, fila_max, numero)
        if res:
            return res
        # abajo
        return encontrar(M, col_min, col_max, mitad_fila + 1, fila_max, numero)
    



#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.