# Un fabricante de perfumes está intentando crear una nueva fragancia. Y desea que la
# misma sea del menor costo posible. El perfumista le indicó un listado de ingredientes. Por
# cada uno de ellos determinó una cantidad mínima (puede ser cero) y una máxima que debe
# contar en la fórmula ﬁnal. Cada ingrediente tiene asociado un costo por milímetros cúbicos.
# Sabiendo que en la presentación ﬁnal es de X milímetros cúbicos. Presentar una solución
# utilizando metodología greedy que resuelva el problema.


def perfume(ingredientes, X):
    ordenados = merge(ingredientes)
    solucion = {}
    volumen_actual = 0
    for i in range(len(ordenados)):
        volumen_futuro_minimo = 0
        for j in range(i+1, len(ordenados)):
            volumen_futuro_minimo += ordenados[j].cantidad_minima
        
        volumenposible = X - volumen_actual - volumen_futuro_minimo
        
    
        if(ordenados[i].cantidad_maxima > volumenposible):
            solucion[ordenados[i]] = volumenposible
            volumen_actual += volumenposible
        else:
            
            solucion[ordenados[i]] = ordenados[i].cantidad_maxima
            volumen_actual += ordenados[i].cantidad_maxima
            
            
    for i in range(len(ordenados)):  # verifico que se cumplieron todos los minimos
        if solucion[ordenados[i]] < ordenados[i].cantidad_minima:
            return None
            
    if volumen_actual == X:
        return solucion
    return None
    
    
                    ##----------------------- esto es O(n²) es optimo pero no eficiente-----------------------##


def perfume2(ingredientes, X):
    ordenados = merge(ingredientes)
    solucion = {}
    volumen_actual = 0
    
    minimo_futuro = [0] * (len(ordenados) + 1)  #creo array
    minimo_futuro[len(ordenados)] = 0  # Caso base para que cuando hago i + 1 no tenga out of index error
    
    
    
    for i in range(len(ordenados)-1, -1, -1):  # Desde el penúltimo hasta el primero
        minimo_futuro[i] = minimo_futuro[i+1] + ordenados[i].cantidad_minima
        
    for i in range(len(ordenados)):
        
        volumen_posible = X - volumen_actual - minimo_futuro[i+1] #aca funciona el caso base para cuando miro el ultimo elemento
        
        if(ordenados[i].cantidad_maxima > volumen_posible):
            solucion[ordenados[i]] = volumen_posible
            volumen_actual += volumen_posible
        else:
            
            solucion[ordenados[i]] = ordenados[i].cantidad_maxima
            volumen_actual += ordenados[i].cantidad_maxima
            
            
    for i in range(len(ordenados)):  
        if solucion[ordenados[i]] < ordenados[i].cantidad_minima:
            return None
            
    if volumen_actual == X:
        return solucion
    return None
    
def merge(ingredientes):
    ordenados = []
    longitud = len(ingredientes) 
    if longitud == 1:
        return ingredientes
    
    mitad = longitud // 2 
    izquierdo = merge(ingredientes[:mitad])
    derecho = merge(ingredientes[mitad:])
    
    i=0
    j=0
    while i < len(izquierdo) and j < len(derecho):
        
        if izquierdo[i].costo < derecho[j].costo:
            ordenados.append(izquierdo[i])
            i +=1
        
        elif derecho[j].costo < izquierdo[i].costo:
            ordenados.append(derecho[j])
            j +=1
        
        else:
            ordenados.append(izquierdo[i])
            ordenados.append(derecho[j])
            i +=1
            j +=1
            
    
    while i < len(izquierdo):
        ordenados.append(izquierdo[i])
        i +=1
        
    while j < len(derecho):
        ordenados.append(derecho[j])
        j +=1
        
    return ordenados


#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.