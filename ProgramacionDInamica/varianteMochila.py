# Considere la siguiente variante del problema de la mochila. Contamos con un conjunto
# ordenado de “n” productos numerados del 1 al “n”. Cada producto i tiene asociado un peso
# pi y un valor vi. Queremos seleccionar un subconjunto de elementos logrando que la suma
# de sus valores sea la máxima posible y sin superar K entre la suma de los pesos de los
# elementos seleccionados. Además se restringe la selección de 2 productos con numeración
# consecutiva.

# OPT[i] = si antes no se sumo elemento a la mochila: max(OPT[i-1], OPT[i - Pi] + Vi ) o sea decido si incluirlo en la mochila 
#          si antes sí se sumo elemento a la mochila: OPT[i-1]


def varianteMochila(productos, K):
    OPT = [0] * (K+1)
    OPT[0] = 0

    for i in range(1,K+1):
        max_local = -1
        aux = -1
        indice_anterior = -1
        for j in range(len(productos)):
            vi,pi = productos[j]
            if OPT[i-1] == OPT[i-1-pi] + vi:
                indice_anterior = j
        
        for i2 in range(len(productos)):
            vi,pi = productos[i2]
            if i >= pi and i2 != indice_anterior:
                ganancia_actual = OPT[i-pi] + vi
                if ganancia_actual > max_local:
                    max_local = ganancia_actual
                    aux = i2
        
        OPT[i] = max(OPT[i-1], max_local)
        
            
    i = K
    seleccionados = []
    while i > 0:
        for vi, pi in productos:
            if OPT[i] == OPT[i-pi] + vi:
                seleccionados.append((vi,pi))
                i -= pi
    
    return OPT[K], seleccionados
        
        

if __name__ == "__main__":
    productos1 = [(10, 1), (20, 2), (15, 1)]
    K1 = 3
    print(varianteMochila(productos1,K1))
# Esperado: (45, [(15,1), (15,1), (15,1)])


    productos2 = [(10, 1), (5, 1), (20, 2)]
    K2 = 4  
    print(varianteMochila(productos2,K2))    
# Esperado: (40, [(20,2), (20,2)])    


    productos3 = [(1, 1), (2, 2), (120, 3)]
    K3 = 10
    print(varianteMochila(productos3,K3))
# Esperado: (361, [(1,1), (120,3), (120,3), (120,3)])
   

        
        
#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.
