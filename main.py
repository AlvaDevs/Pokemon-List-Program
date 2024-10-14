# Nodo para la lista simplemente enlazada
class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon  # Dato del nodo (nombre del Pokémon)
        self.siguiente = None   # Apunta al siguiente nodo


# Lista simplemente enlazada para capturar Pokémon
class ListaPokemones:
    def __init__(self):
        self.head = None  # Inicialmente la lista está vacía

    def capturar_pokemon(self, pokemon):
        # Añadir un nuevo Pokémon al final de la lista
        nuevo_nodo = NodoPokemon(pokemon)
        if not self.head:  # Si la lista está vacía
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:  # Recorre hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_pokemones(self):
        # Mostrar todos los Pokémon capturados
        actual = self.head
        while actual:
            print(actual.pokemon)
            actual = actual.siguiente


# Nodo para la lista doblemente enlazada (movimientos)
class NodoMovimiento:
    def __init__(self, movimiento):
        self.movimiento = movimiento  # Dato del nodo (nombre del movimiento)
        self.siguiente = None         # Enlace al siguiente nodo
        self.anterior = None          # Enlace al nodo anterior


# Lista doblemente enlazada para movimientos de un Pokémon
class ListaMovimientos:
    def __init__(self):
        self.head = None  # Inicialmente la lista está vacía

    def agregar_movimiento(self, movimiento):
        # Añadir un nuevo movimiento al final de la lista
        nuevo_nodo = NodoMovimiento(movimiento)
        if not self.head:  # Si la lista está vacía
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def mostrar_movimientos(self):
        # Mostrar todos los movimientos en orden
        actual = self.head
        print("Movimientos disponibles:")
        while actual:
            print(actual.movimiento)
            actual = actual.siguiente


# Nodo para la lista circular simplemente enlazada (equipo Pokémon)
class NodoEquipo:
    def __init__(self, pokemon):
        self.pokemon = pokemon  # Dato del nodo (nombre del Pokémon)
        self.siguiente = None   # Enlace al siguiente nodo


# Lista circular simplemente enlazada para manejar el equipo de Pokémon
class ListaEquipoCircular:
    def __init__(self):
        self.head = None  # Inicialmente vacía
        self.tail = None  # Nodo de referencia al final de la lista

    def agregar_pokemon(self, pokemon):
        # Añadir un nuevo Pokémon al equipo
        nuevo_nodo = NodoEquipo(pokemon)
        if not self.head:  # Si la lista está vacía
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            nuevo_nodo.siguiente = self.head  # Enlace circular
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.head
            self.tail = nuevo_nodo

    def mostrar_equipo(self, vueltas=1):
        # Mostrar el equipo Pokémon, puede hacer varias vueltas
        actual = self.head
        contador = 0
        if actual:
            while contador < vueltas * self.contar_equipo():
                print(f"Pokémon en batalla: {actual.pokemon}")
                actual = actual.siguiente
                contador += 1

    def contar_equipo(self):
        # Método para contar cuántos Pokémon hay en el equipo
        if not self.head:
            return 0
        actual = self.head
        contador = 1
        while actual.siguiente != self.head:
            actual = actual.siguiente
            contador += 1
        return contador


# Programa principal
if __name__ == "__main__":
    # 1. Lista simplemente enlazada para Pokémon capturados
    print("Capturando Pokémon...")
    lista_pokemones = ListaPokemones()
    lista_pokemones.capturar_pokemon("Sprigatito")
    lista_pokemones.capturar_pokemon("Fuecoco")
    lista_pokemones.capturar_pokemon("Quaxly")
    lista_pokemones.mostrar_pokemones()

    print("\n---\n")

    # 2. Lista doblemente enlazada para movimientos de un Pokémon
    print("Agregando movimientos a Sprigatito...")
    lista_movimientos = ListaMovimientos()
    lista_movimientos.agregar_movimiento("Follaje")
    lista_movimientos.agregar_movimiento("Arañazo")
    lista_movimientos.agregar_movimiento("Latigo")
    lista_movimientos.mostrar_movimientos()

    print("\n---\n")

    # 3. Lista circular para el equipo Pokémon en batalla
    print("Formando el equipo Pokémon para la batalla...")
    equipo_circular = ListaEquipoCircular()
    equipo_circular.agregar_pokemon("Sprigatito")
    equipo_circular.agregar_pokemon("Fuecoco")
    equipo_circular.agregar_pokemon("Quaxly")
    
    # Mostrar el equipo en batalla haciendo una vuelta completa
    equipo_circular.mostrar_equipo(vueltas=2)  # Muestra el equipo 2 veces en un ciclo
