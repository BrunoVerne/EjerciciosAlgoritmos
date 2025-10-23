# La siguiente es una versión de Conjunto Independiente. Dado un grafo G= (V, E) y un
# entero k, decimos que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I, la
# arista (v, u) no pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas)
# de u a v. El problema de Conjuntos Fuertemente Independientes consiste en decidir si G
# tiene un conjunto fuertemente independiente de tamaño al menos k. Probar que el
# problema de Conjuntos Fuertemente Independientes es NP completo. Utilizar para ello que
# Conjuntos Independientes es NP completo. def solucion(G, k, S):
#     if |S| < k:
#         return False
    
#     for nodo in S:
#         if not nodo pertenece a G:
#             return False
        
#     for u in S:
#         for v in S , v != u:
#             if grafo.distancia_minima(u,v) <= 2:
#                 return False
    
#     return True
    
# demostracion(G):
#     sea G' una copia de G
#     por cada e in E:
#         sea u,v los nodos conectados por e
#         G´.borrar_arista(e)
#         G´.crear_nodo(auxiliar)
#         G´.crear_nodo(u)
#         G´.crear_nodo(v)
#         G´.crear_arista(u,auxiliar)
#         G´.crear_arista(auxiliar,v)
    
#     return G´
        

# Demostracion: Si tengo un grago G = (V,E) y creo un Grafo G' un conjunto S dado sea un conjunto independiente <==> S es un conjunto fuertemente conexto en G´
# porque al crear un nodo intermedio entre dos nodos "reales" de G y hacer que estos nodos intermedios formen un clique hará que para dos nodos reales de G que son independientes
# estos tendran en G´ una distancia de por lo menos 3 o sea > 2 o sea no tienen un nodo vecino en comun.