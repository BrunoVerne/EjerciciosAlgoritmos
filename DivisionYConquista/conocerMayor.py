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

def procesoC(vector):
    if len(vector) == 1:
        return vector[0]
    elif len(vector) == 2:
        if vector[0] == vector[1]:
            return vector[0]
        return None
    vector2 = []
    i = 0
    while i < len(vector) // 2 + 1:
        if vector[i] == vector[i+1]:
            vector2.append(vector[i])
            vector2.append(vector[i+1])

        i +=2
          
        
    if i == len(vector) -1:
        vector2.append(vector[i])
    
    if len(vector2) == 0:
        return None
    
    if(len(vector2) == len(vector)):
        return vector2[0]

    
    candidato = procesoC(vector2)
    
    if candidato is None:
        return None
    
    apariciones = 0
    for v in vector:
        if v == candidato:
            apariciones +=1
    
    if(apariciones > len(vector) // 2):
        return "resultado: ", candidato, "apariciones: ", apariciones
    return None
    

if __name__ == "__main__":
    print(procesoC([1,1,2,1,3,1,1])) #1 aparece 5 veces  
    print(procesoC([2,2,3,3,4,4]))  # None
    print(procesoC([1,1,1,2,3]))       #1 aparece 3 veces
    print(procesoC([5,5,5,5,2,3,5]))  # 5 aparece 5 veces
    print(procesoC([9,8,9,9,7,9,6,9,9]))  #9 aparece 6 veces
    print(procesoC([1,2,3,4,5])) #None
    print(procesoC([1,1,1,1,1])) #1 aparece 5 veces (este me da mal )
    print(procesoC([1,2,1,2,1])) # 1 aparece 3 veces
