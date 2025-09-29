# Una encuesta de internet pidió a personas que ordenen un conjunto de “n” películas
# comenzando por las que más les gusta a las que menos. Con los resultados quieren
# encontrar quienes comparten gustos entre sí. Nos solicitan generar un algoritmo, que
# basándose en el concepto de inversión, compare entre pares de personas y determine qué
# tan compatibles o incompatibles son. Proponer un algoritmo utilizando división y conquista
# que lo resuelva.


# caso base cuando llego a dos personas ahi empiezo a hacer el conteo de inversiones, puedo modularizarlo en una primera etapa de llegar al
#caso base y una segunda de conteo de inversiones es un conteo entre dos listas
def compatibilidad(peliculas):
    n = len(peliculas)
    resultados = [[0] * n for _ in range(n)]
    dycPeliculas(peliculas, 0, n-1, resultados)
    return "\n".join(
        "\t".join(f"{x:3}" for x in fila)
        for fila in resultados
    )

def dycPeliculas(peliculas, inicio, fin, resultados):
    if inicio >= fin:
        return
    elif fin - inicio == 1:
        resultados[inicio][fin] = contarInversiones(peliculas[inicio], peliculas[fin])
        resultados[fin][inicio] = resultados[inicio][fin] 
        return
    
    else:
        mitad = (fin + inicio) //2
        dycPeliculas(peliculas, inicio, mitad, resultados)
        dycPeliculas(peliculas, mitad + 1, fin, resultados) 
        
    
    for i in range(inicio, mitad+1):
        for j in range(mitad+1, fin+1):
            resultados[i][j] = contarInversiones(peliculas[i], peliculas[j])
            resultados[j][i] = resultados[i][j]

    return resultados

def contarInversiones(l1, l2):
    orden = {}
    contador = 0
    n = len(l1)
    ordenL1 = []
    for i in range(n):
        orden[l1[i]] = i
        ordenL1.append(i)
    
    ordenL2= []
    for i in range(n):
        ordenL2.append(orden[l2[i]])
    
    for i in range(n):
        for j in range(i + 1, n):
            if ordenL2[i] > ordenL2[j]:
                contador += 1
    
    return contador
        
        
if __name__ == "__main__":
    peliculas = [["A","B","C","D"], ["D", "C", "B","A"],["D", "A", "B","C"],["B", "A", "D","C"]]
    print(compatibilidad(peliculas))