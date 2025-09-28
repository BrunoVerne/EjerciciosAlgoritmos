# Una familia planea un viaje. Tienen pensado salir desde su ciudad a una determinada
# hora y llegar lo antes que puedan a la ciudad de destino. Para hacer el viaje cuentan con
# diferentes opciones de recorridos. Diferentes rutas pasan por diferentes pueblos y se
# ramiﬁcan en otras rutas diferentes. Cada trayecto cuenta con una longitud que - teniendo en
# cuenta el límite de velocidad - les permite establecer el tiempo que les llevará recorrerlo. Por
# otro lado, conocen el tráﬁco por hora de cada trayecto. Esto es, el tiempo extra que le
# insume realizar un trayecto si inician el recorrido en una determinada hora. Construir un
# algoritmo greedy que determine el mejor camino a realizar en el menor tiempo posible.


Inicializar:
  tiempo[nodo] = infinito para todos los nodos
  tiempo[origen] = hora_salida
  previo[nodo] = ninguno

Mientras haya nodos por visitar:
  Tomar nodo u con menor tiempo actual
  Para cada vecino v de u:
    hora_llegada_a_u = tiempo[u]
    tiempo_trayecto = tiempo_base(u,v) + trafico(hora_llegada_a_u)
    tiempo_total = tiempo[u] + tiempo_trayecto
    
    Si tiempo_total < tiempo[v]:
      tiempo[v] = tiempo_total
      previo[v] = u

Recuperar camino desde destino hacia origen