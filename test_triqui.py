import unittest

from triqui import Tablero, LINEAS_GANADORAS, jugada_computadora


def tablero_con(casillas):
    t = Tablero()
    t.casillas = list(casillas)
    return t


class TestTablero(unittest.TestCase):
    def test_jugada_valida_y_ocupada(self):
        t = Tablero()
        self.assertTrue(t.jugar(0, "X"))
        self.assertFalse(t.jugar(0, "O"))
        self.assertFalse(t.jugar(9, "O"))
        self.assertFalse(t.jugar(-1, "O"))

    def test_las_ocho_lineas_ganan(self):
        for linea in LINEAS_GANADORAS:
            t = Tablero()
            for pos in linea:
                t.jugar(pos, "O")
            self.assertEqual(t.ganador(), "O")

    def test_empate(self):
        t = tablero_con("XOXXOOOXX")
        self.assertIsNone(t.ganador())
        self.assertTrue(t.lleno())

    def test_sin_ganador_aun(self):
        t = tablero_con("XO       ")
        self.assertIsNone(t.ganador())
        self.assertFalse(t.lleno())


class TestComputadora(unittest.TestCase):
    def test_gana_si_puede(self):
        t = tablero_con("OO XX    ")
        self.assertEqual(jugada_computadora(t, "O"), 2)

    def test_bloquea_al_rival(self):
        t = tablero_con("XX  O    ")
        self.assertEqual(jugada_computadora(t, "O"), 2)

    def test_toma_el_centro(self):
        t = tablero_con("X        ")
        self.assertEqual(jugada_computadora(t, "O"), 4)


if __name__ == "__main__":
    unittest.main()
