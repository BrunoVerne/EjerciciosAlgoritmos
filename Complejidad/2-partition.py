# Una de las parejas más ricas del mundo está pasando por un proceso de divorcio. Entre
# sus bienes cuentan con propiedades, autos, motos, estampillas raras y otros coleccionables.
# Como no se ponen de acuerdo en la manera de dividirlos, el juez ha dictaminado que un
# tasador ponga valor a cada bien y luego se haga una partición por valores iguales (el
# problema abstracto se conoce como 2-partition) El juez nos pide que elaboremos un
# algoritmo que en forma eﬁciente haga este trabajo. Demuestre que la solución pedida en
# NP-completa. Sugerencia: Pruebe con “subset sum”.







# def solucion(L,K,S1,S2):
# 	vS1 = 0
	
	
# 	validador = copia de L 			O(L)
	
# 	for i = 0 hasta |S1|-1: 		O(S1)
# 		valor = S1[i]
# 		if valor not in L:		O(L)
# 			return False
# 		vs1 += valor
		
# 		if valor not in validador:
# 			return False
			
# 		validador.borrar(valor)
	
# 	vS2 = 0
# 	for i = 0 hasta |S2|-1: 		O(S2)
# 		valor = S2[i]
# 		vs2 += valor
# 		if valor not in L:          O(L)
# 			return False
		
# 		if valor not in validador:
# 			return False
			
# 		validador.borrar(valor)
			
# 	if vS1 != vS2 or vS1 != K: 		O(1)
# 		return False
	
# 	return True
	
# TOTAL = O(S1*L + S2*L) = O((S1+S2)*L) = O(L²)
	
	
# Representacion: Subset Sum(L,K) --> L = 2K--> 2-Partition(L) --> resultado 2Partition S1, S2 / S1 = K --> resultado Subset Sum = S1 Ó S2

# Dado un problema de Subset Sum con un vector L y un valor K / la suma de los valores de L = 2K, entonces si existe solucion  S1,S2 en 2-Partition(L,K) la solucion de Subset Sum con valor K será S1 ∨ S2
# Dado un problema de 2-Partition con un vector L y un valor K si existe solución S1, S2 entonces existira solución S1 ∨ S2 en Subset Sum(L,K)


# L,K)∈SubsetSum⟺(L,K)∈2-Partition siempre que la suma total de 𝐿 sea 2𝐾
