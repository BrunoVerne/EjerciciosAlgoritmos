# Un ramal ferroviaria pone en concesión los patios de comida en todas las estaciones. Son
# en total “n” estaciones. Por cada estación se cuenta con el promedio de facturación de los
# últimos 5 años. Por normativa antimonopólica existe como limitante que ninguna empresa
# puede explotar 3 o más estaciones contiguas. Pero, no existe una cantidad máxima de
# estaciones a explotar. Un oferente nos solicita que le digamos cuales son las estaciones que
# le conviene obtener para maximizar sus ganancias. Plantee la solución mediante
# programación dinámica.



# opt[0]= primer elemento
#opt[i] = max(opt[i-1], opt[anterior_valido] + Gi) y el anterior valido es lo que hay que pensar, 
#si i - 1 fue elegido E i - 2 no fue elegido => anterior_valido = i - 1
# si i - 1 fue elegido E i - 2 fue elegio => anterior valido = i - 3
# si i - 1  no fue elegido E i - 2 fue elegido => anterio valido = i - 1
# si 1 - 1 no fue elegido E i - 2 tampoco fue elegido => anterior valido = i - 1


# se resume a:
# si i - 1 fue elegido E i - 2 fue elegio => anterior valido = i - 3
#sino anterior_valido = i - 1

#lista tiene elementos del tipo = (numero, facturacion)
def ferroviarios(ferroviarios):
    n = len(ferroviarios)
    ferroviarios = sorted(ferroviarios, key=lambda x: x[0])
    OPT = [0] * (1 + n )
    OPT[0] = 0
    OPT[1] = ferroviarios[0][1] 
    seleccionados = [False] * n
    seleccionados[0] = True
    for i in range(2,len(ferroviarios) + 1):
        ganancia_actual = ferroviarios[i-1][1]
        opcion_1 = OPT[i-1] #no elijo el actual
        opcion_2 = OPT[i-2] + ganancia_actual # no elijo el anterior 
        opcion_3 = OPT[i-3] + ferroviarios[i-2][1] +  ferroviarios[i-1][1] if i>=3 else 0
        OPT[i] = max(opcion_1,opcion_2,opcion_3)
        

    i = n
    while i > 0:
        if OPT[i] == OPT[i-1]: # no elegi el elemento i
            i -= 1
        elif OPT[i] == OPT[i-2] + ferroviarios[i-1][1]: #eleji i y chance de que haya elegido i - 2
            seleccionados[i-1] = True #  i = true
            i -= 2
        else:   # caso 3 que elegi i - 1 e i
            seleccionados[i-1] = True # i = True
            seleccionados[i-2] = True # i - 1 = True
            i -= 3
    
    return OPT[n], seleccionados    
    
    
    
        
def main():
    lista1 = [(1, 5), (2, 6), (3, 4), (4, 11), (5, 7)]
    lista2 = [(1, 10), (2, 5), (3, 20), (4, 15)]
    lista3 = [(1, 3), (2, 2), (3, 5), (4, 10), (5, 7), (6, 8)]
    lista4 = [(1, 1), (2, 100), (3, 1), (4, 100), (5, 1)]
    lista5 = [(1, 8), (2, 9), (3, 10), (4, 1), (5, 2), (6, 3)]

    print(ferroviarios(lista1))
    print(ferroviarios(lista2))
    print(ferroviarios(lista3))
    print(ferroviarios(lista4))
    print(ferroviarios(lista5))


if __name__ == "__main__":
    main()
    


#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.