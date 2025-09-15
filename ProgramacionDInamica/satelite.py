# Para un nuevo satélite a poner en órbita una empresa privada puede optar por incluir
#  diversos sensores a bordo (por ejemplo: variación de temperatura, humedad en tierra,
#  caudal de ríos, etc). Cada uno de ellos tiene un peso "pi" y una ganancia "gi" calculado por su
#  uso durante la vida útil del satélite. Si bien les gustaría incluir todos, el satélite tiene una
#  carga máxima P que puede llevar. Nos piden que generemos un algoritmo (utilizando
#  programación dinámica) para resolver el problema. Indique si su solución es polinomial.

#defino a sensores como lista de elementos del estilo: (pi,gi)
def pesos_satelite(sensores,carga_maxima):
    OPT = [0] * (carga_maxima + 1)
    OPT[0]=0
    for i in range(1,carga_maxima+1):
        for p,g in sensores:
            if i >= p:
                OPT[i] = max(OPT[i], OPT[i - p] + g)

    return OPT[carga_maxima]


if __name__ == "__main__":
    sensores1 = [(2, 3), (3, 4), (4, 5)]
    print(pesos_satelite(sensores1, 5))
    sensores2 = [(4, 20), (6, 30), (8, 40)]
    print(pesos_satelite(sensores2, 12))