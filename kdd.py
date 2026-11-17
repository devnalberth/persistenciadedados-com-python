"""MVP final: lê palavras de um TXT, ordena e persiste em outro TXT."""

import argparse
from pathlib import Path
from time import perf_counter

PASTA = Path(__file__).resolve().parent


def gerar_glossario(entrada, saida):
    if entrada.resolve() == saida.resolve():
        raise ValueError("A saída deve ser diferente do arquivo de entrada.")

    palavras = list()
    with open(entrada, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.extend(linha.split())

    # Método escolhido após a comparação registrada no arquivo de resultados.
    inicio = perf_counter()
    palavras.sort()
    duracao = perf_counter() - inicio

    with open(saida, "w", encoding="utf-8") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")

    print("Palavras ordenadas:", palavras)
    print("Quantidade de palavras:", len(palavras))
    print(f"Tempo de ordenação (list.sort): {duracao:.9f} s")
    print("Arquivo salvo em:", saida.resolve())
    return palavras


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", nargs="?", type=Path, default=PASTA / "entrada.txt")
    parser.add_argument("--saida", type=Path, default=PASTA / "palavras_ordenadas.txt")
    args = parser.parse_args()
    try:
        gerar_glossario(args.entrada, args.saida)
    except (OSError, UnicodeError, ValueError) as erro:
        parser.exit(1, f"Não foi possível gerar o glossário: {erro}\n")


if __name__ == "__main__":
    main()
