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




def detector_de_mentiras(vector, inicio, fin):
    
    if inicio == fin:
        return vector[inicio]
    
    mitad = (inicio + fin) // 2
    
    
    candidato = detector_de_mentiras(vector, inicio, mitad)
    
    if candidato is None:
        candidato = detector_de_mentiras(vector, mitad + 1, fin)
    
    if candidato is None:
        return None
    
    
    conteo = 0
    for i in range(inicio, fin + 1):
        if candidato.funciona(vector[i]) and vector[i].funciona(candidato):
            conteo += 1
    
    if conteo > (fin - inicio + 1) // 2:
        return candidato
    return None



if __name__ == "__main__":
    dA = Detector(False, "A")
    dB = Detector(True, "B")
    dC = Detector(True, "C")
    dD = Detector(True, "D")
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