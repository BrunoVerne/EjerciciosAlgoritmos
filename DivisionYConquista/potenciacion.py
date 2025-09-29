def potenciacion(a,b):
    if b == 1:
        return a
    mitad = potenciacion(a, b // 2)
    if b % 2 == 1:
        return a * mitad *mitad
    return mitad * mitad


if __name__ == "__main__":
    print(potenciacion(2,32))
    
    



#COMPLEJIDAD TEMPORAL: log(n) COMPLEJIDAD ESPACIAL log(n):  EC DE RECURRENCIA: T(n) = T(n/2) + O(1)