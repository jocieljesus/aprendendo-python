frase = input("Digite a frase: ").lower().split()

contagem = {}

for palavra in frase:
    if palavra not in contagem:
        contagem[palavra] =1
    else:
        contagem[palavra] +=1

for i, j in contagem.items():
    print(f"{i} : {j}")
