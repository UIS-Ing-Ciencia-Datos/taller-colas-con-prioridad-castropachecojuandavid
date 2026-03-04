class Nodo:
    def _init_(self, data, prioridad):
        self.data=data
        self.siguiente=None
        self.prioridad=prioridad

class cola:
    def _init_(self):
        self.cabeza=None

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente

    def agregar(self,data,prioridad):
        nuevoNodo=Nodo(data,prioridad)
        if self.cabeza is None:
            self.cabeza=nuevoNodo
            return
        elif nuevoNodo.prioridad<=self.cabeza.prioridad:
            nuevoNodo.siguiente=self.cabeza
            self.cabeza=nuevoNodo
            return
        actual=self.cabeza
        while actual.siguiente is not None and actual.siguiente.prioridad<=prioridad:
            actual=actual.siguiente
        nuevoNodo.siguiente = actual.siguiente
        actual.siguiente = nuevoNodo

    def eliminar(self):
        if self.cabeza is None:
            print("No hay nada que eliminar")
            return None
        eliminado = self.cabeza          
        self.cabeza = self.cabeza.siguiente  
        eliminado.siguiente = None       
        print(f"Llamada de '{eliminado.data}' atendida.")
        return eliminado

colita=cola()

cent=0
while cent!=4:
    print("1. Ingresar Llamada")
    print("2. Pasar siguiente solicitud")
    print("3. Mostrar la cola")
    print("4. Salir")
    opc=int(input("Seleccione una opcion: "))
    if opc==1:
        prio=0
        nom=str(input("Ingrese su nombre: "))
        edad=int(input("Digite su edad (en años): "))
        if edad>=0 and edad<=12:
            prio=prio+1
        elif edad>65:
            prio=prio+2
        else:
            prio=prio+3
        print("Opciones de direccion")
        print("1. Zona urbana (unidad movil motorizada)")
        print("2. Zona rural o de alto riesgo (patrulla y unidades de refuerzo)")
        dire=int(input("Seleccione una opcion de direccion: "))
        if dire==1:
            prio=prio+1
        elif dire==2:
            prio=prio+2
        else:
            print("Opcion invalida")
        mot=str(input("Cual es el motivo de su llamada?: "))
        gra=int(input("Del 1-5 cuan califica que es la gravedad de su emergencia (siendo 1 la de mayor gravedad): "))
        if gra==1:
            prio=prio+1
        elif gra==2:
            prio=prio+2
        elif gra==3:
            prio=prio+3
        elif gra==4:
            prio=prio+4
        elif gra==5:
            prio=prio+5
        else:
            print("Opcion invalida")
        colita.agregar(nom,prio)
    elif opc==2:
        colita.eliminar()
        colita.imprimir()
    elif opc==3:
        colita.imprimir()
    elif opc==4:
        cent=4
    else:
        print("Opcion invalida")