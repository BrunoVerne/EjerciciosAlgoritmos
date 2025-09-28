def subsetSum(elementos, W):
    """
    elementos: lista de tuplas (nombre, peso)
    W: capacidad máxima
    Devuelve: valor máximo alcanzable sin exceder W
    """
    E = len(elementos) # = cantidad de elementos Ei = cantidad de pesos Wi
    OPT = [[0] * (W + 1) for _ in range(E + 1)]
    

    for i in range(E + 1):
        OPT[i][0] = 0
    for w in range(W + 1):
        OPT[0][w] = 0
    
    for i in range(1, E  + 1):
        peso_i = elementos[i - 1][1]
        for Wi in range(1, W + 1):
            if peso_i <= Wi:
                OPT[i][Wi] = max(OPT[i - 1][Wi], OPT[i - 1][Wi - peso_i] + peso_i)
            else:
                OPT[i][Wi] = OPT[i - 1][Wi]
    
    return OPT[E][W]


if __name__ == "__main__":
    
    elementos = [("A", 2), ("B", 3), ("C", 7), ("D", 8)]
    W = 11
    resultado = subsetSum(elementos, W)
    print(f"Suma máxima posible sin exceder {W}: {resultado}")