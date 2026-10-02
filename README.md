# Triqui

Juego de triqui (tres en raya) para dos jugadores, desarrollado como parte del Curso IA Andes.

## Descripción

El triqui se juega en un tablero de 3x3. Dos jugadores se turnan para marcar una casilla con `X` u `O`. Gana quien logre alinear tres marcas iguales en una fila, columna o diagonal. Si el tablero se llena sin ganador, la partida termina en empate.

## Reglas

1. El jugador `X` empieza la partida.
2. Los jugadores alternan turnos y marcan una casilla vacía.
3. Gana quien complete una línea de tres (horizontal, vertical o diagonal).
4. Si las nueve casillas quedan ocupadas sin ganador, es empate.

## Plan de desarrollo

1. **Tablero**: representar el tablero como una estructura de 9 casillas.
2. **Turnos**: alternar entre `X` y `O` y rechazar jugadas en casillas ocupadas.
3. **Detección de ganador**: comprobar las 8 combinaciones ganadoras (3 filas, 3 columnas, 2 diagonales).
4. **Detección de empate**: terminar la partida cuando el tablero esté lleno.
5. **Interfaz**: mostrar el tablero y recibir las jugadas de los jugadores.
6. **Reinicio**: permitir comenzar una nueva partida.
7. **Mejoras opcionales**: marcador de partidas y jugador contra la computadora.

## Estructura del proyecto

```
Triqui/
├── README.md
├── triqui.py        # lógica del juego e interfaz de consola
└── test_triqui.py   # pruebas unitarias
```

## Cómo ejecutarlo

Requiere Python 3.8 o superior, sin dependencias externas.

```bash
python triqui.py
```

Las casillas se numeran del 1 al 9 (de izquierda a derecha y de arriba abajo). Al iniciar puedes elegir jugar contra la computadora, que gana si puede, bloquea al rival, prefiere el centro y si no juega al azar.

## Pruebas

```bash
python -m unittest -v
```

## Estado

Implementados todos los puntos del plan: tablero, turnos, ganador, empate, interfaz, reinicio, marcador y modo contra la computadora.
