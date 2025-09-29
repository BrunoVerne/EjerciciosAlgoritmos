# Para habilitar la realización de un importante evento multideportivo se solicitó como
# precondición que durante el lapso que dura cada actividad exista junto a la misma personal
# médico. Conocemos para cada una de las “n” actividades a realizar, el momento de inicio y
# ﬁnal. Como encargados de la inspección nos solicitan que programemos la menor cantidad
# de inspecciones posibles en las que constatamos que (al menos al momento de la
# inspección) se cumple la precondición. Una inspección veriﬁca únicamente aquellos eventos
# que se están llevando a cabo en el momento. Ninguna actividad debe quedar sin
# inspeccionar. Presentar una solución greedy óptima al problema.


ordenar actividades por fin
singuardar = actividades[0]
horarios = lista vacía

for i en 1 to len(actividades)-1:
    si actividades[i].inicio > singuardar.fin:
        horarios.agregar(singuardar.fin)
        singuardar = actividades[i]

horarios.agregar(singuardar.fin)

return horarios




#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.