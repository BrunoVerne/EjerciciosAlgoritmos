# Contamos con una carretera de longitud M km que tiene distribuidos varios carteles
# publicitarios. Cada cartel ”i” está ubicado en un “ki” kilómetro determinado (pueden ubicarse
# en cualquier posición o fracción de kilómetro) y a quien lo utiliza le asegura una ganancia
# “gi”. Por una regulación no se puede contratar más de 1 cartel a 5km de otros. Queremos
# determinar qué carteles conviene contratar de tal forma de maximizar la ganancia a obtener.

# ej: lista = [(1,5), (17,6), (19,2)] etc uno es el kilometro el segundo elementod e los vectores es su ganancia y esta ordenada segun kilometros asc
def carteles(kilometros):
    kilometros = sorted(kilometros, key=lambda x: x[0])
    seleccionados = [0] * len(kilometros)
    OPT = [0] * (len(kilometros) + 1)
    OPT[0] = 0
    OPT[1]= kilometros[0][1]
    indice_minimo = 0
    seleccionados[0] = 1
    for i in range(2, len(kilometros)):
        ultimo_valido = anterior_valido(kilometros,i,indice_minimo)
        OPT[i] = max(OPT[i-1], OPT[ultimo_valido] + kilometros[i-1][1])
        
        if OPT[i] == OPT[ultimo_valido] + kilometros[i-1][1]:
            seleccionados[i] = 1
            indice_minimo = ultimo_valido
    
    return mostrar_seleccionados(seleccionados, kilometros)
    

def anterior_valido(kilometros, indice, indice_minimo):
    anterior = 0
    kilometro = kilometros[indice-1][0]
    for i in range(indice_minimo,indice):
        if kilometros[i][0] + 5 <= kilometro:
            anterior = i + 1
    return anterior


def mostrar_seleccionados(seleccionados, kilometros):
    resultado = [0] * len(seleccionados)
    kilometros_anterior = -1
    for i in range(len(seleccionados)-1, -1, -1):
        if seleccionados[i] == 1:
            if kilometros_anterior - kilometros[i][0] >=5 or kilometros_anterior == -1:
                resultado[i] = kilometros[i]
                kilometros_anterior = kilometros[i][0]
            
    return resultado



if __name__ == "__main__":
    lista = [(1,5), (17,6), (19,2), (22,3), (127,4), (128,49)]
    print(carteles(lista))