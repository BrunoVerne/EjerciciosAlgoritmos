import sys
def ejecucion(sectores):
    
    array_frecuencia = contar_frecuencia(sectores)
    
    cantidad_impares = contar_impares(array_frecuencia)   
    if cantidad_impares > 1:  #solo en la primera fila solo puede haber algun impar de cada lado
        print("no es posible realizar el escenario")
        return 1
        
    izquierda = ordenamiento_greedy(array_frecuencia)
    centro = elegir_centro(array_frecuencia)

    derecha = espejar_lista(izquierda)
    
    
    if centro is not None:
        resultado = izquierda + [centro] + derecha
    else:
        resultado = izquierda + derecha
    
    
    salida = ""
    for x in resultado:
        salida += str(x)
    print(salida)
    
    return 0    


def contar_frecuencia(sectores): # O(n)
    array_frecuencia = [0] * 10
    for butacas in sectores:  
        array_frecuencia[int(butacas)] +=1  
        
    return array_frecuencia


def contar_impares(frecuencias): #O(1)
    cantidad_impares = 0
    for frecuencia in frecuencias:
        if frecuencia > 0 and frecuencia % 2 == 1:
            cantidad_impares +=1
    return cantidad_impares


def espejar_lista(lista):# O(n)
    espejado = []
    for i in range(len(lista) - 1, -1, -1):   
        espejado.append(lista[i])
    return espejado
        
        
        


def ordenamiento_greedy(frecuencia): # O(1)
    lista_greedy = []
    for i in range(9, -1, -1): # va de 9  a  0 a paso -1 
        while frecuencia[i] >= 2:
            lista_greedy.append(i)
            frecuencia[i] -= 2
            
    return lista_greedy

def elegir_centro(frecuencia):  # O(1)  #eleccion Greedy tambien
    centro = None
    for i in range(9,-1,-1):
        if frecuencia[i] == 1 and centro == None:
            centro = i
            frecuencia[i] -=1
    return centro

if __name__ == "__main__":
    sectores = sys.argv[1]
    ejecucion(sectores)