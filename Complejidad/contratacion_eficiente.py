# Nos piden que organicemos una jornada de apoyo de estudio para exámenes. Tenemos
# que poder dar apoyo a “n” materias y hemos recibido currículos de “m” postulantes para ser
# potenciales ayudantes. Cada ayudante puede ayudar en un determinado subconjunto de
# materias. Para cada una de las materias hay un subconjunto de postulantes que pueden dar
# apoyo en ella. La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo “k”
# ayudantes de modo tal que siempre haya un ayudante que pueda dar consultas en alguna
# de las n materias? Este problema se llama Contratación Eﬁciente. Probar que “Contratación
# Eﬁciente” es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices.
        

    

# def certificador(m,n,K,S):
# 	if |S| > K:
# 		return False
	
# 	n´ = copia de n
# 	for elegido in S:							 O(S)
# 		if elegido not in m:
# 			return False
			
# 		sea subconjunto el subconjunto de materias del elegido
# 		for materia in subconjunto:					 O(n)
# 			if materia in n´
# 			n´.sacar(materia)
# 	if |n´| > 0:
# 		return False
	
# 	return True

# O(S + n)

# def transformacion(G,k):
# 	Sea G un grafo bipartito tal que los nodos "ayudantes" apuntan a sus respectivos nodos "materias"
# 	ayudantes, materias = dividir_bipartito(G)
# 	subconjuntos = {}
	
# 	for ayudante in ayudantes:
# 		subconjunto = grafo.adyacentes(ayudante)
# 		subconjuntos[ayudante] = subconjunto
	
# 	return ayudantes, materias, subconjuntos
	

# Demostracion:
#  Si S ⊆ V es vertex cover en G:

# ∀ arista e = (u,v) ∈ E, al menos uno de {u,v} ∈ S

# En la instancia transformada: cada materia (arista) es cubierta por al menos un ayudante (vértice) en S

# ∴ S cubre todas las materias

# (⇐) Si S ⊆ ayudantes cubre todas las materias:

# ∀ materia (arista) e ∈ E, ∃ ayudante v ∈ S que cubre e

# Esto significa que ∀ arista e = (u,v), al menos uno de {u,v} ∈ S

# ∴ S es vertex cover en G


# Representación: Vertex Cover(G,k) --> Transformacion(G,k)--> resolvedor Contratacion Eficiente(ayudantes, materias, subconjuntos) --> resultado C-E --> resultado Vertex Cover
# por lo tanto con el certificador vemos que C-E es NP y con la transformaciones desde Vertex Cover vemos que Vertex Cover <=p C-E entonces C-E es NP y NP Hard por lo tanto podemos decir que C-E es NP COMPLETO		
		
	

		
		
    
    