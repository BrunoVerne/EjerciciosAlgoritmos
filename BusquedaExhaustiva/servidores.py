# Se cuenta con “n” servidores especializados en renderización de videos para
# películas animadas en 3d. Los servidores son exactamente iguales. Además contamos
# con “m” escenas de películas que se desean procesar. Cada escena tiene una duración
# determinada. Queremos determinar la asignación de las escenas a los servidores de
# modo tal de minimizar el tiempo a esperar hasta que la última de las escenas termine de
# procesarse. Determinar dos metodologías con la que pueda resolver el problema y
# presente cómo realizar el proceso.
	
	

# def solucion(n,m)
# 	resultados = []
# 	asignacion = [-1] * |m|
# 	tiempo_minimo = ∞
# 	tiempos_servidores = []
# 	BandB(0, n,m,tiempo_minimo,tiempos_servidores, asignacion, resultado)
# 	return resultado, tiempo_minimo


# BandB(indice,n,m,tiempo_minimo,tiempos_servidores, asignacion, resultado):
# 	if indice == |m|:
# 		if max(tiempos_servidores) < tiempo_minimo:
# 			tiempo_minimo = copia(max(tiempos_servidores))
# 			resultado = copia(asignacion)
# 		return
	
# 	for i = 0 hasta |n|-1:
# 		tiempos_servidores[i] += m[indice]
# 		asignacion[indice] = i
		
# 		cota = max(tiempos_servidores) #solamente mirando los servidores que estan asignados 
# 		if cota < tiempo_minimo:
# 			BandB(indice+1,n,m,tiempo_minimo, tiempos_servidores, asignacion, resultado)
			
# 			tiempo_servidores[i] -= m[indice]
# 			asignacion[indice] = -1
			
			
		
	
		
		


