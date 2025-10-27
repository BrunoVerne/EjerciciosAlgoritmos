# Se cuenta con “n” trabajos por realizar y la misma cantidad de contratistas para
# realizarlos. Ellos son capaces de realizar cualquiera de los trabajos aunque una vez que
# se comprometen a hacer uno, no podrán realizar el resto. Tenemos un presupuesto de
# cada trabajo por cada contratista. Queremos asignarlos de forma tal de minimizar el
# costo del trabajo total. Proponer un algoritmo por branch and bound que resuelva el
# problema de la asignación.


# def solucion(C, n)
# 	 #Sea C[i][j] el costo del trabajo i al contratista j
# 	 mejorAsignacion = []
# 	 mejorCosto = ∞
# 	 asignacionParcial = [-1] * n # -1 indica trabajo no asignado
#  	 BandB(0,asignacionParcial, 0, mejorCosto, mejorAsignacion, n,C )
 	 
# BandB(trabajo, asignacionParcial, costoActual, mejorCosto, mejorAsignacion,n,C):
# 	if trabajo == n:
# 		if costoActual < mejorCosto:
# 			mejorCosto = costoActual
# 			mejorAsignacion = asignacionParcial
	
# 	for i = 0 hasta |n|-1:
# 		if i not in asignacionParcial
# 			nuevoCosto = costoActual + C[trabajo][i]
# 			cota = nuevoCosto + cotaInferior(trabajo +1, asignacionParcial,C,n)
			
# 			if cota < mejorCosto:
# 				asignacionParcial[trabajo] = i
# 				BandB(trabajo+1,asignacionParcial, costoActual, mejorCosto, mejorAsignacion,n,C)
# 				asignacionParcial[trabajo] = -1
		
		

# cotaInferior(trabajo, asignacion, C, n):
# 	costoMin = 0
# 	para t = trabajo hasta |n|-1:
# 		minimoActual = ∞
# 		para j = 0 hasta |n|-1:
# 			if j not in asignacion:
# 				costoActual = C[trabajo][j]
# 				if costoActual < minimoActual:
# 					minimoActual = costoActual
				
# 		costoMin += minimoActual
# 	return costoMin
