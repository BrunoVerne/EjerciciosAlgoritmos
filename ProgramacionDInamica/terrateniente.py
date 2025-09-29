# El dueño de una cosechadora está teniendo una demanda muy elevada en los próximos 7
# meses. Desde “n” campos lo quieren contratar para que preste sus servicios.
#Lamentablemente no puede hacer todos los contratos puesto que varios de ellos se
# superponen en sus tiempos. Cuenta con un listado de los pedidos donde para cada uno de
# ellos se consigna: fecha de inicio, fecha de ﬁnalización, monto a ganar por realizarlo. Su idea
# es seleccionar la mayor cantidad de trabajos posibles. Mostrarle que esta solución puede no
# ser la óptima. Proponer una solución utilizando programación dinámica que nos otorgue el
# resultado óptimo (que trabajos elegir y cuanto se puede ganar).



def terrateniente(contratos):
    """

    Args:
        sea n un array de contratos tal que cada campo lleva la siguiente forma: inicio, fin, monto
        OPT[i] = max(elegir i, no elegir i)
    """
    contratos = sorted(contratos, key= lambda x: x[1]) # ordenados segun fecha de finalizacion ascendente
    n = len(contratos)
    OPT = [0] * (n+1)
    seleccionados = [0] * (n+1)
    OPT[0] = 0
    
    for i in range(1,n+1):
        anterior_valido = 0
        for j in range(i):
            if contratos[j-1][1] <= contratos[i-1][0]:
                anterior_valido = j
        
        monto_a_ganar = contratos[i-1][2]
        OPT[i] = max(OPT[i-1], OPT[anterior_valido] + monto_a_ganar)
        if OPT[i] == OPT[anterior_valido] + monto_a_ganar:
            seleccionados[i] = 1
        
    
    i = n
    solucion = []
    while i >=0:
        if seleccionados[i] == 1:
            solucion.append(contratos[i-1])
            j = i-1
            superpone = True
            while j > 0 and superpone:
                if contratos[j-1][1] < contratos[i-1][0]:
                    superpone = False
                j -= 1
            i = j
        else:
            i -= 1
    
    return OPT[n], solucion[::-1]
                
    
if __name__ == "__main__":
    contratos = [[1,2,10],[1.5,2,500],[4,5,10],[4.5,7,100]]
    print(terrateniente(contratos))
    
    contratos2 = [[1, 3, 50], [3, 5, 10], [5, 7, 10],[1, 7, 120]]
    print(terrateniente(contratos2))



#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.