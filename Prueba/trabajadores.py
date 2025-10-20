# lista de trabajadores tal que un trabajador contiene: [dia inicio, dia fin, hora inicio, hora fin]


def trabajadores(trabajadores):
    seleccion = []
    ultimo = trabajadores[0]
    for i in range(len(trabajadores)):
        actual = trabajadores[i]
        if actual[0] > ultimo[1]:
            seleccion.append(trabajadores[i-1])
            ultimo = trabajadores[i]
        
        elif actual[0] == ultimo[i] and actual[2] > ultimo[3]:
            seleccion.append(trabajadores[i-1])
            ultimo = trabajadores[i]

    if len(seleccion) != 0:
        if ultimo[0] > seleccion[-1][1] or ultimo[0] == seleccion[-1][1] and ultimo[2] > seleccion[-1][2]:
            seleccion.append(ultimo)
    
    else:
        seleccion.append(ultimo)
    return seleccion


if __name__ == "__main__":
    t8 = [[1,1,8,10], [3,4,5,7], [6,7,1,4]]
    print(trabajadores(t8))