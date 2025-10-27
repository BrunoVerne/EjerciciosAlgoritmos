# Contamos con una cuadrícula de n*n celdas. Cada celda puede pintarse de 2
# colores: blanco o negro. Por cada fila (y cada columna) nos indican cuantas celdas hay
# que pintar de negro. Debemos obtener todas las coloraciones válidas que cumplan con
# las instrucciones. Resolver mediante Backtracking.



# def solucion(matriz):
# 		sea matriz una matriz toda inicializada en 0s
# 		soluciones = []
# 		contador = 0
# 		Backtraking(matriz,n, soluciones):
				
# 			for i = 0 hasta |n|-1
# 				for j = 0 hasta |n|-1:
# 					posicion = (i,j)
# 					if matriz[i][j]== 0:
# 						negro_col = contar_por_columna(j,"N", matriz)
# 						negros_fila = contar_por_fila(i,"N", matriz)
# 						sin_asignar_col = contar_por_columna(j, "0", matriz)
# 						sin_asignar_fila = contar_por_fila(i, "0", copia(matriz))
						
#    						requisito_fila = negros_requeridos_fila[i]
#                 				requisito_col = negros_requeridos_columna[j]
						
# 						if sin_asignar_col + negro_col < requisito_col or sin_asignar_fila + negro_fila < requisito_fila:
# 							return
						
# 						matriz[i][j] = "N"
# 						Backtraking(matriz,n,soluciones)
# 						matriz[i][j] = "B"
# 						Backtraking(matriz,n,soluciones)
					
# 						matriz[i][j] = 0
# 						return
					

			
# 			cumple_todo = True

# 			for i = 0 hasta |n|-1:
# 				if not cumpleFila(i, matriz):
# 					cumple_todo = False
# 				elif not cumpleColumna(i, matriz):
# 					cumple_todo = False
				
# 			if cumple_todo:
# 				soluciones.agregar(copia(matriz))
			
# 			return
			