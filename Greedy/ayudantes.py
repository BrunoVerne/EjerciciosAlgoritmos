# Una jefa de trabajos prácticos (jtp) está a cargo de un grupo de N ayudantes, cada uno
# de los cuales tiene que trabajar un turno completo durante la semana. Hay muchas
# actividades asociadas con cada turno (atender el laboratorio, dar clase de consultas, etc.)
# pero podemos pensar en un turno como un intervalo de tiempo contiguo. Puede haber más
# de un turno simultáneamente. La Jtp está tratando de construir un subconjunto de esos N
# ayudantes para formar un comité de supervisión, que esté en contacto con todos los
# ayudantes. Un comité de supervisión está en contacto con todos los ayudantes si, cualquiera
# sea el turno de un ayudante, hay alguien en el comité de supervisión cuyo turno se
# superpone, aunque sea parcialmente, con el turno de ese ayudante. Ejemplo: N=3, ayudante
# 1 = Lunes de 16 a 20, ayudante 2 = Lunes de 18 a 22, ayudante 3 = Lunes de 21 a 23. En este
# caso, la solución es {ayudante 2}. Dado un conjunto de ayudantes, diseñar un comité de
# supervisión lo más pequeño posible, usando una estrategia greedy.

ultimoguardado = actividades[0]
agarrados = [0] * len(actividades)

for i in range(0, len(actividades)-1):
    if ultimoguardado.fin < actividades[i+1].inicio:
        agarrados[i] = 1
        ultimoguardado = actividades[i]

if ultimoguardado.fin < actividades[-1].inicio:
    agarrados[-1] = 1

for j in range(len(actividades)-2, -1, -1):
    if agarrados[j] == 1 and agarrados[j+1] == 1:
        if actividades[j].fin >= actividades[j+1].inicio:  
            agarrados[j] = 0

return [actividades[i] for i in range(len(actividades)) if agarrados[i] == 1]