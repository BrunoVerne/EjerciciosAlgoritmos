# Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los
# primeros ”m” números naturales ordenados en forma creciente (m >= n). En el vector no hay
# números repetidos. Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8,
# 9, 11, 12, 13, 14, 20, 22]. Solución: 6. Proponer un algoritmo de tipo división y conquista que
# resuelva el problema en tiempo inferior a lineal. Expresar su relación de recurrencia y
# calcular su complejidad temporal.


def encontrarMenor(vector, inicio, fin):

    if(fin - inicio == 1): #indices juntos o sea elementos consecutivos
        if(vector[fin] - vector[inicio] > 1):
            return vector[inicio] +1
        return None
    
    if(fin <= inicio):
        return None
    
    mitad = int((fin + inicio) / 2)
    
    menorIzquierdo = encontrarMenor(vector, inicio, mitad)
    if(menorIzquierdo is not None):
        return menorIzquierdo
    
    menorDerecho = encontrarMenor(vector, mitad, fin)

    if(menorDerecho is not None):
        return menorDerecho



if __name__ == "__main__":
    vector = [1,2,3,4,6,7,8,9]
    print("vector 1:" ,encontrarMenor(vector, 0, len(vector)-1))
    vector2 = [4,5,6,7,9]
    print("vector 2:" ,encontrarMenor(vector2,0,len(vector2)-1))
    vector3 = [2, 3, 4, 5, 6]
    print("vector3:", encontrarMenor(vector3, 0, len(vector3)-1))
    vector4 = [1, 2, 3, 5, 7, 8, 9]
    print("vector4:", encontrarMenor(vector4, 0, len(vector4)-1))  
    vector5 = [10, 11, 12, 20, 21, 22]
    print("vector5:", encontrarMenor(vector5, 0, len(vector5)-1))
    vector6 = [1, 2, 3, 4, 10]
    print("vector6:", encontrarMenor(vector6, 0, len(vector6)-1))