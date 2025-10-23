# La policía de la ciudad tiene “n” comisarías dispersas por la ciudad. Para un evento
# deportivo internacional deben asignar la custodia de “m” centros de actividades. Una
# comisaría y un centro de actividades pueden ser emparejados si y sólo si la distancia entre
# ellos no es mayor a un valor d. Contamos con la distancia entre todos los centros y las
# comisarías. Una comisaría sólo puede custodiar un centro. El centro puede ser custodiado
# por una comisaría. Determinar si es posible la asignación de tal forma que todos los centros
# estén custodiados. 

#---------------------PARTE 1----------------------#
# def solucion_parte1():
# 	sea auxiliar un grafo vacio
# 	sea n la lista de comisarias
# 	sea m la lista de centros de actividades
# 	sea d la constante de distancia maxima entre comisaria y centro de actividades
# 	sea fuente un nodo nuevo
# 	sea sumidero un nodo nuevo
	
# 	por cada tarea in m:
# 		auxiliar.crear_nodo(tarea)
# 		auxiliar.crear_arista(tarea,sumidero, 1)
# 	por cada comisaria in n:
# 		auxiliar.crear_nodo(comisaria)
# 		auxiliar.crear_arista(fuente,comisaria, 1)
# 		por cada actividad in m:
# 			if |distancia(comisaria,actividad)| < d:
# 				auxiliar.crear_arista(comisaria, actividad, 1)
				
		
	
# 	if FordFulkerson(auxiliar, fuente, sumidero) == cantidad de elemento de m:
# 		return True
# 	else:
# 		return False
		




#---------------------PARTE 2----------------------#


#Cómo modiﬁcaría la resolución del problema si en lugar de que cada centro de actividades i tenga que ser asignado a una sola comisaría,
# tenga que ser asignado a mi comisarías? 

#  modificacion1:
    #  total_custodias = 0
    #  por cada actividad in m:
    # 		sea mi la cantidad de comistarias custodiadas por actividad
    # 		total_custodias += mi
    # 		auxiliar.crear_nodo(tarea)
    # 		auxiliar.crear_arista(tarea,sumidero, mi)
    
#modificacion2:
    # if FordFulkerson(auxiliar, fuente, sumidero) == total_custodias:
	#	return True
 	# else:
    #	return False
# # 
# 



#---------------------PARTE 3----------------------#


# ¿Cómo modiﬁcaría la resolución del problema si además hubiera una
# restricción entre comisarías que implicaría que una comisaría Ni y una Nj no pudieran ser
# asignadas juntas a un centro Mi? ¿Para qué casos dejaría de ser eﬁciente la resolución?

#deberia crear una columna de nodos intermedio tal que si el centro Mi tiene comisarias que se restringen estas comisarias
#apunten al nodo itnermedio y este resuelva asignando solamente 1 de flujo a ese centro de actividades




# def solucion_parte2():
# 	sea auxiliar un grafo vacio
# 	sea n la lista de comisarias
# 	sea m la lista de centros de actividades
# 	sea d la constante de distancia maxima entre comisaria y centro de actividades
# 	sea fuente un nodo nuevo
# 	sea sumidero un nodo nuevo


	
# 	total_custodias =0 
# 	por cada actividad in m:
# 		sea mi la cantidad de comistarias custodiadas por actividad
# 		total_custodias += mi
# 		auxiliar.crear_nodo(tarea)
# 		auxiliar.crear_arista(tarea,sumidero, mi)
		
# 		sea r la lista de pares de comistarias restrictas en actividad
# 		para cada ni, nj de r en conflico:
# 			sea intermedio un nodo nuevo
# 			auxiliar.crear_nodo(intermedio)
# 			auxilicar.crear_arista(intermedio, actividad, 1)
# 			auxiliar.crear_arista(ni, intermedio, 1)
# 			auxiliar.crear_arista(nj, intermedio, 1)
		
# 	por cada comisaria in n:
# 		auxiliar.crear_nodo(comisaria)
# 		auxiliar.crear_arista(fuente,comisaria, 1)
# 		por cada actividad in m:
# 			if |distancia(comisaria,actividad)| < d:
# 				sea r la lista de pares de comistarias restrictas en actividad
# 				if comisaria not in r:
# 					auxiliar.crear_arista(comisaria, actividad, 1)
				
					
				
		
	
# 	if FordFulkerson(auxiliar, fuente, sumidero) == total_custodias:
# 		return True
# 	else:
# 		return False
		
		
					