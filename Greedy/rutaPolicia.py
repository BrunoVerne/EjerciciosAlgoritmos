#Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado
#(ordenado por nombre del pueblo) contiene el número de kilómetros donde está ubicada
#cada una. Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de
#tal forma que no haya bifurcaciones con vigilancia a más de 50 km. Proponer un algoritmo
#que lo resuelva.
lista=[0, 51, 102]
radio = 50

    
def minimizarPolicias(distanciasPueblos, radioPatrulla):
    posicionPatrullas = []
    distanciasPueblos = sorted(distanciasPueblos)
    n = len(distanciasPueblos)
    
    if n == 0:
        return posicionPatrullas 
    
    minima = distanciasPueblos[0]
    
    for i in range(1, n):
        if distanciasPueblos[i] - minima > 2 * radioPatrulla:
            posicionPatrullas.append(minima + radioPatrulla)
            minima = distanciasPueblos[i]
    

    posicionPatrullas.append(minima + radioPatrulla)
    
    return posicionPatrullas



def main():
    resultado = minimizarPolicias(lista, radio)
    print(resultado)
    

# Ejecutar el programa
if __name__ == "__main__":
    main()
