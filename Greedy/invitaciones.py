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
        if len(s.conocidos ) < 4: 
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
        socioAinvitar.invitar()



def invitar(self):
    print(f"{self.nombre} ha sido invitado.")

