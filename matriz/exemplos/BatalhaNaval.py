"""
Exercício 3: Batalha Naval Simplificada
Crie uma matriz 4x4 que represente um oceano. Esconda um único navio (representado pelo caractere 'N') em uma posição secreta de sua escolha. Preencha o resto com água ('~'). Peça para o aluno criar um script onde o jogador tenta adivinhar a linha e a coluna. Se ele acertar a posição do 'N', exiba "Você afundou o navio!", caso contrário, exiba "Água!".
"""

oceano = [
    ['~', '~', '~', '~'],
    ['~', '~', '~', '~'],
    ['~', '~', 'N', '~'],
    ['~', '~', '~', '~']
]

print("********************************************")
print("  Bem Vindo ao campo de Batalha Naval 4 x 4 ")
print("********************************************")
print(" Você tem o poder de tentar afundar o meu navio, mas para isso você precisará encontrá-lo.")
print(" Para começar, você precisa escolher para onde irá o seu primeiro canhão.")

while True:

    mira = input(" Mire utilizando a linha e a coluna separados por vírgula para lançar: ").split(",")
    linha = int(mira[0])
    coluna = int(mira[1])

    if oceano[linha][coluna] == "N":
        print(" VOCÊ AFUNDOU O NAVIO")
        break
    print(" Não foi dessa vez, que tal tentar de novo?")