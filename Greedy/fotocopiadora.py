# Contamos con una impresora central en un centro de cómputos del campus universitario.
# Entre varios departamentos y laboratorios nos solicitan al inicio de cada mes, la impresión
# de “n” documentos. Cada uno de ellos tiene una duración determinada y cuenta con una
# fecha de entrega. Si nos pasamos de esta recibimos un apercibimiento proporcional al
# retraso más largo del mes. Como a la impresora le falta mantenimiento queremos lograr -
# siempre que sea posible - tiempo entre los trabajos de impresión. Presentar un algoritmo
# greedy que dada la lista de tareas proponga la fechas de inicio de publicación minimizando
# el apercibimiento y dando tiempo entre las tareas siempre que sea posible



# ordeno los n documentos segun ratio mas próximos(menores) o sea la diferencia entre la fecha de entrega y su duracion 
# lo minimo que se puede tardar es un ratio de 1 ya que si lo tengo que entregar en x horas y hacerlo me dura x el minimo deadline es = 1
# por lo tanto si el i-ésimo documento tiene deadline > 1 le doy esa diferencia hasta 1 para resfrecar la maquina

def fotocopiadora(documentos):
     # -> sea documentos una lista de documentos del tipo documento = [duracion, fecha_entrega(en horas)]
    documentos = sorted(documentos, key=lambda x: x[1])
    horarios = []
    refresco_maquina = []
    apercibimiento = 0
    inicio = 0
    for duracion, entrega in documentos:
        if inicio + duracion <= entrega:
            fin_descanso = entrega - duracion
            if fin_descanso > inicio:
                refresco_maquina.append([inicio, fin_descanso])
                horarios.append([fin_descanso,entrega])
            else:
                horarios.append([inicio, inicio + duracion])
            
            inicio = entrega
        
        else:
            horarios.append([inicio, inicio + duracion])
            retraso = inicio + duracion - entrega 
            if retraso > apercibimiento:
                apercibimiento = retraso
            
            inicio = inicio + duracion
                
    return horarios, refresco_maquina, apercibimiento


#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.

    