import random

class Detector:
    def __init__(self, confiable=True, id=None):
        self.confiable = confiable
        self.id = id  
    
    def funciona(self, detector_a_probar):
        if self.confiable:  
            return detector_a_probar.confiable # me devuelve la posta del otro detector
        else:
            return random.choice([True, False]) # si esta fallado el detector te devuelve cualquier cosa 
    
    def __repr__(self):
        return f"Detector({self.id})"




def detector_de_mentiras(vector, inicio, fin):  # O(n)
    if(fin - inicio == 0):
        return vector[inicio]
    elif(fin - inicio < 0):
        return None
    
    elif (fin - inicio == 1):
        if(vector[inicio].funciona(vector[fin]) and vector[fin].funciona(vector[inicio])):
            return vector[inicio]
        return None
    
    mitad = (inicio + fin) //2
    
    candidato = detector_de_mentiras(vector, inicio, mitad)
    if candidato is not None:
        if(chequearMayoria(candidato,vector)): # se que mas de la mitad funcionan correctamente asi que debe matchear con mas de la mitad 
            return candidato
    
    candidato = detector_de_mentiras(vector, mitad + 1, fin)
    if candidato is not None:
        if(chequearMayoria(candidato,vector)):
            return candidato
        
    return None
    
    


def chequearMayoria(elemento, vector): # O(n)
    contador = 0
    for i in vector:
        if i.funciona(elemento) and elemento.funciona(i):
            contador +=1
    return contador > len(vector) // 2

if __name__ == "__main__":
    dA = Detector(True, "A")
    dB = Detector(True, "B")
    dC = Detector(True, "C")
    dD = Detector(False, "D")
    dE = Detector(False, "E")
    dF = Detector(True, "F")
    dG = Detector(False, "G")
    
    vector1 = [dA, dB, dC, dD]      # mayoría confiable -> devuelve un confiable
    vector2 = [dA, dB, dD, dE]       # 2 confiables de 4 -> no hay mayoría -> None
    vector3 = [dA, dB, dC, dF]       # 4 confiables -> devuelve un confiable
    vector4 = [dD, dE, dG]            # ninguno confiable -> None
    vector5 = [dA, dD, dF, dG, dB]     # 3 confiables de 5 -> devuelve un confiable

    print(detector_de_mentiras(vector1, 0, len(vector1)-1))
    print(detector_de_mentiras(vector2,0, len(vector2)-1))
    print(detector_de_mentiras(vector3, 0, len(vector3)-1))
    print(detector_de_mentiras(vector4, 0, len(vector4)-1))
    print(detector_de_mentiras(vector5, 0, len(vector5)-1))    