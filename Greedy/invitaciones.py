# El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la
# que desea invitar a la máxima cantidad de sus “n” socios. Sin embargo por protocolo cada
# persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4
# personas invitadas. Nos solicita seleccionar el mayor número posible de invitados. Proponga
# una estrategia greedy óptima para resolver el problema.

#PSEUDOCODIGO

class Socio:
    def __init__(self, nombre, conocidos):
        self.nombre = nombre
        self.conocidos = conocidos 
        
        
   
def seleccionar_invitados(n):
    cola = set()

    for s in n:
        if s.conocidos < 4: 
            n.remove(s)
            for conocido in s.conocidos:
                cola.add(conocido)

    seDesinvito = True
    while seDesinvito:
        seDesinvito = False
        for c in cola:
            if c.conocidos < 4:
                n.remove(c)
                for conocido in c.conocidos:
                    cola.add(conocido)
                    conocido.conocidos -=1
                
                seDesinvito = True
            cola.remove(c)

    
    for socioAinvitar in n:
        socioAinvitar.invitar



def invitar(self):
    print(f"{self.nombre} ha sido invitado.")




# Considere el problema anterior, pero con la adición de una nueva restricción: Los
# organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos
# solicitan que sólo puede asistir si NO conoce al menos otras 4 personas invitadas. Modiﬁque
# su propuesta para satisfacer esta nueva solución.


def seleccionar_invitados2(invitados):
    revisar = set()
    desinvitados = set()

    for s in invitados:
        
                
        if len(invitados) - len(s.conocidos) < 4: # desconocidos = cantidad de invitados - conocidos
            invitados.remove(s)
            desinvitados.add(s)
            
            for conocido in s.conocidos:
                if conocido in desinvitados:
                    conocido.conocidos.remove(s)
                    revisar.add(conocido)       
        

    seAgrego = True
    while seAgrego:
        seAgrego = False
        
        invitados = len(invitados)
        
        for c in revisar:

            if len(invitados) - len(c.conocidos) >= 4:
                invitados.add(c)
                desinvitados.remove(c)
                revisar.remove(c)
                seAgrego = True
                
                for conocido in c.conocidos:
                    if conocido in invitados:
                        conocido.conocidos.add(c) # porque acabo de meter a un conocido a la lista
                        revisar.add(conocido)         
            else:
                revisar.remove(c)
                for conocido in c.conocidos:
                    if conocido in desinvitados:
                        conocido.conocidos.remove(c)
                        revisar.add(conocido)


            
    for socioAinvitar in invitados:
        socioAinvitar.invitar                                    

    

#expresar la relación de recurrencia, brindar pseudocódigo y calcular la complejidad
#temporal, espacial.


                
    