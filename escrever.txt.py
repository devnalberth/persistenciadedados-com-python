"""Microatividade 5: escrita das frases de uma lista em um TXT."""

from pathlib import Path

caminho = Path(__file__).resolve().parent / "texto.txt"
texto = list()
texto.append("Aprendendo persistência de dados com Python.\n")
texto.append("Listas podem ser ordenadas de várias formas.\n")
texto.append("Arquivos de texto permitem guardar os resultados.\n")

with open(caminho, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(texto)

print("Arquivo criado:", caminho)
