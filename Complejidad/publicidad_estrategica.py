# Una agencia de marketing coloca publicidad en la Web. Se han ilusionado con vender
# publicidad con la siguiente idea, que llamaremos el problema de la Publicidad Estratégica:
# Un sitio Web se puede modelar como un grafo G = (V, E). Las acciones habituales de los
# usuarios que visitan un sitio se pueden modelar mediante “t” recorridos posibles P1, P2, ... , Pt
# (donde cada Pi es un camino dirigido en G). Dado un número k, se quieren elegir a lo sumo k
# vértices en G para poner publicidad, de modo tal que todos los “t” recorridos habituales
# pasen por al menos uno de esos vértices. Tenemos que mostrarle a esta empresa que su
# idea no es realizable por el momento ya que el problema de la Publicidad Estratégica es
# NP-completo. Sugerencia: relacionarlo con cubrimiento de vértices.


# demuestro que publicidad estratégica pertenece a NP
# def solucion(G, K, S, T):
#     if |S| > K:
#         return False
    
#     for nodo in S: 
#         if not nodo pertenece a V: O(S * V)
#             return False
            
    
#     for Pi in T:
#         recorre = False
#         for nodo in S: 
#             if nodo pertenece a Pi: O(S*T*(V+E))
#                 recorre = True
        
#         if not recorre:
#             return False
    
#     return True
    
# TOTAL= O(S*T*(V+E))

# Ahora paso a demostrar que Publicidad Estrategica pertenece a NP Hard.
# Existira una solución con Vertex Cover dado un grafo G=(V,E) y un natural K <==> existe una solucion con Publicidad Estratégica con G,K, y T siendo T cada arista del recorrido o sea T contiene todas las aristas del Grafo.
# Representación: Vertex Cover(G,k)----> transformacion ---> Publicidad Estrategica(G,K,T) ---> T/F Publicidad estrategica == T/F Vertex Cover
# Defino

# Transformacion(G', K):

#     G = G'                         
#     T = []                        

#     para cada arista (u, v) en E':
#         agregar [u, v] a T          // cada arista se vuelve un recorrido de 2 vértices

#     devolver (G, T, K)
            
    