# Problema del camino más largo en un grafo general con aristas sin peso: Dados G = (V, E)
# un grafo no dirigido y un natural k, determinar si existe un camino simple en G de longitud
# >=k. Probar que es un problema NP-completo (Usar el problema del camino hamiltoniano
# para probarlo).




# def solucion(G, k, certificado): # certificado es un camino o sea una lista de nodos
#     visitados = []
#     for nodo in C O(certificado)
#         if not nodo pertenece a G O(1)
#             return false

#         if nodo esta en visitados: 
#             return false
        
#         visitados.agregar(nodo)
    
#     if |visitados| < k: O(1)
#         return false
    
#     for i = 1 hasta |certificado| - 1: O(certificado)
#         if not existe_arista(G, certificado[i], certificado[i+1]) O(E)
#             return false
    
#     return true
    
    
#Total: 0(C*E)
# Demostracion:Podemos ver a Camino Hamiltoniano como una instancia particular del Camino Mas Largo donde K = |V| - 1 (el -1 porque CML repite inicio y 
# fin y CH no).
#=>  Existe Camino Hamiltoniano para un grafo G = (V,E) <--> Existe resultado = CaminoMaslargo(G) | resultado = |V| - 1 (CML ES NP HARD)
#por lo tanto Ciclo Hamiltoniano <=p Camino mas Largo. Camino mas largo es NP Completo