# Contamos con un conjunto de “n” actividades entre las que se puede optar por
# realizar. Cada actividad x tiene una fecha de inicio Ix, una fecha de finalización fx y un
# valor vx que obtenemos por realizarla. Queremos seleccionar el subconjunto de
# actividades compatibles entre sí que maximice la ganancia a obtener (suma de los
# valores del subconjunto). Proponer un algoritmo por branch and bound que resuelva el
# problema.



# def solucion(actividades):
# 	mejor_eleccion = []
# 	eleccion_parcial = [0] * |actividades|
# 	mejor_ganancia = -∞
# 	actividades ordenadas segun fecha de finalizacion
# 	BandB(0,mejor_eleccion, eleccion_parcial, mejor_ganancia, actividades)
# 	return mejor_ganancia, mejor_eleccion
	
	
# BandB(indice, mejor_eleccion, eleccion_parcial, mejor_ganancia, actividades):
# 	if indice == |actividades|:
# 		ganancia_actual =  ganancia(eleccion_parcial)
# 		if ganancia_actual> ganancia(mejor_eleccion):
# 			mejor_eleccion = eleccion_parcial
# 			mejor_ganancia = ganancia_actual 
# 			break
		
	
# 	ultima = ultima_actividad(eleccion_parcial)
# 	actividad = actividades[indice]
# 	if actividad.Ix > ultima.Fx or |eleccion_parcial| ==0:
# 		ganancia_posible = ganancia(eleccion_parcial) + cotaSuperiorOptimista(ultima, indice+1, actividades)
# 		if ganancia_posible > mejor_ganancia:
# 			eleccion_parcial.agregar(actividades[indice])
# 			BandB(indice +1, mejor_eleccion, eleccion_parcial, mejor_ganancia, actividades)
# 			eleccion_parcial.borrar(actividades[indice])
			
# 	else:
# 		BandB(indice +1, mejor_eleccion, eleccion_parcial, mejor_ganancia, actividades)
	

# cotaSuperiorOptimista(ultima_elegida, indice, actividades):
#     # Ordeno las actividades restantes por valor descendente
#     actividadesRestantes = actividades[indice:]
#     ordenar(actividadesRestantes, por=vx, descendente=True)
#     ultima = ultima_elegida		
#     suma = 0
#     for act in actividadesRestantes:
#     	if act.Ix > ultima.Fx:	
#         	suma += act.vx
#         	ultima = act
#     return suma
				
			
	