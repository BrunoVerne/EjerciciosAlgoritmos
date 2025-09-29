# Una agencia de inteligencia ha conseguido interceptar algunos mensajes
# encriptados de una agencia rival. Mediante espionaje logran saber algunas cosas para
# desencriptar los mensajes. Por ejemplo, que para dificultar la tarea de los criptoanalistas los
# mensajes enviados no contienen espacios. Se ha organizado un grupo de trabajo para
# generar un algoritmo para quebrar la seguridad. El trabajo se dividió en diferentes partes. A
# usted le toca, dado un string “desencriptado” y sin espacios, determinar si lo que se lee
# corresponde a un posible mensaje en idioma castellano. El proceso debe ser rápido dado
# que se debe utilizar muchas veces. Cuenta con un diccionario de “n” palabras. y con una
# cadena de texto con el posible mensaje.
# Ejemplo: si el diccionario es “peso”, “pesado”, “oso”, “soso”, “pesa”, “dote”, ”a”, “te”,
# para la cadena de texto “osopesadotepesa”. Existe un posible mensaje con las palabras
# “oso”, “pesado”, “te”, “pesa”. Para la cadena de texto “ososoapesadote”. No existe un posible
# mensaje

# a. Construir una solución que informe si la cadena de entrada es un posible texto
# utilizando programación dinámica.

# b. Existe la posibilidad de que una cadena de texto puede corresponder a más de un
# mensaje. Modifique su solución para que se informen todos los posibles mensajes.
# Determine el impacto en las complejidades en el nuevo algoritmo.


                 #OPT[i]  existe si y solo si se tiene OPT(j) == True + diccionario(palabra[j:i]) == True

def hacker(palabra, diccionario):
    n = len(palabra)
    OPT = [False] * (n+1)
    OPT[0] = True
    posibles_resultados = []
    for i in range(1,n+1):
        for j in range(i):
            if OPT[j] == True and palabra[j:i] in diccionario:
                OPT[i] = True
                posibles_resultados.append(palabra[j:i])
                break

    return (OPT[len(palabra)], posibles_resultados)



if __name__ == "__main__":
    palabra = "osopesadotepesa"
    diccionario = ["oso", "pesado","te","pesa"]
    print(hacker(palabra,diccionario))
    



#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.