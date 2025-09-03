# A raíz de una nueva regulación industrial un fabricante debe rotular cada lote que
# produce según un valor numérico que lo caracteriza. Cada lote está conformado por “n”
# piezas. A cada una de ellas se le realiza una medición de volumen. La regulación considera
# que el lote es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el
# rótulo deberá ser ese valor. De lo contrario el lote se descarta. Actualmente cuenta con el
# proceso “A” que consiste en para cada pieza del lote contar cuántas de las restantes tienen el
# mismo volumen. Si alguna de las piezas corresponde al “elemento mayoritario”, lo rotula. De
# lo contrario lo rechaza. Un consultor informático impulsa una solución (proceso “B”) que
# considera la más eﬁciente: ordenar las piezas por volumen y con ello luego reducir el tiempo
# de búsqueda del elemento mayoritario. Nos contratan para construir una solución mejor
# (proceso “C”).

def procesoC(vector, inicio, fin):
    if inicio == fin:
        return vector[inicio]
    elif fin - inicio == 1:
        if vector[inicio] == vector[fin]:
            return vector[inicio]
        return None
    
    mitad = (inicio + fin) // 2
    candidato_izquierdo = procesoC(vector, inicio, mitad)
    candidato_derecho = procesoC(vector, mitad + 1, fin)
    
    if candidato_izquierdo is not None and chequearMayoria(candidato_izquierdo, vector, inicio, fin):
        return candidato_izquierdo
    
    if candidato_derecho is not None and chequearMayoria(candidato_derecho, vector, inicio, fin):
        return candidato_derecho
    
    return None

    
    

def chequearMayoria(elemento, vector, inicio , fin):
    contador = 0
    for i in range(inicio, fin+1):
        if vector[i] == elemento:
            contador +=1
    return contador > (fin - inicio + 1 ) // 2


if __name__ == "__main__":
    
    vector1 = [1, 2, 3, 4, 5]  
    print(procesoC(vector1, 0, len(vector1)-1))
    
    vector2 = [1, 1, 1, 2, 3] 
    print(procesoC(vector2, 0, len(vector2)-1))

    vector3 = [1, 1, 2, 2]     
    print(procesoC(vector3, 0, len(vector3)-1))

    vector4 = [1, 1, 1, 2, 2]  
    print(procesoC(vector4, 0, len(vector4)-1))
    
    vector5 = [9,8,9,6,9,4,9,9,1,9]  
    print(procesoC(vector5, 0, len(vector1)-1))

