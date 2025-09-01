# Esta peculiar empresa se dedica a cubrir patios cuadrados de n*n metros (“n” es un
# número entero potencia de 2 y mayor o igual a 2). Cuenta con baldosas especiales que
# tienen forma en L (como se muestra en celeste en la
# imágen). Las baldosas no se pueden cortar. Todo patio
# cuenta con un único sumidero de agua de lluvia. Ocupa
# 1x1 metro y su ubicación depende del patio (Se muestra en
# la ﬁgura de ejemplo como un cuadrado negro). Nos piden
# que, dado un patio con un valor “n” y una ubicación del
# sumidero en una posición x,y desde la punta superior
# izquierda, determinemos cómo ubicar las baldosas.
# Presentar un algoritmo que lo resuelva utilizando división y
# conquista.
posiciones = []
def cubrirPatio(n, sumideroX, sumideroY, inicioX, inicioY):
    if n > 2:
        return(n/2,sumideroX, sumideroY, inicioX, inicioY)
    
    elif(n == 2):
        finalX = inicioX + n -1
        finalY = inicioY + n -1       
        if(inicioX + sumideroX < finalX and inicioY + sumideroY < finalY):
            return (inicioX,inicioY) , (finalX, finalY), (inicioX, finalY), (finalX, inicioY)
        return None
    
    
    mitad = int(n/2)
    cubrirPatio(mitad, sumideroX, sumideroY, inicioX, inicioY + mitad) # cuadrante de arriba a la izquierda
    cubrirPatio(mitad, sumideroX, sumideroY, inicioX + mitad, inicioY + mitad) # cuadrante de arriba a la derecha
    cubrirPatio(mitad, sumideroX, sumideroY, inicioX , inicioY) # cuadrante de abajo a la izquierda
    cubrirPatio(mitad, sumideroX, sumideroY, inicioX + mitad, inicioY) # cuadrante de abajo a la derecha



