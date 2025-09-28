# Dentro de un país existen dos colonias subacuáticas cada una de ellas con “n”
# habitantes. Cada habitante tiene su documento de identidad único identiﬁcado por un
# número. Para una tarea especial se decidió seleccionar a aquella persona que vive en alguna
# de las colonias cuyo número de documento corresponda a la mediana de todos los números
# de documento presentes en ellas. Por una cuestión de protocolo no nos quieren dar los
# listados completos de documentos. Solo nos responden de cada colonia ante la consulta
# “Cual es el documento en la posición X de todos los habitantes de la isla ordenados de mayor
# a menor”. Utilizando esto, proponer un algoritmo utilizando división y conquista que
# resuelva el problema con la menor cantidad posibles de consultas. Analizar complejidad
# espacial y temporal.

def encontrar_dni(colonia1, colonia2):
    n = len(colonia1)
    minimo = min(colonia1[-1], colonia2[-1])
    maximo = max(colonia1[0], colonia2[0])

    
    media = (maximo + minimo) // 2
    
    posicion, colonia = encontrar_media(colonia1,0,n-1, media)
    if posicion != -1:
        return posicion, colonia
    
    return encontrar_media(colonia2,0, n-1, media)


def encontrar_media(n, inicio, fin, elemento):
    if fin <= inicio:
        if n[fin] == elemento:
            return (fin, n)
        return (-1,n)
    
    
    media = (fin + inicio) //2
    
    if n[media] == elemento:
        return (media, n)
    
    if n[media] < elemento:
        return encontrar_media(n, 0, media-1, elemento)
    
    return encontrar_media(n,media+1,fin,elemento)


