def bolo (a, b, c):
    a = a // 2
    b = b // 3
    c = c //5
    return min(a, b, c)

print(bolo (4, 6, 10))



def matricula(path):
    candidatos = []
    with open(path, "r") as file:
        for line in file:
            candidatos.append(line.removesuffix("\n").split(";"))
    candidatos = sorted(candidatos, key=lambda x: (x[1], -int(x[2]), x[3], x[4], x[5]))
    candidatos = candidatos[::-1]
    pontuacao = []
    for i in range(len(candidatos)):
       pontuacao.append([candidatos[i][0], candidatos[i][1] + candidatos[i][2] + candidatos[i][3] + candidatos[i][4] + candidatos[i][5]])
    
    pos = 1
    final = ""
    for i in range(len(pontuacao)):
        final += f"{pos} {pontuacao[i][0]}\n"
        try:
            if pontuacao[i][1] == pontuacao[i+1][1]:
                pos = pos
            else:
                pos += 1
        except IndexError: pass

    print(final)



def ordem(cartas=str):
    nums = [int(carta) for carta in cartas.split()]
    arrumado = sorted(nums)
    if nums == arrumado: return "C"
    if nums == arrumado[::-1]: return "D"
    return "N"

# cartas = input()
# print (ordem(cartas))

def maior_soma_continua(conjunto):
    soma = sum(conjunto)
    for i in range(len(conjunto)):
        for j in range(len(conjunto)+1):
            if sum(conjunto[i:j]) > soma: soma = sum(conjunto[i:j])
    return soma


def troco():
    valor_e_moedas = input().split()
    moedas = [int(i) for i in input().split()]
    preco = int(valor_e_moedas[0])
    if preco in moedas: return "S"
    for moeda in moedas:
        if preco - moeda in moedas: return "S"
    
    return "N"

print()