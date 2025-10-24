# Se conoce Bin-Packing al problema de decisión donde se cuenta con “N” elementos de
# diferentes pesos y con “M” contenedores de cierta capacidad. Queremos saber si es posible
# acomodar todos los elementos en no más de k contenedores. Se pide demostrar que el
# problema es NP-Completo. Sugerencia utilizar 2-partition.


# def solucion(N,M,K,S):
# 	if |S| > K or |S| > M:				O(1)
# 		return False
	
# 	valores_N = suma(N) 				O(N)
# 	valores_S = 0
	
# 	validador = copia de N
	
# 	sea C la capacidad del contenedor
# 	for contenedor in S:				O(S)
# 		if contenedor.capacidad() > C:
# 			return False
# 		for elemento in contenedor:		O(N)
# 			if elemento not in validador:	O(N)
# 				return False
			
# 			validador.quitar(elemento)
# 			valor_S += elemento.valor()
	
# 	if |validador| > 0:				O(1)
# 		return False
	
# 	if valor_S != valor_N:				O(1)
# 		return False
	
# 	return True
	
# TOTAL = O(N²*S)

# Dado un problema de 2-Partition con un vector N y un valor N / 2 = A si lo transformo a un problema de Bin Packing tal que tengo que la cantidad maxima de contenedores K <=2, y sea C la capacidad maxima de los contenedores se cumpla que C=A entonces si existe solucion para Bin-Packing(N,M,K,C) entonces existirá solucion para 2-Partition
# Y En su contraparte dado un problema de Bin Packing con un vector N, M contenedores con capacidad N/2 y un natural K <=2 entonces si existe solucion para 2-Partition(N) enotences existira solucion para Bin-Packing


		
	
	
		
			
	
	