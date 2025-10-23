# Una agencia de marketing coloca publicidad en la Web. Se han ilusionado con vender
# publicidad con la siguiente idea, que llamaremos el problema de la Publicidad Estratégica:
# Un sitio Web se puede modelar como un grafo G = (V, E). Las acciones habituales de los
# usuarios que visitan un sitio se pueden modelar mediante “t” recorridos posibles P1, P2, ... , Pt
# (donde cada Pi es un camino dirigido en G). Dado un número k, se quieren elegir a lo sumo k
# Un almacén registra en una matriz qué productos compra cada uno de sus clientes. Un
# conjunto de clientes es diverso si cada uno de ellos compra cosas diferentes (tiene
# intersección vacía con lo que compran los demás). Deﬁnimos al problema de los clientes
# diversos como: Dada una matriz de registro, de tamaño m (clientes) x n (productos), y un
# número k<=m, ¿existe un subconjunto de tamaño al menos k de los clientes que sea diverso?
# Probar que el problema es NP-completo. Sugerencia: Reducir polinomialmente conjuntos
# independientes a clientes diversos.


# def solucion(registro,K,S)
#     |registro| = m
#     if |S| > m: 
#         return False
    
#     if |S| < K:
#         return False
    
#     visitados = []
#     for indice_elegido in S:                    O(S)
#         if indice_elegido >= m:
#             return False
#         productos = registro[indice_elegido]
#         for producto in productos:              O(n)
#             if producto in visitados:
#                 return false
#             visitados.agregar(producto)
        
        
# Total = O(S*n)

# def transformacion(G):
#     clientes, productos = dividir_bipartito(G)
#     m = |clientes|
#     n = |productos|
#     registro = matriz de m x n inicializada en 0
#     for cliente in clientes:
#         sea i el indice del cliente
#         for elegido in grafo.adyacentes(cliente)
#             sea j el indice del elegido
#             registro[i][j] = producto
#     return registro
    

    

# demostracion de CLientes diversos es NP Hard
# Podemos ver a la matriz de clientes x productos como un grafo bipartito que tiene de un lado clientes y del otro productos de tal manera que los clientes y sus productos elegidos
# estan conectados por una arista y los clientes entre si no tienen arista ninguna entre ellos. Entonces podré saber que la lista de clientes diversos es correcta si y solo si ese subconjunto de clientes es un conjunto independiente del grafo ya que si alguno de los clientes comparten algun producto ese producto representado en el grafo como un nodo tendra arista de dos nodos que son del subconjunto por lo tanto ese nodo producto será vecino tanto de un cliente como del otro entonces no es un subconjunto válido

# Representacion: Instancia de Conjunto Independiente (G,k)
#         ↓
# transformación_polinomial (esta es la reducción)
#         ↓
# Instancia de Clientes Diversos (matriz, k)
#         ↓
# Si tuviera un resolvedor para Clientes Diversos
#         ↓
# Resultado de Clientes Diversos
#         ↓
# transformación_inversa
#         ↓  
# Resultado de Conjunto Independiente
    
        
        

    
    
    