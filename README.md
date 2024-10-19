# Carrera de Carritos 🚗💨

Este es un mini proyecto en Python que simula una carrera de carritos en la terminal. Los competidores avanzan de manera aleatoria hasta alcanzar la meta, y el primero en llegar es coronado como el ganador.

## Características

- **Carrera rápida**: Los carritos compiten sin nombres personalizados.
- **Carrera con nombres**: Los usuarios pueden ingresar nombres para cada carrito.
- **Sistema de clasificación**: Al final de cada carrera, se muestra el ranking de los carritos según su avance.
- **Animación**: Se muestra el progreso de los carritos en tiempo real en la terminal.

## Requisitos

- Python 3.x

## Instrucciones de Uso

1. Clona o descarga este repositorio en tu máquina.

```bash
git clone https://github.com/EddyBel/CarreraDeAutos.git
```

2. Ejecuta el script principal:

```bash
python main.py
```

3. Selecciona una de las opciones del menú:

   - **Iniciar carrera rápida**: Comienza una carrera sin nombres personalizados.
   - **Iniciar carrera con nombres**: Los jugadores pueden ingresar nombres personalizados para los carritos.
   - **Salir**: Cierra el programa.

4. Observa el progreso de los carritos en la terminal.
5. El primer carrito en cruzar la meta será declarado ganador. Luego, se mostrará el ranking de todos los competidores basado en su avance.

## Ejemplo de Salida

```
--- Menú Principal ---
1. Iniciar carrera rápida
2. Iniciar carrera con nombres
3. Salir

Selecciona una opción: 1

--------------------------------------------------------------------------------------|
Carrito 1 (10km)
           .-'--`-._
           '-O---O--'
--------------------------------------------------------------------------------------|
Carrito 2 (8km)
        .-'--`-._
        '-O---O--'
--------------------------------------------------------------------------------------|
...
◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼
◼   ¡Carrito 1 ha ganado!   ◼
◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼

Ranking final:
1 :: Carrito 1 con avance de 150km
2 :: Carrito 2 con avance de 140km
```

## Personalización

El constructor de la clase `Carrera` acepta los siguientes parámetros:

- `competidores`: Número de competidores (por defecto 5).
- `meta`: Longitud de la carrera (por defecto 150).
- `time`: Tiempo de espera entre cada actualización del avance (por defecto 0.05 segundos).
- `useName`: Si se desea usar nombres personalizados para los carritos (`True`/`False`).

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, siéntete libre de abrir un pull request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT.
