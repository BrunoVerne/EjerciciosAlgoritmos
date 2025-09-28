# El dueño de una empresa desea organizar una fiesta de la misma. Cómo quiere que la
# fiesta sea lo más tranquila posible, no quiere que asistan un empleado y su jefe directo. Pidió
# a su encargado que le ponga un rating de convivencia (Ri) a cada empleado. Con dicha
# información más un organigrama de la compañía, le pidió a un especialista en informática
# que diseñe un algoritmo para obtener el listado de los empleados que deberá invitar a la
# fiesta. Teniendo en cuenta que: Ri > 0, que no cuenta para el armado del algoritmo y que la
# 1
# estructura jerárquica es en forma de árbol. Se pide resolver mediante programación
# dinámica


Sea rating = [] una lista de los rating de cada empleado o sea de longitud n
sea OPT una matriz de n x 2 siendo el binario la representacion de invitar al i-ésimo empleado o no
OPT[nodo] = max(OPT[nodo][0] + OPT[nodo][1]) #o sea el rating que tengo invitandolo y no invitandolo


def pseudocodigo():
    
    for nodo in arbol recorriendo de hojas a nodo:
        if nodo.esHoja():
            OPT[nodo][0] = 0
            OPT[nodo][1] = rating[nodo]
        
        else:
            OPT[nodo][0] = 0
            OPT[nodo][1] = rating[nodo] 
            
            for hijo in nodo.hijos():  
                OPT[nodo][0] += max(OPT[hijo][0], OPT[hijo][1]) # no lo invito al jefe
                
                OPT[nodo][1] += OPT[hijo][0] #lo invito
                
    return max(OPT[raiz][0], OPT[raiz][1])
            






def codigo():
    OPT = [[0, 0] for _ in range(n+1)]
    # Obtener orden de procesamiento (hojas → raíz)
    orden = obtener_orden_hojas_a_raiz(raiz, hijos)

    for nodo in orden:
        if len(hijos[nodo]) == 0:  # nodo.esHoja()
            OPT[nodo][0] = 0
            OPT[nodo][1] = rating[nodo]
        else:
            OPT[nodo][0] = 0
            OPT[nodo][1] = rating[nodo]  # ← Inicializar con el rating del nodo
            
            for hijo in hijos[nodo]:
                OPT[nodo][0] += max(OPT[hijo][0], OPT[hijo][1])
                OPT[nodo][1] += OPT[hijo][0]

    return max(OPT[raiz][0], OPT[raiz][1])