# Para una inversión inmobiliaria un grupo inversor desea desarrollar un barrio privado
# paralelo a la una ruta. Con ese motivo realizaron una evaluación de los diferentes terrenos
# en un trayecto de la misma. Diferentes inversores participarán, pero a condición de comprar
# algún terreno en particular. El grupo inversor determinó para cada propiedad su evaluación
# de ganancia. El mismo surge como la suma de inversiones ofrecida por el terreno menos el
# costo de compra. Debemos recomendar que terrenos contiguos comprar para que
# maximicen sus ganancias. Ejemplo: S = [-2, 3, -3, 4, -1, 2]. La mayor ganancia es de 5,
# comprando los terrenos de valor [4, -1, 2]. Solucionar el problema mediante un algoritmo de
# programación dinámica.

def inversion(lista):
    max_local = [0] * len(lista)
    max_local[0] = lista[0]
    max_global = lista[0]
    
    for i in range(len(lista)):
        max_local[i] = max(max_local[i-1] + lista[i], lista[i])
        max_global = max(max_local[i], max_global)
        
        
    
    return reconstruir(max_global, max_local, lista)


def reconstruir(max_global, maximos_locales,lista):
    indice_final = -1
    for i in range(len(lista)-1,0,-1):
        if maximos_locales[i] == max_global:
            max_aux = 0
            indice_final = i
            for j in range(i,-1,-1):
                max_aux = lista[j] + max_aux
                if max_aux == max_global:
                    return "indice inicial: ", j , " indice final: ", i
    
    

if __name__ == "__main__":
    S = [-2, 3, -3, 4, -1, 2]
    print(inversion(S))
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(inversion(lista1))



#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.