"""Verificações de ordenação e persistência usando apenas a biblioteca padrão."""

import io
import random
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from algoritmos import bubbleSort, selectionSort
from kdd import gerar_glossario
from kdd_comparacao import ler_palavras


class TestOrdenacao(unittest.TestCase):
    def test_algoritmos_preservam_valores_e_ordenam(self):
        casos = [[], [1], [3, 2, 1], [1, 2, 3], [4, 4, 2],
                 [-3, 0, -8, 9], ["ação", "Acordo", "lei,", "lei", "lei"]]
        gerador = random.Random(2819)
        casos.extend([gerador.choices(range(-20, 21), k=30) for _ in range(100)])
        for ordenar in [bubbleSort, selectionSort]:
            for caso in casos:
                with self.subTest(algoritmo=ordenar.__name__, entrada=caso):
                    copia = caso.copy()
                    ordenar(copia)
                    self.assertEqual(copia, sorted(caso))

    def test_arquivo_com_acentos_repeticoes_e_linhas_vazias(self):
        with tempfile.TemporaryDirectory() as pasta:
            entrada = Path(pasta) / "entrada.txt"
            saida = Path(pasta) / "saida.txt"
            entrada.write_text("ação lei\n\nAcordo  lei,\tlei\n", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                palavras = gerar_glossario(entrada, saida)
            esperado = sorted(["ação", "lei", "Acordo", "lei,", "lei"])
            self.assertEqual(palavras, esperado)
            self.assertEqual(saida.read_text(encoding="utf-8").splitlines(), esperado)
            self.assertEqual(ler_palavras(entrada), ["ação", "lei", "Acordo", "lei,", "lei"])

    def test_arquivo_vazio(self):
        with tempfile.TemporaryDirectory() as pasta:
            entrada = Path(pasta) / "entrada.txt"
            saida = Path(pasta) / "saida.txt"
            entrada.write_text("", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                gerar_glossario(entrada, saida)
            self.assertEqual(saida.read_text(encoding="utf-8"), "")

    def test_protege_arquivo_de_entrada(self):
        with tempfile.TemporaryDirectory() as pasta:
            entrada = Path(pasta) / "entrada.txt"
            entrada.write_text("lei contrato", encoding="utf-8")
            with self.assertRaises(ValueError):
                gerar_glossario(entrada, entrada)
            self.assertEqual(entrada.read_text(encoding="utf-8"), "lei contrato")

    def test_entrada_inexistente(self):
        with tempfile.TemporaryDirectory() as pasta:
            with self.assertRaises(FileNotFoundError):
                gerar_glossario(Path(pasta) / "ausente.txt", Path(pasta) / "saida.txt")


if __name__ == "__main__":
    unittest.main(verbosity=2)
