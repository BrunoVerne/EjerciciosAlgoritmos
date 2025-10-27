# En un tablero de ajedrez (una cuadrícula de 8x8) se ubica la pieza llamada “caballo”
# en la esquina superior izquierda. Un caballo tiene una manera peculiar de moverse por el
# tablero: Dos casillas en dirección horizontal o vertical y después una casilla más en
# ángulo recto (formando una forma similar a la letra “L”). El caballo se traslada de la casilla
# inicial a la final sin tocar las intermedias, dado que las “salta”. Se quiere determinar si es
# posible, mover esta pieza de forma sucesiva a través de todas las casillas del tablero,
# pasando una sola vez por cada una de ellas, y terminando en la casilla inicial. Plantear la
# solución mediante backtracking.


# def solucion(n):
#     tablero = matriz n x n inicializada en False
#     movimientos_parciales = []
#     soluciones = []
#     backtracking((0,0), n, 1, tablero, movimientos_parciales, soluciones)
#     retornar soluciones

# def backtracking(pos, n, contador, tablero, movimientos_parciales, soluciones):
#     i,j = pos
#     si i<0 o j<0 o i>=n o j>=n:
#         retornar
#     si tablero[i][j] == True:
#         retornar

#     tablero[i][j] = True
#     movimientos_parciales.agregar(pos)
#     contador = contador + 1

#     si contador == n*n:
#         soluciones.agregar(copia(movimientos_parciales))
#         movimientos_parciales.pop()
#         retornar

#     para nueva_pos en movs_posibles(pos):
#         backtracking(nueva_pos, n, contador, tablero, movimientos_parciales, soluciones)

#     tablero[i][j] = False
#     movimientos_parciales.pop()
    
#    movs_posibles(pos):
#    	i,j = pos
#    	return [(i+2,j+1),(i+1,j+2),(i-1,j+2),(i-2,j+1),(i-2,j-1),(i-1,j-2),(i+1,j-2),(i+2,j-1)]
    

	
