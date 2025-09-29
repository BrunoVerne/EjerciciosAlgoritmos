# Un centro de distribución de repuestos ferroviarios se encuentra en un punto de la red
# de este transporte. Es la encargada de distribuir a demanda los materiales y recursos para
# las reparaciones que solicitan las diferentes estaciones. Como la red es antigua y está mal
# mantenida la cantidad de kilos que se puede transferir sobre cada trayecto es variable. Esto
# para ellos es un problema porque quieren enviar la mayor cantidad posible de material por
# viaje. Tanto es así que no les importa realizar un camino más largo siempre que eso implique
# transportar más materiales. Se pueden armar diferentes caminos que unan el centro de
# distribución con cada estación. Estos estarán conformados por una secuencia de trayectos,
# cada uno con su propia limitación de kilos que soporta. Llamamos cuello de botella al valor
# mínimo entre ellos. Construir un algoritmo greedy que permita calcular el camino con el
# máximo cuello de botella entre el punto de partida y el resto de los puntos.


Inicialización:
  Para cada estación v:
      cuello_botella[v] = 0
  cuello_botella[origen] = infinito

  Estaciones por visitar = todas las estaciones

Mientras haya estaciones por visitar:
  Encontrar la estación u no visitada con mayor cuello_botella[u]
  Marcar u como visitada
  
  Para cada estación vecina v de u (no visitada):
    capacidad_trayecto = capacidad entre u y v
    nuevo_cuello = mínimo entre cuello_botella[u] y capacidad_trayecto
    
    Si nuevo_cuello > cuello_botella[v]:
      cuello_botella[v] = nuevo_cuello

Al final, cuello_botella[v] contiene el máximo cuello de botella posible desde el origen hasta v.



#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.