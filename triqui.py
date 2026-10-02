"""Juego de triqui (tres en raya) por consola."""

import random

LINEAS_GANADORAS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
    (0, 4, 8), (2, 4, 6),             # diagonales
)


class Tablero:
    """Tablero de 3x3 representado como una lista de 9 casillas."""

    def __init__(self):
        self.casillas = [" "] * 9

    def jugar(self, posicion, ficha):
        """Marca la casilla (0-8). Devuelve False si es inválida u ocupada."""
        if not 0 <= posicion < 9 or self.casillas[posicion] != " ":
            return False
        self.casillas[posicion] = ficha
        return True

    def disponibles(self):
        return [i for i, c in enumerate(self.casillas) if c == " "]

    def ganador(self):
        """Devuelve 'X', 'O' o None."""
        for a, b, c in LINEAS_GANADORAS:
            if self.casillas[a] != " " and self.casillas[a] == self.casillas[b] == self.casillas[c]:
                return self.casillas[a]
        return None

    def lleno(self):
        return not self.disponibles()

    def __str__(self):
        c = [x if x != " " else str(i + 1) for i, x in enumerate(self.casillas)]
        filas = [f" {c[i]} | {c[i + 1]} | {c[i + 2]} " for i in (0, 3, 6)]
        return "\n---+---+---\n".join(filas)


def jugada_computadora(tablero, ficha):
    """Elige una jugada: ganar, bloquear, centro, o al azar."""
    rival = "O" if ficha == "X" else "X"
    for objetivo in (ficha, rival):
        for pos in tablero.disponibles():
            tablero.casillas[pos] = objetivo
            gana = tablero.ganador() == objetivo
            tablero.casillas[pos] = " "
            if gana:
                return pos
    if 4 in tablero.disponibles():
        return 4
    return random.choice(tablero.disponibles())


def pedir_jugada(tablero, ficha):
    while True:
        entrada = input(f"Turno de {ficha}. Elige casilla (1-9): ").strip()
        if not entrada.isdigit():
            print("Ingresa un número del 1 al 9.")
        elif not tablero.jugar(int(entrada) - 1, ficha):
            print("Casilla inválida u ocupada.")
        else:
            return


def jugar_partida(contra_computadora):
    """Juega una partida. Devuelve 'X', 'O' o None (empate)."""
    tablero = Tablero()
    ficha = "X"
    while True:
        print("\n" + str(tablero) + "\n")
        if contra_computadora and ficha == "O":
            pos = jugada_computadora(tablero, ficha)
            tablero.jugar(pos, ficha)
            print(f"La computadora juega en {pos + 1}.")
        else:
            pedir_jugada(tablero, ficha)
        ganador = tablero.ganador()
        if ganador or tablero.lleno():
            print("\n" + str(tablero) + "\n")
            print(f"¡Ganó {ganador}!" if ganador else "Empate.")
            return ganador
        ficha = "O" if ficha == "X" else "X"


def pedir_si_no(pregunta):
    while True:
        r = input(pregunta + " (s/n): ").strip().lower()
        if r in ("s", "n"):
            return r == "s"


def main():
    print("=== TRIQUI ===")
    contra_pc = pedir_si_no("¿Jugar contra la computadora? (tú eres X)")
    marcador = {"X": 0, "O": 0, "Empates": 0}
    while True:
        ganador = jugar_partida(contra_pc)
        marcador[ganador or "Empates"] += 1
        print(f"Marcador -> X: {marcador['X']}  O: {marcador['O']}  Empates: {marcador['Empates']}")
        if not pedir_si_no("¿Jugar otra partida?"):
            break
    print("¡Gracias por jugar!")


if __name__ == "__main__":
    main()
