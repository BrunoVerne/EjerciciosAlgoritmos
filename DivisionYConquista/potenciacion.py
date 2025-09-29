def potenciacion(a,b):
    if b == 1:
        return a
    mitad = potenciacion(a, b // 2)
    if b % 2 == 1:
        return a * mitad *mitad
    return mitad * mitad


if __name__ == "__main__":
    print(potenciacion(2,32))
    
    



#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.