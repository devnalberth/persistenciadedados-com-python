"""Microatividade 4: leitura completa, por linha e por caracteres."""

from pathlib import Path

caminho = Path(__file__).resolve().parent / "loremipsum.txt"
arquivo = open(caminho, "r", encoding="utf-8")
try:
    conteudo = arquivo.read()
    print("Conteúdo completo:\n" + conteudo)
    # read() deixa o cursor no fim: seek(0) permite ler desde o início.
    arquivo.seek(0)
    print("Primeira linha:", arquivo.readline().rstrip("\n"))
    arquivo.seek(0)
    print("Três primeiros caracteres:", arquivo.read(3))
finally:
    arquivo.close()

with open(caminho, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Leitura usando with:\n" + conteudo)
