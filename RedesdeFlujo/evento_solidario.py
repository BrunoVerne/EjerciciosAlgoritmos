# Para un evento solidario un conjunto de n personas se ofrecieron a colaborar. En el
# evento hay m tareas a desarrollar. Cada tarea tiene un cupo máximo de personas que la
# puede realizar. A su vez cada persona tiene ciertas habilidades que la hacen adecuadas para
# un subconjunto de tareas. Proponga una solución mediante red de ﬂujos que maximice la
# cantidad de personas asignadas a las tareas. 



# def solucion_parte1():
# 	sea auxiliar un grafo vacio
# 	sea n la lista de personas
# 	sea m la lista de tareas a realizar
# 	sea fuente un nodo nuevo
# 	sea sumidero un nodo nuevo
# 	auxiliar.agregar_nodo(fuente)
# 	auxiliar.agregar_nodo(sumidero)
	
# 	por cada tarea in m:
# 		auxiliar.agregar_nodo(tarea)
		
# 		sea max el cupo maximo de personas que puede realizar tarea
# 		auxiliar.agregar_arista(tarea,sumidero, max)
	
# 	por cada persona in n:
# 		auxiliar.agregar_nodo(n)
# 		auxiliar.agrear_arista(fuente, n, ∞)
		
# 		sea posibles el subgrupo de tareas realizables por persona
# 		por cada tarea in posibles:
# 			auxiliar.agregar_arista(n, tarea, 1)
		
	
# 	return FordFulkerson(auxiliar, fuente, sumidero) 




#¿Hay forma de lograr asegurarnos un piso
# mínimo de personas en cada tarea? ¿Cómo impacta en la solución presentada en el punto anterior?

#Restringiendo las aristas desde las tareas al sumidero con ese nuimero piso que queremos,
#no lo pude hacer aún