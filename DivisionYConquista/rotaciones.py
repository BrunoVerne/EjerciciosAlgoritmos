







def encontrar_rotacion(V, inicio, fin, longitud):
    if inicio >= fin:
        return None
    
    elif fin - inicio == 1:
        if V[fin] < V[inicio]:
            if fin < longitud //2:
                return fin
            return longitud - fin
        return None
    
    media = (fin + inicio) // 2
    
    if V[media] > V[fin]:
        if fin - media == 1:
            if fin < longitud //2:
                return fin
            return longitud - fin
        return encontrar_rotacion(V,media, fin, longitud)
    
    else:
        if media - inicio == 1:
            return media
        return encontrar_rotacion(V,inicio, media, longitud)
    
 
    
        
    
    
    
    
if __name__ == "__main__":
    lista1= [9,1,6,7,8]
    print(encontrar_rotacion(lista1,0,len(lista1)-1, len(lista1)))
    
    