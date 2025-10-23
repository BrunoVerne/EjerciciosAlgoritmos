# La red ARPANET, antecesora de internet, se creó para seguir funcionando incluso ante
# fallas en parte de su red. El país “Atrasoñia” - que se mantuvo cerrado a los avances
# tecnológicos de las últimas décadas - ha decidido construir su propia red de redes. Han leído
# la documentación desclasiﬁcada de ARPANET y se han instruido en conectividad de redes.
# Proponen una red informática para unir sus principales organismos estatales. Nos convocan
# para que validemos su diseño. Debemos responder: ¿Cuántos cables de datos de la red se
# tienen que romper antes que la conectividad del grafo se rompa? (tener en cuenta que los
# cables de datos son bidireccionales) ¿Cuántos nodos se tienen que romper antes que el
# grafo restante deje de ser conexo? (Sugerencia: piense en transformar de alguna forma los
# nodos para resolverlo mediante lo creado en el punto a)


#o sea ver la cantidad de aristas que puedo romper hasta perder la conectividad del grafo o sea que 1 o mas nodos queden aislados del grafo o sea
#que no haya camino posible para i-ésimo nodo del grafo. Seguro tenga que usar Ford Fulkerson pero como carajo relaciono esta resolucion con F-F?

                                # ------------------------SOLUCION------------------------#

# defino FordFulkerson(grafo, fuente, sumidero) el algoritmo de Ford FUlkerson con parametros el grafo el nodo fuente y el nodo sumidero
# def solucion_A(grafo):
# 	minimo_global = ∞
# 	por cada u,v pares del nodo del grafo:
# 		sea auxiliar un grafo vacio
# 		auxiliar = grafo 
# 		por cada arista ar in auxiliar:
# 			ar.peso_arista(1)
# 		minimo_local = FordFulkerson(auxiliar, u, v)
# 		si minimo_local < minimo_global:
# 			minimo_global = minimo_local 

# 	return minimo_global


# def solucion_B(grafo):
# 	minimo_global = ∞
# 	por cada n1,n2 pares del nodo del grafo:
# 		auxiliar = un grafo vacio 
# 		fuente = n1
# 		sumidero = n2
		
# 		por cada n nodo in grafo:
# 			si n == fuente || n == sumidero:
# 				auxiliar.agregar_nodo(n)
			
# 			else:
# 				sea n_entrada nodo nuevo
# 				sea n_salida nodo nuevo
# 				auxiliar.agregar_nodo(n_entrada)
# 				auxiliar.agregar_nodo(n_salida)
# 				auxiliar.crear_arista(n_entrada, n_salida, 1)
# 				auxiliar.crear_arista(n_salida, n_entrada, 1)
				
# 			por cada ady adyacente a n:
# 				si no existe arista (n_salida , adyacente) en auxiliar:
# 					auxiliar.crear_arista(n_salida, adyacente, ∞)
# 					auxiliar.crear_arista(adyacente, n_salida, ∞)               #hago de un grafo no dirigido uno sí dirigido haciendolo bidireccional
		
		
		
# 		minimo_local = FordFulkerson(auxiliar, fuente, sumidero)
		
# 		if minimo_Local < minimo_global:
# 			minimo_global = minimo_local
	
# 	return minimo_global
				