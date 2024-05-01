import string
import json
m1 = [["a"]]
m2 = [
    ['b', 'b', 'b'],
    ['b', 'a', 'b'],
    ['b', 'b', 'b']
]


def matriz_letras(n_letras):
    characters = string.ascii_lowercase + string.ascii_uppercase

    if n_letras == 0:
        return []

    matriz = [["a"]]

    for index in range(1, n_letras):
        for i in range(2*index-1):
            matriz[i].insert(0, characters[index])
            matriz[i].append(characters[index])
        matriz.insert(0, [characters[index] for i in range(2*index+1)])
        matriz.append([characters[index] for i in range(2*index+1)])

    return matriz


def salvar_matrizes(path):
    matrizes = {}
    for i in range(53):
        matrizes[i] = matriz_letras(i)
        for row in matrizes[i]:
            with open (f'{path}/matrizes.txt', 'a') as file:
                file.write(f"{str(row)}\n")
    return matrizes


def writejson():
    with open ('matrizes.json', 'w') as file:
        json.dump(salvar_matrizes(), file, indent=4)


for row in matriz_letras(3):
    print(row)



    # index = 1
    # matriz[0].insert(0, characters[index])
    # matriz[0].append(characters[index])

    # matriz.insert(0, [characters[index] for i in range(2*index+1)])
    # matriz.append([characters[index] for i in range(2*index+1)])

    # index = 2
    # matriz[0].insert(0, characters[index])
    # matriz[0].append(characters[index])

    # matriz[1].insert(0, characters[index])
    # matriz[1].append(characters[index])

    # matriz[2].insert(0, characters[index])
    # matriz[2].append(characters[index])

    # matriz.insert(0, [characters[index] for i in range(2*index+1)])
    # matriz.append([characters[index] for i in range(2*index+1)])

    # index = 3
    # matriz[0].insert(0, characters[index])
    # matriz[0].append(characters[index])

    # matriz[1].insert(0, characters[index])
    # matriz[1].append(characters[index])

    # matriz[2].insert(0, characters[index])
    # matriz[2].append(characters[index])

    # matriz[3].insert(0, characters[index])
    # matriz[3].append(characters[index])

    # matriz[4].insert(0, characters[index])
    # matriz[4].append(characters[index])

    # matriz.insert(0, [characters[index] for i in range(2*index+1)])
    # matriz.append([characters[index] for i in range(2*index+1)])

    # index = 4
    # matriz[0].insert(0, characters[index])
    # matriz[0].append(characters[index])

    # matriz[1].insert(0, characters[index])
    # matriz[1].append(characters[index])

    # matriz[2].insert(0, characters[index])
    # matriz[2].append(characters[index])

    # matriz[3].insert(0, characters[index])
    # matriz[3].append(characters[index])

    # matriz[4].insert(0, characters[index])
    # matriz[4].append(characters[index])

    # matriz[5].insert(0, characters[index])
    # matriz[5].append(characters[index])

    # matriz[6].insert(0, characters[index])
    # matriz[6].append(characters[index])

    # matriz.insert(0, [characters[index] for i in range(2*index+1)])
    # matriz.append([characters[index] for i in range(2*index+1)])

            
