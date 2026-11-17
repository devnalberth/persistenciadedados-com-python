"""Microatividade 3: Selection Sort em uma lista de 15 inteiros."""

from algoritmos import selectionSort

numeros = [42, 7, 19, 3, 88, 12, 65, 1, 34, 9, 56, 23, 78, 4, 31]
print("Antes:", numeros)
selectionSort(numeros)
print("Depois (Selection Sort):", numeros)
