# El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la
# que desea invitar a la máxima cantidad de sus “n” socios. Sin embargo por protocolo cada
# persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4
# personas invitadas. Nos solicita seleccionar el mayor número posible de invitados. Proponga
# una estrategia greedy óptima para resolver el problema.

#PSEUDOCODIGO

class Socio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conocidos = set() 
        
        
    def invitar(self):
        print(f"{self.nombre} ha sido invitado.")

def seleccionar_invitados(socios):
    
    n = set(socios)
    cola = set()

    for s in list(n):
        if len(s.conocidos & n) < 4: 
            n.remove(s)
            for conocido in s.conocidos:
                cola.add(conocido)

    # Paso 2: propagar efecto de eliminación
    seDesinvito = True
    while seDesinvito:
        seDesinvito = False
        for c in list(cola):
            cola.remove(c)
            if c in n and len(c.conocidos & n) < 4:
                n.remove(c)
                seDesinvito = True
                for conocido in c.conocidos:
                    cola.add(conocido)

    # Paso 3: invitar a los que quedan
    for socioAinvitar in n:
        socioAinvitar.invitar()
