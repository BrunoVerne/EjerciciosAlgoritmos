#Para la realización del próximo congreso de “charlas motivacionales para el joven de
#hoy” se contrató un hotel que cuenta con “m” salas de exposición. Existirán “n” oradores.
#Cada uno solicitó un tiempo de exposición definido por un horario de ingreso y una
#duración. Los organizadores quieren asignar las salas con un intervalo entre charla y charla
#de 15 minutos y desean utilizar la menor cantidad de salas posibles. Presentar un algoritmo
#greedy que resuelve el problema indicando la cantidad de salas a utilizar y la asignación de
#las charlas. En caso de sobrepasar el máximo de salas disponibles informar. Analice
#complejidad y optimalidad
class Orador:
    def __init__(self, nombre, inicio, duracion,asignado):
        self.nombre = nombre
        self.inicio = inicio
        self.duracion = duracion
        
        
def asignaciones(salas, oradores, intervalo, maxSalas):
    oradores = sorted(oradores, key=lambda x: x.inicio)
    for orador in oradores:
        asignado = False
        for sala in salas:
            
            if len(sala) == 0: 
                sala.append(orador)
                asignado = True
                break
            
            else:
                ultimoOrador = sala[-1]
                if(ultimoOrador.inicio + ultimoOrador.duracion + intervalo <= orador.inicio):
                    sala.append(orador)
                    asignado = True
                    break
        if(not asignado):
            if(len(salas) < maxSalas):
                salas.append([orador])
                asignado = True   
        
        if(not asignado):
            print("no hay salas disponibles")

    return salas


#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.
                
        
        
        
        
        
