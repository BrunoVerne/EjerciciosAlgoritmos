# Una variante del problema de la mochila corresponde a la posibilidad de incluir una
# cantidad ilimitada de cada uno de los elementos disponibles. En ese caso, tenemos una
# mochila de tamaño “k” y un conjunto de “n” elementos con stock ilimitado. Cada elemento
# tiene un peso y un costo. Queremos seleccionar el subconjunto de elementos que maximice
# la ganancia de la mochila sin superar su capacidad. Solucione el problema utilizando
# programación dinámica.

# OPT[i] = mayor cantidad posible de valor que puedo poner en el i-ésimo peso
# OPT[i] = max(OPT[i-j] +  Gj) para todo j,Gj perteneciente a los n elementos
# siendo j peso de los n elemento y Gj su ganancia 

def mochila2(total, elementos):
    OPT = [0] * (total+1)
    OPT[0] = 0
    for i in range(total+1):
        for j, Gj in elementos:
            if i >=j:
                nuevaGanancia = OPT[i-j] + Gj 
                if nuevaGanancia > OPT[i]:
                    OPT[i] = nuevaGanancia
    
    return OPT[total]
                    


if __name__ == "__main__":
    total = 40
    elementos = [[10,1],[20,100],[5,1]]
    print(mochila2(total, elementos))
    
    

#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.