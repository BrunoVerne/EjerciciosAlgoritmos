# Una carrera tipo “Ironman” es un triatlón compuesto por 3 instancias: natación (3,86
# km de natación), ciclismo (180 km) y carrera a pie (42,2km). Para conocer al ganador se
# suman los tiempos realizados en cada una de las etapas. Tanto el ciclismo como la carrera a
# pie se puede realizar en simultáneo con todos los inscriptos. Pero, por una regulación se
# prohibió que más de 1 persona realice la etapa de nado en el lago en simultáneo. Se conoce
# el tiempo estimado de cada participante para cada evento. Proponga un orden de salida de
# tal forma de minimizar el tiempo total de toda la competencia.



class Participante:
    def __init__(self, nombre, tiempoRunning, tiempoCiclismo,tiempoNatacion):
        self.tiempoRunning = tiempoRunning
        self.tiempoCiclismo = tiempoCiclismo
        self.tiempoNatacion = tiempoNatacion
        

def ordenarParticipantes(participantes):
    participantesOrdenados = sorted(participantes, key=lambda x: x.tiempoRunning + x.tiempoCiclismo - x.tiempoNatacion, reverse=True)
    
    tiempoTotalEstimado = 0
    tiempoRetraso = 0
    for p in participantesOrdenados:
        tiempoTotal = tiempoRetraso + p.tiempoNatacion + p.tiempoRunning + p.tiempoCiclismo
        tiempoRetraso += p.tiempoNatacion
        if(tiempoTotal > tiempoTotalEstimado):
            tiempoTotalEstimado = tiempoTotal
            
    return participantesOrdenados,tiempoTotalEstimado
        
        