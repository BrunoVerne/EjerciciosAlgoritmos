# La sala de guardia de un hospital tiene que tener al menos un médico en todos los
# feriados y en los ﬁnes de semana largos de feriados. Cada profesional indica sus
# posibilidades: por ejemplo alguien puede estar de guardia en cualquier momento del ﬁn de
# semana largo del 9 de julio (p. ej. disponibilidad de A para el 9 de julio = (Jueves 9/7, Viernes
# 10/7, Sábado 11/7, Domingo 12/7)), también puede suceder que alguien pueda sólo en parte
# (por ejemplo, disponibilidad de B para 9 de julio = (Jueves 9/7, Sábado 11/7, Domingo 12/7)).
# Aunque los profesionales tengan múltiples posibilidades, a cada uno se lo puede convocar
# para un solo día (se puede disponer de B sólo en uno de los tres días que indicó). Para
# ayudar a la sala de guardia a planiﬁcar cómo se cubren los feriados durante todo el año
# debemos resolver el problema de las guardias: Existen k períodos de feriados (por ejemplo, 9
# de julio es un período de jueves 9/7 a domingo 12/7, en 2019 Día del Trabajador fue un
# período de 1 día: miércoles 1 de mayo, etc.). Dj es el conjunto de fechas que se incluyen en el
# período de feriado j-ésimo. Todos los días feriados son los que resultan de la unión de todos
# los Dj. Hay n médicos y cada médico i tiene asociado un conjunto Si de días feriados en los
# que puede trabajar (por ejemplo B tiene asociado los días Jueves 9/7, Sábado 11/7, Domingo
# 12/7, entre otros).
# Proponer un algoritmo polinomial (usando ﬂujo en redes) que toma esta información ydevuelve qué profesional se asigna a cada día feriado (o informa que no es posible resolver
# el problema) sujeto a las restricciones:
# ○ Ningún profesional trabajará más de F días feriados (F es un dato), y sólo en días en
# los que haya informado su disponibilidad.
# ○ A ningún profesional se le asignará más de un feriado dentro de cada período Dj.




#---------Modelacion:   Fuente → Médicos → [Médico i × Período j] → Días feriados -> Periodo correspondiente → Sumidero



#PSEUDOCÓDIGO:
# ALGORITMO AsignarGuardias(medicos, periodos, F)
#     ENTRADA:
#         medicos: lista de conjuntos de días disponibles por médico
#         periodos: lista de conjuntos de días por período
#         F: máximo de días por médico
    
#     SALIDA:
#         asignaciones: día → médico O "No es posible"

#     // CONSTRUIR GRAFO
#     n_medicos = LONGITUD(medicos)
#     n_periodos = LONGITUD(periodos)
    
#     // Calcular total de nodos
#     total_nodos = 1 + n_medicos + (n_medicos * n_periodos) + total_dias + n_periodos + 1
    
#     // Crear grafo de flujo
#     grafo = MATRIZ[total_nodos][total_nodos] inicializada en 0
    
#     // Asignar índices simples
#     fuente = 0
#     sumidero = total_nodos - 1
    
#     // Nodos médicos: 1..n_medicos
#     // Nodos médico×período: siguiente bloque  
#     // Nodos días: siguiente bloque (numerados consecutivamente)
#     // Nodos períodos: último bloque antes del sumidero
    
#     // 1. FUENTE → MÉDICOS
#     PARA i = 0 hasta n_medicos-1 HACER
#         grafo[fuente][nodo_medico(i)] = F
#     FIN PARA
    
#     // 2. MÉDICOS → MÉDICO×PERÍODO  
#     PARA i = 0 hasta n_medicos-1 HACER
#         PARA j = 0 hasta n_periodos-1 HACER
#             SI medicos[i] INTERSECCION periodos[j] NO ES VACÍO ENTONCES
#                 grafo[nodo_medico(i)][nodo_medico_periodo(i,j)] = 1
#             FIN SI
#         FIN PARA
#     FIN PARA
    
#     // 3. MÉDICO×PERÍODO → DÍAS
#     PARA i = 0 hasta n_medicos-1 HACER
#         PARA j = 0 hasta n_periodos-1 HACER
#             PARA CADA dia EN periodos[j] HACER
#                 SI dia EN medicos[i] ENTONCES
#                     grafo[nodo_medico_periodo(i,j)][nodo_dia(dia)] = 1
#                 FIN SI
#             FIN PARA
#         FIN PARA
#     FIN PARA
    
#     // 4. DÍAS → PERÍODOS
#     PARA j = 0 hasta n_periodos-1 HACER
#         PARA CADA dia EN periodos[j] HACER
#             grafo[nodo_dia(dia)][nodo_periodo(j)] = 1
#         FIN PARA
#     FIN PARA
    
#     // 5. PERÍODOS → SUMIDERO
#     PARA j = 0 hasta n_periodos-1 HACER
#         grafo[nodo_periodo(j)][sumidero] = 1
#     FIN PARA
    
#     // EJECUTAR FORD-FULKERSON
#     flujo = FordFulkerson(grafo, fuente, sumidero)
    
#     SI flujo < n_periodos ENTONCES
#         DEVOLVER "No es posible"
#     SINO
#         // RECONSTRUIR ASIGNACIONES
#         asignaciones = {}
#         PARA CADA dia EN TODOS_LOS_DIAS HACER
#             PARA i = 0 hasta n_medicos-1 HACER
#                 PARA j = 0 hasta n_periodos-1 HACER
#                     nodo_mp = nodo_medico_periodo(i,j)
#                     nodo_d = nodo_dia(dia)
#                     SI grafo[nodo_d][nodo_mp] > 0 ENTONCES
#                         asignaciones[dia] = i
#                     FIN SI
#                 FIN PARA
#             FIN PARA
#         FIN PARA
#         DEVOLVER asignaciones
#     FIN SI
# FIN ALGORITMO



class Grafo:
    def __init__(self):
        self.conexiones = {}  # nodo -> {vecino: capacidad}
    
    def agregar_arista(self, u, v, capacidad):
        if u not in self.conexiones:
            self.conexiones[u] = {}
        if v not in self.conexiones:
            self.conexiones[v] = {}
        self.conexiones[u][v] = capacidad
        self.conexiones[v][u] = 0

def asignar_guardias(medicos, periodos, F):
    n_medicos = len(medicos)
    n_periodos = len(periodos)
    
    # Calcular días totales
    dias_totales = set()
    for periodo in periodos:
        dias_totales.update(periodo)
    n_dias = len(dias_totales)
    
    # Crear grafo
    grafo = Grafo()
    fuente = 0
    sumidero = 1
    
    # Asignar índices únicos
    # Médicos: 2, 3, 4, ...
    # Médico×Período: después de médicos
    # Días: después de médico×período  
    # Períodos: después de días
    
    idx_actual = 2
    
    # Nodos médicos
    nodos_medicos = list(range(idx_actual, idx_actual + n_medicos))
    idx_actual += n_medicos
    
    # Nodos médico×período
    nodos_mp = {}
    for i in range(n_medicos):
        for j in range(n_periodos):
            # Solo crear nodo si el médico puede trabajar en algún día del período
            puede_trabajar = False
            for dia in periodos[j]:
                if dia in medicos[i]:
                    puede_trabajar = True
                    break
            
            if puede_trabajar:
                nodos_mp[(i, j)] = idx_actual
                idx_actual += 1
    
    # Nodos días
    dias_a_nodo = {}
    for dia in dias_totales:
        dias_a_nodo[dia] = idx_actual
        idx_actual += 1
    
    # Nodos períodos
    nodos_periodos = list(range(idx_actual, idx_actual + n_periodos))
    idx_actual += n_periodos
    
    # 1. Fuente -> Médicos
    for i, nodo_med in enumerate(nodos_medicos):
        grafo.agregar_arista(fuente, nodo_med, F)
    
    # 2. Médicos -> Médico×Período
    for (i, j), nodo_mp in nodos_mp.items():
        grafo.agregar_arista(nodos_medicos[i], nodo_mp, 1)
    
    # 3. Médico×Período -> Días
    for (i, j), nodo_mp in nodos_mp.items():
        for dia in periodos[j]:
            if dia in medicos[i]:
                grafo.agregar_arista(nodo_mp, dias_a_nodo[dia], 1)
    
    # 4. Días -> Períodos
    for j in range(n_periodos):
        for dia in periodos[j]:
            grafo.agregar_arista(dias_a_nodo[dia], nodos_periodos[j], 1)
    
    # 5. Períodos -> Sumidero
    for j in range(n_periodos):
        grafo.agregar_arista(nodos_periodos[j], sumidero, len(periodos[j]))
    
    # Ford-Fulkerson
    flujo = ford_fulkerson(grafo, fuente, sumidero)
    
    if flujo < n_dias:
        return "No es posible asignar guardias"
    
    # Reconstruir asignaciones
    asignaciones = {}
    
    for dia, nodo_dia in dias_a_nodo.items():
        # Buscar de qué médico×período viene el flujo
        for (i, j), nodo_mp in nodos_mp.items():
            if nodo_dia in grafo.conexiones.get(nodo_mp, {}):
                if grafo.conexiones[nodo_dia][nodo_mp] > 0:
                    asignaciones[dia] = i
                    break
    
    return asignaciones

def ford_fulkerson(grafo, fuente, sumidero):
    return 0