"""Etapa experimental: três métodos recebem cópias da mesma lista original."""

import argparse
import json
import platform
import statistics
from pathlib import Path
from time import perf_counter

from algoritmos import bubbleSort, selectionSort

PASTA = Path(__file__).resolve().parent


def ler_palavras(caminho):
    palavras = list()
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.extend(linha.split())
    return palavras


def repeticoes_positivas(valor):
    numero = int(valor)
    if numero < 1:
        raise argparse.ArgumentTypeError("Use pelo menos uma repetição.")
    return numero


def comparar(entrada, repeticoes):
    originais = ler_palavras(entrada)
    esperado = sorted(originais)
    metodos = {"Bubble Sort": bubbleSort, "Selection Sort": selectionSort,
               "list.sort()": list.sort}
    resultados = {}
    for nome, ordenar in metodos.items():
        tempos = []
        for _ in range(repeticoes):
            # A cópia e a verificação ficam fora do intervalo cronometrado.
            copia = originais.copy()
            inicio = perf_counter()
            ordenar(copia)
            tempos.append(perf_counter() - inicio)
            if copia != esperado:
                raise RuntimeError("Resultado incorreto: " + nome)
        resultados[nome] = {
            "tempos_segundos": tempos,
            "mediana_segundos": statistics.median(tempos),
        }
        print("\nMétodo:", nome)
        print("Palavras ordenadas:", copia)
        print("Tempos (s):", ", ".join(f"{tempo:.9f}" for tempo in tempos))
        print(f"Mediana: {statistics.median(tempos):.9f} s")

    vencedor = min(resultados, key=lambda nome: resultados[nome]["mediana_segundos"])
    relatorio = {
        "python": platform.python_version(),
        "sistema": platform.system(),
        "entrada": entrada.name,
        "quantidade_palavras": len(originais),
        "repeticoes": repeticoes,
        "metodos": resultados,
        "menor_mediana": vencedor,
    }
    with open(PASTA / "resultados_comparacao.json", "w", encoding="utf-8") as arquivo:
        json.dump(relatorio, arquivo, ensure_ascii=False, indent=2)
        arquivo.write("\n")
    print("\nMenor mediana nesta execução:", vencedor)
    print("Relatório salvo em:", PASTA / "resultados_comparacao.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", nargs="?", type=Path, default=PASTA / "entrada.txt")
    parser.add_argument("--repeticoes", type=repeticoes_positivas, default=5)
    args = parser.parse_args()
    try:
        comparar(args.entrada, args.repeticoes)
    except (OSError, UnicodeError) as erro:
        parser.exit(1, f"Não foi possível ler a entrada ou salvar o relatório: {erro}\n")


if __name__ == "__main__":
    main()
