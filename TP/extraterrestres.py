import sys
def ejecucion(palabra):
    n = len(palabra)
    if n == 0:
        return 0, ""
    
    # Matriz booleana
    OPT = [[0] * n for _ in range(n)]
    
    max_longitud = 1
    inicio_max = 0 
    
    # Caso base: una letra es palíndromo de sí misma
    for i in range(n):
        OPT[i][i] = 1
    

    for i in range(n - 1):
        if palabra[i] == palabra[i + 1]:
            OPT[i][i + 1] = 1
            max_longitud = 2
            inicio_max = i  
            
    
    # Voy agarrando cadenas de 3 a n y las voy comparando mirando la matriz booleana 
    for longitud in range(3, n + 1):
        for i in range(n - longitud + 1):
            final = i + longitud - 1
            if palabra[i] == palabra[final] and OPT[i + 1][final - 1] == 1:
                OPT[i][final] = 1
                if longitud > max_longitud:
                    max_longitud = longitud
                    inicio_max = i  # Guardamos el inicio del nuevo palíndromo máximo
    
    palindromo = ""
    for i in range(inicio_max, inicio_max + max_longitud):
        palindromo += palabra[i]
    
    return palindromo
    
     

if __name__ == "__main__":
    frase = sys.argv[1]
    print(ejecucion(frase))