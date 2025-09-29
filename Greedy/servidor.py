# Un servidor de videojuegos se alquila por horas. El contrato dura un tiempo ﬁjo y
# permite utilizar en forma exclusiva el mismo por una cantidad continua de horas una vez por
# semana. Por cada contrato que el dueño del servidor establece, se lleva un monto ﬁjo de
# dinero. Al dueño del servidor le interesa tener la mayor cantidad de contratos posibles (sin
# importar la duración en horas de los mismos). El servidor funciona las 24hs. Recibe un
# conjunto de ofertas de contrato y debe seleccionar cuales aceptar. Cada contrato tiene un
# día y hora de inicio y un día y hora de ﬁn. Durante ese lapso tendrán la exclusividad del
# servidor. Ese tiempo contiguo no puede durar más de 1 semana (un contrato podría pedir
# por ejemplo 3 días completos pero nunca superar la semana).. Y esa fecha se repite todas las
# semanas. Los contratos aceptados no deben superponerse. Proponer una solución greedy
# que solucione el problema de forma óptima. Tenga en cuenta que es posible contratos que
# empiecen al ﬁnalizar la semana y terminen horas después del inicio de la misma.

def servidor(contratos):
    """_summary_

    Args:
        contratos una lista de contrato del tipo contrado = [inicio (en horas), fin(en horas)]
    """
    contratos = sorted(contratos, key= lambda x: x[1])
    elegidos=[]
    elegidos.append(contratos[0])
    inicio_primero,fin_ultimo = contratos[0]
    for i in range(1,len(contratos)):
        contrato_actual = contratos[i]
        
        if contrato_actual[1] < contrato_actual[0]: # caso en que empieza un domingo y termina un lunes
            if contrato_actual[1] < inicio_primero  and contrato_actual[0] > fin_ultimo:# si termina antes del inicio del primer contrato y empieza antes del último contrato
                elegidos.append(contrato_actual)
                inicio_primero = contrato_actual[0]
                
        elif contrato_actual[0] > fin_ultimo:
            elegidos.append(contrato_actual)
            fin_ultimo  =  contrato_actual[1]
    
    return elegidos
            