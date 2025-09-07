# Para la elaboración de un juego se desea construir un cielo nocturno de una ciudad
# donde se vea el contorno de los ediﬁcios en el horizonte. Cada ediﬁcio “ei“ está representado
# por rectángulos mediante la tripla (izquierda, altura, derecha). Dónde “izquierda”
# corresponde a la coordenada x menor, “derecha” la coordenada x mayor y altura la
# coordenada y. Todos los ediﬁcios inician en la coordenada 0 de y. Se cuenta con una lista de
# N ediﬁcios que llegan sin un criterio de orden especíﬁco. Se desea emitir como resultado el
# contorno representado como una lista de coordenadas “x” y sus alturas. Tenga en cuenta el
# siguiente ejemplo: Lista de ediﬁcios: (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16) , (14, 3, 25),
# (19,18,22). Contorno: (1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(25,0). Presentar un
# algoritmo utilizando división y conquista que dado el listado de ediﬁcios retorna como
# resultado el contorno de la ciudad.

class Edificio:
    def __init__(self, izquierda, altura, derecha):
        self.izquierda = izquierda
        self.altura = altura
        self.derecha = derecha
    
    def __repr__(self):
        return f"({self.izquierda}, {self.altura}, {self.derecha})"
    
    
    
    
    

def contorno(lista_edificios):
    lista_edificios_ordenada = sorted(lista_edificios, key=lambda x: x.izquierda)
    return definir_contorno(lista_edificios_ordenada,0,len(lista_edificios_ordenada)-1)    




def definir_contorno(edificios, inicio, fin):
    if inicio == fin:
        edificio = edificios[inicio]
        return [(edificio.izquierda, edificio.altura), (edificio.derecha, 0)]
    
    
    elif fin - inicio == 1 :
        multisuperposicion = False
        if edificios.index(edificios[fin]) - edificios.index(edificios[inicio]) != 1:
            multisuperposicion = True
        
        if not multisuperposicion:
        
            edificioA = edificios[inicio]
            edificioB = edificios[fin]
            if edificioA.izquierda < edificioB.izquierda and edificioA.derecha < edificioB.derecha:
                if(edificioA.altura < edificioB.altura):
                    return [(edificioA.izquierda, edificioA.altura),
                            (edificioB.izquierda, edificioB.altura)]
                
                else:
                    return [(edificioA.izquierda, edificioA.altura),
                            (edificioA.derecha, edificioB.altura)]
                    
                    
            elif edificioA.izquierda < edificioB.izquierda and edificioA.derecha > edificioB.derecha:
                    if edificioA.altura < edificioB.altura:
                        return [(edificioA.izquierda, edificioA.altura),
                                (edificioB.izquierda, edificioB.altura)]
                    else:
                        return [(edificioA.izquierda, edificioA.altura)]
                            
            elif edificioA.derecha < edificioB.izquierda:
                    return [(edificioA.derecha, 0),(edificioB.izquierda, edificioB.altura)]
        else:
            contorno_superposiciones(inicio, fin)

    mitad = (inicio + fin) // 2
    izquierda = definir_contorno(edificios, inicio,mitad) 
    derecha = definir_contorno(edificios,mitad+1,fin)
    return izquierda + derecha
    

def contorno_superposiciones(edificios, inicio, fin):
    i = edificios.index([inicio])
    j = edificios.index([fin])
    
    mas_alto = None
    while i <= j:
        edifico = edificios[i]
        if(edificios[i].altura > mas_alto):
            mas_alto = edi
        i +=1


if __name__ == "__main__":
    edificios1 = [
        Edificio(1, 11, 5),
        Edificio(2, 6, 7),
        Edificio(3, 13, 9),
        Edificio(12, 7, 16),
        Edificio(14, 3, 25),
        Edificio(19, 18, 22)
    ]
    
    print(contorno(edificios1))
    
    
