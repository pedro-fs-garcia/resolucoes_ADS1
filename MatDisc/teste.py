import string

def matriz_letras(n_letras):
    if n_letras <= 0:
        return []

    characters = string.ascii_lowercase
    matriz = []

    for i in range(n_letras * 2 - 1):
        row = [characters[max(abs(n_letras - i - 1), abs(n_letras - (n_letras * 2 - i - 1)))] for _ in range(n_letras * 2 - 1)]
        matriz.append(row)

    return matriz

# Exemplo de uso:
matriz = matriz_letras(3)
for row in matriz:
    print(row)


