# Una empresa que realiza ciencia de datos debe realizar en las próximas “n” semanas
# procesos y cálculos intensivos. Para eso debe contratar tiempo de cómputo en la nube.
# Realizando una estimación conocen cuantas horas de cómputo necesitaran para cada una
# de las semanas. Por otro lado, luego de negociar con los principales proveedores tienen 2
# opciones que puede combinar a gusto. Opción 1: Contratar a la empresa “Arganzón” por
# semana. En esa semana se cobra proporcional al tiempo de cómputo según un parámetro
# “r” (horas computo x r). Opción 2: Contratar a la empresa “Fuddle” por un lapso de 5
# semanas contiguas. Durante el lapso contratado se paga una tarifa ﬁja de “c”. Proponer una
# solución utilizando programación dinámica que nos indique la secuencia de elecciones a
# realizar para minimizar el costo total de cómputo.

# OPT[i] = min(OPT[i-1] + R*i, OPT[i-5]+ C) siendo i >= 5


def computo(t,R,C):
    OPT = [0] * (t+1)
    OPT[0]= 0
    for i in range(1,t+1):
        if i >=5:
            OPT[i] = min(OPT[i-1] + R, OPT[i-5] +  C)
        else:
            OPT[i] = OPT[i-1] + R
            

    reconstruir = [""] * (t+1)
    i = t
    while i >= 0:
        if OPT[i-1] + R == OPT[i]:
            reconstruir[t-i] = "Arganzón"
            i -=1
        
        else:
            reconstruir[t-i] = "Fuddle"
            i -= 5
    
    return list(filter(lambda x: x != "", reconstruir)), OPT


if __name__ == "__main__":
    n = 14
    R = 25
    C = 20
    print(computo(n,R,C))
    
    


#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.