"""Algoritmos usados nas microatividades e na etapa de comparação."""


def bubbleSort(array):
    """Ordena a própria lista comparando elementos vizinhos."""
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporario = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporario


def selectionSort(array):
    """Ordena a própria lista procurando o menor elemento restante."""
    for i in range(len(array)):
        indice_menor = i
        for j in range(i + 1, len(array)):
            if array[indice_menor] > array[j]:
                indice_menor = j
        # A troca simultânea preserva os dois valores originais.
        array[i], array[indice_menor] = array[indice_menor], array[i]
