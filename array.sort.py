"""Microatividade 1: ordenação crescente e decrescente com list.sort()."""

numeros = [42, 7, 19, 3, 88, 12, 65, 1, 34, 9, 56, 23, 78, 4, 31]
print("Números originais:", numeros)
numeros.sort()
print("Números crescentes:", numeros)
numeros.sort(key=None, reverse=True)
print("Números decrescentes:", numeros)

palavras = ["nome", "dataNascimento", "cpf", "rg"]
print("Strings originais:", palavras)
palavras.sort()
print("Strings crescentes:", palavras)
palavras.sort(key=None, reverse=True)
print("Strings decrescentes:", palavras)
