# Una compañía minera nos pide que la ayudemos a analizar su nueva explotación. Ha
# realizado el estudio de suelos de diferentes vetas y porciones del subsuelo. Con estos datos
# se ha construido una regionalización del mismo. Cada región cuenta con un costo de
# procesamiento y una ganancia por extracción de metales preciosos. (En algunos casos el
# costo supera al beneﬁcio). Al ser un procesamiento en profundidad ciertas regiones
# requieren previamente procesar otras para acceder a ellas. La compañía nos solicita que le
# ayudemos a maximizar su ganancia, determinando cuales son las regiones que tiene que
# trabajar. Tener en cuenta que el costo y ganancia de cada región es un valor entero. Para
# cada región sabemos cuales son aquellas regiones que le preceden. Resolver el problema
# planteado utilizando una aproximación mediante ﬂujo de redes.


# def solucion(regiones):
#     sea grafo un grafo vacio
#     sea fuente un nodo nuevo
#     sea sumidero un nodo nuevo
#     grafo.agregar_nodo(fuente)
#     grafo.agregar_nodo(sumidero)
    
#     por cada r in region:
#         balance = r.ganancia() - r.costo()
#         sea predecesores las regiones predecesoras de r
        
#         if balance >=0:
#             grafo.agregar_arista(fuente, r, balance)
            
#         else:
#             grafo.agregar_arista(r, sumidero , -balance)
            
#         por cada pred predecesor a r distinto de fuente:
#             grafo.agregar_arista(pred, r, ∞)
         
         
#     flujo = FordFulkerson(grafo, fuente, sumidero) #mi grafo fue modificado por el residual
#     visitado = set()
#     pila = [fuente]

#     while pila:
#         u = pila.pop()
#         if u not in visitado:
#             visitado.add(u)
#             sea vecinos los nodos adyacentes a u
#             for v in vecinos:
#                 if grafo.capacidad_residual(u, v) > 0 and v not in visitado:
#                     pila.append(v)


#     return visitado