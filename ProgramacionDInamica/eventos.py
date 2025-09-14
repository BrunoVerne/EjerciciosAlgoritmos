# La organización de una feria internacional tiene que programar diferentes eventos a
# realizar en su escenario principal. Para ello pueden elegir, en los diferentes días del evento,
# entre alguno de los siguientes rubros: un cantante, una compañía de danza, un show de
# variedades o un humorista. Disponen de una oferta de cada tipo para cada día y la posible
# ganancia por venta de entradas. Existen ciertas restricciones que se aplican. No se pueden
# repetir 2 días seguidos el mismo rubro. Además por el tiempo de preparación un día
# después de un cantante solo puede presentarse un humorista. Plantear la resolución
# mediante programación dinámica.

# elemento actividades[0][1] es la primera actividad el segundo dia  y tiene un valor de  ganancia Gi
# defino orden 0 = cantante 1 = danza 2 = variedades 3 = humorista
def eventos(actividades):
    n = len(actividades)
    m = len(actividades[0])
    
    OPT = []
    for i in range(n):
        fila = [0] * m
        OPT.append(fila)
    
    for j in range(m):
        OPT[0][j] = actividades[0][j]
        
    for i in range(1,n):
        for j in range(m): #actividades actuales representadas en j
            maximo_anterior = float("-inf") #representa un -infinito
            for k in range(m): #recorro las actividades anteriores representadas en k
                if j == k:
                    continue # no se puede repetir lo del dia pasado
                elif k == 0 and j !=3:
                    continue
                
                maximo_anterior = max(maximo_anterior, OPT[i-1][k])
                
            if maximo_anterior != float("-inf"):
                OPT[i][j] = actividades[i][j] + maximo_anterior
            else:
                OPT[i][j] = actividades[i][j]
    
    return max(OPT[n-1])                    




if __name__ == "__main__":
    # 4 días, 4 actividades: [cantante, danza, variedades, humorista]
    ganancias = [
        [100, 80, 90, 70],   # Día 1
        [120, 85, 95, 75],   # Día 2  
        [110, 90, 100, 80],  # Día 3
        [130, 95, 105, 85]   # Día 4
    ]
    
    resultado = eventos(ganancias)
    print(f"Máxima ganancia posible: {resultado}")