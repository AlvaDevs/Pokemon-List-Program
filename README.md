# Pokémon List Program

Este es un programa en Python que implementa diferentes tipos de **listas** en la estructura de datos utilizando un tema relacionado con Pokémon. Se muestran ejemplos prácticos de **listas simplemente enlazadas**, **listas doblemente enlazadas**, y **listas circulares simplemente enlazadas** para organizar y gestionar datos.

## Descripción del Programa

Este programa simula la captura de Pokémon, la gestión de sus movimientos, y la rotación de un equipo Pokémon en una batalla. Utiliza los siguientes tipos de listas:

1. **Lista Simplemente Enlazada**: Para guardar los Pokémon capturados.
2. **Lista Doblemente Enlazada**: Para manejar los movimientos que un Pokémon puede aprender.
3. **Lista Circular Simplemente Enlazada**: Para manejar un equipo Pokémon disponible en una batalla y rotar entre ellos.

### Funcionalidades:

- Captura de Pokémon y almacenamiento en una lista simplemente enlazada.
- Agregación de movimientos a un Pokémon utilizando una lista doblemente enlazada.
- Gestión de un equipo Pokémon en batalla con una lista circular, permitiendo rotaciones cíclicas de los Pokémon.

## Estructura del Código

### Clases y Métodos

- **`NodoPokemon`**: Representa un nodo de la lista simplemente enlazada que contiene el nombre de un Pokémon y un enlace al siguiente nodo.
  
- **`ListaPokemones`**:
  - **`capturar_pokemon(pokemon)`**: Añade un nuevo Pokémon a la lista.
  - **`mostrar_pokemones()`**: Muestra todos los Pokémon capturados en la lista.
  
- **`NodoMovimiento`**: Nodo de la lista doblemente enlazada que contiene un movimiento y enlaces tanto al siguiente como al anterior nodo.
  
- **`ListaMovimientos`**:
  - **`agregar_movimiento(movimiento)`**: Añade un nuevo movimiento a la lista.
  - **`mostrar_movimientos()`**: Muestra todos los movimientos del Pokémon.
  
- **`NodoEquipo`**: Nodo de la lista circular que contiene el nombre de un Pokémon y un enlace al siguiente nodo.
  
- **`ListaEquipoCircular`**:
  - **`agregar_pokemon(pokemon)`**: Añade un nuevo Pokémon al equipo circular.
  - **`mostrar_equipo(vueltas)`**: Muestra el equipo Pokémon haciendo un número determinado de vueltas en la lista circular.
  - **`contar_equipo()`**: Devuelve la cantidad de Pokémon en el equipo.