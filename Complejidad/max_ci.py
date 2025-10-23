# Nos brindan una caja negra A que, dado un grafo no dirigido G = (V, E) y un número k se
# comporta de la siguiente manera:
# ○ Si G es no conexo devuelve “no conexo”.
# ○ Si G es conexo y tiene un conjunto independiente de tamaño al menos k devuelve
# “Sí”.
# ○ Si G es conexo y no tiene un conjunto independiente de tamaño al menos k devuelve
# “No”.
# Mostrar cómo podríamos resolver el problema del máximo conjunto independiente en
# tiempo polinomial, usando llamadas a A si suponemos que A corre en tiempo polinomial en
# el tamaño de G y k. Describir la solución. ¿Tiene sentido la hipótesis de que A corre en
# tiempo polinomial en el tamaño de G y k? ¿Por qué?




# max_conjunto_independiente(G):
#     sea V los nodos de G
#     for i = |V| to 0:  #O(V*A)
#         if A(g,i) == "Si":
#             return i
#     return 0

# solucion(G,k):

#     if A(g,1) == "no conexo":
#         componentes[] = componentes_conexas(G)  # O(V) 
#         contador = 0
#         for componente in componentes:
#             contador += max_conjunto_independiente(componente)
#             return contador >= k
#     return max_conjunto_independiente(G) >= k
    
    
            
#Total: O(V²*A)

#Resolucion: Conjunto independiente -> NP COMPLETO 
#            Maximo conjunto independiente -> NP - H
#           Conjunto Independiente <=p max conjunto independiente 
#           MAXIMO CONJUNTO INDEPENDIENTE ES NP COMPLETO