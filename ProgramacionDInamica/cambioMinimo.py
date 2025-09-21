def cambioMinimo(n, base):
    """
    n: cantidad de cambio a dar
    base: lista de denominaciones de monedas disponibles
    """
    OPT = [float('inf')] * (n + 1) 
    OPT[0] = 0  
    elegida = [0] * (n + 1) 
 
    for i in range(1, n + 1):
        minimo = float('inf')
        # Probar cada tipo de moneda
        for moneda in base:
            resto = i - moneda
            if resto >= 0:  # Si podemos usar esta moneda
                if OPT[resto] < minimo:
                    minimo = OPT[resto]
                    elegida[i] = moneda
        OPT[i] = 1 + minimo
    
    resto = i
    while resto > 0:
        if elegida[resto] == 0:
            print("NO ES POSIBLE DAR CAMBIO CON ESTA BASE")
            break
        
        moneda = elegida[resto]
        print(moneda)
        resto = resto - moneda
    return "cantidad de monedas: ", OPT[n]



if __name__ == "__main__":
    print(cambioMinimo(8,[1,2,4,5]))