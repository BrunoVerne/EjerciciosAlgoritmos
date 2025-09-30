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

    if ultimo[0] > seleccion[-1][1] or ultimo[0] == seleccion[-1][1] and ultimo[2] > seleccion[-1][2]:
        seleccion.append(ultimo)
    return seleccion


if __name__ == "__main__":
    t = [[1,1,1,2], [1,3,1,15], [2,3,4,6]]
    print(trabajadores(t))