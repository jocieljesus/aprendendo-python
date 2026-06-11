buscador = [
    [10, 22, 15],
    [40, 17, 35],
    [54, 72, 28]
]

busca = int(input("Digite um numero que deseja procurar: "))

achou = False

for i in range(len(buscador)):
    for j in range(len(buscador[i])):
        if buscador[i][j] == busca:
            print(f" O numero que você procura está na linha {i+1} e na coluna {j+1}")
            achou = True
            break
    if achou:
        break

if not achou:
    print("Número não encontrado")





